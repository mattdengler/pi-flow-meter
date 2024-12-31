# Raspberry Pi + DIGITEN flow meter

This is a Python 3 program for the DIGITEN (https://www.digiten.shop/collections/counter/products/digiten-g1-2-water-flow-hall-sensor-switch-flow-meter-1-30l-min) flow meter (or similar device) using interrupts.

Flow Meter Specs
Frequency:
F = 7.5 * Q (L / Min)
F = Constant * units of flow (L / min) * time (seconds)

450 output pulses/liters
error: ± 2%
Flow range: 1-30L/min
current can not exceed 10mA
Maximum current: 15 mA(DC 5V)
Working voltage range: DC 5-24 V
Load capacity: ≤ 10 mA(DC 5V)
Operating Temp: ≤ 80℃
Operating humidity: 35%-90%RH
Allow compression: Water pressure 1.75 Mpa below
Insulation resistance: >100M OHM
Storage Temperature: -25-80℃
Storage humidity: 25%-95%RH
Output Waveform: Square Wave, output pulse signal.
ROHS Compliant.
Sensor:Hall effect
Cable length: 15cm.

Packaging include:
G1/2" Flowmeter x 1




Input MUST go through voltage divider circuit!!!
Input -> 4.7k ohm resistor -> RPi pin 13 + 10k ohm resistor-> Gnd RPi & SR04

Referece:
https://www.youtube.com/watch?v=wpenAP8gN3c
![image](https://github.com/user-attachments/assets/b40440e6-357d-4685-9196-032503a52f99)


Other points:
- A stopped impeller should not give false readings
- I want an email alert when flow starts and stops
- I want the stop email to tell me how much water passed


Documentation from the flow meter manufacturer:
Frequency:
- F = 7.5 * Q (L / min)
- F = Constant * units of flow (L / min) * time (seconds)
- 450 output pulses/liters

 ![image](https://github.com/user-attachments/assets/218f624c-8fda-490f-9e78-54b206185ca0)
