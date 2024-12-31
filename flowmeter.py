#!/usr/bin/env python3

# REPLACE SMTP SERVER AND EMAIL ADDRESS DETAILS BELOW

# Notes
#   Python 3 program for the YF-S201 flow meter (or similar device) using interrupts
#   Input MUST go through voltage divider circuit!!!
#   Input -> 4.7k ohm resistor -> RPi pin 13 + 10k ohm resistor-> Gnd RPi & SR04
#   A stopped impeller should not give false readings
#   I want an email alert when flow starts and stops
#   I want the stop email to tell me how much water passed

#   Documentation from the flow meter manufacturer:
#     Frequency:
#     F = 7.5 * Q (L / min)
#     F = Constant * units of flow (L / min) * time (seconds)
#     450 output pulses/liters

from datetime import datetime, timedelta
from gpiozero import Button
import logging
# import sqlite3
import sys
import time
import traceback

# Import email libraries
import smtplib
import ssl
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Count meter pulses fromt the hall effect
def pulse_count():
    global rate_count
    rate_count += 1

# Get the current time in seconds
def get_time():
    stamp = time.time()
    return stamp

# Setup logging
logging.basicConfig(
    filename='flowmeter.log',
    encoding='utf-8',
    level=logging.INFO, # (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    datefmt='%Y-%m-%d %I:%M:%S %p',
    format='%(asctime)s | %(levelname)s | %(message)s'
    )

logging.warning('Service Started')

# Set the GPIO pin used on the Raspberry Pi
flow_sensor = Button(pin=23, bounce_time=0.01)
flow_sensor.when_activated = pulse_count

# Email configuration variables
smtp_server = '[REPLACE WITH YOUR SMTP SERVER]'
smtp_port = 587
smtp_username = '[REPLACE WITH YOUR SMTP USERNAME]'
smtp_password = '[REPLACE WITH YOUR SMTP PASSWORD]'
from_address = 'Flow Meter <[REPLACE WITH YOUR FROM EMAIL ADDRESS]>'
destination_address = '[REPLACE WITH YOUR DESTIATION EMAIL ADDRESS]'

# Initialize variables
rate_count = 0
previous_rate_count = 0
total_duration = 0.0
start_time = 0.0
end_time = 0.0
liters_per_minute = 0

# Loop forever
while True:

    try:

        # Check for water flow
        if (rate_count > previous_rate_count):
            # There is water flowing

            flow_start_time = get_time()

            logging.info('Start Cycle')
            logging.info('Water Flow Detected')

            # Do while there is water flowing...
            while (rate_count > previous_rate_count):
                logging.debug('Rate Count: ' + str(rate_count))
                previous_rate_count = rate_count
                time.sleep(1)

            logging.info('Water Flow Stopped')

            flow_end_time = get_time()

            # Find the total time water was flowing (in seconds)
            total_flow_duration = flow_end_time - flow_start_time
            total_flow_duration_min = total_flow_duration / 60

            total_liters = rate_count / 450

            # Liters per minute calculation
            liters_per_minute = round(((rate_count/450) / total_flow_duration_min), 1)

            logging.info('Final Rate Count: ' + str(rate_count))
            logging.info('Total Duration (min): ' + str(round(total_flow_duration_min, 2)))
            logging.info('Start Time: ' + str(flow_start_time))
            logging.info('End Time: ' + str(flow_end_time))
            logging.info('Liters per Minute: ' + str(liters_per_minute))
            logging.info('Total Liters: ' + str(round(total_liters, 2)))

            if (rate_count > 10):
                # Build the email

                msg = MIMEMultipart('alternative')
                msg_html = """\
                    <html>Flow Meter: 
                    """ + str(round(total_flow_duration_min, 2)) + """ min / """ + str(round(total_liters, 2)) + """ liters
                    </html>
                    """
                msg.attach(MIMEText(msg_html, 'html'))
                msg['From'] = from_address
                msg['To'] = destination_address

                try:
                    # Try to open an SMTP connection and send the email
                    smtp = smtplib.SMTP(smtp_server, smtp_port)
                    context_ssl = ssl.create_default_context()
                    smtp.starttls(context=context_ssl)
                    smtp.login(smtp_username,smtp_password)
                    smtp.send_message(msg)
                    smtp.quit()
                    
                    logging.info('Email Sent Successfully')

                except Exception as ex:
                    # Do if the email can't be sent, throw exception
                    logging.error('There was a problem sending the email.' + str(ex))
                    logging.error(traceback.format_exc())

            # Final water flow time stamp
            logging.info('End Cycle')

            timestamp = datetime.now()
            
            # try:
            #     sql_db_connection = sqlite3.connect('flowmeter.db', detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
            #     sql_cursor = sql_db_connection.cursor()
            #     sql_cursor.execute('INSERT INTO flow_data VALUES(?,?,?,?,?,?,?)', (timestamp, rate_count, flow_start_time, flow_end_time, total_flow_duration_min, liters_per_minute, total_liters))
            #     sql_db_connection.commit()
            # except sqlite3.Error as sql_error:
            #     logging.critical('SQLite update failed!: ' + str(sql_error))
            # finally:
            #     if sql_db_connection:
            #         sql_db_connection.close()

            # Reset some variable
            previous_rate_count = 0
            rate_count = 0
            flow_start_time = 0.0
            flow_end_time = 0.0
            total_flow_duration = 0.0
            liters_per_minute = 0

    except Exception as ex:
        logging.critical(str(ex))
        logging.critical(traceback.format_exc())
        sys.exit(0)

    time.sleep(0.2)
