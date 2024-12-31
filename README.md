# Raspberry Pi + DIGITEN Flow Meter

This is a Python 3 program for the DIGITEN flow meter (or similar device) using interrupts.

## Device Details

https://www.digiten.shop/collections/counter/products/digiten-g1-2-water-flow-hall-sensor-switch-flow-meter-1-30l-min<br>

### Frequency Calculation:<br>
F = 7.5 * Q (L / Min)<br>
F = Constant * units of flow (L / min) * time (seconds)<br>
450 output pulses/liters<br>

### Deviec Specs:<br>
450 output pulses/liters<br>
error: ± 2%<br>
Flow range: 1-30L/min<br>
current can not exceed 10mA<br>
Maximum current: 15 mA(DC 5V)<br>
Working voltage range: DC 5-24 V<br>
Load capacity: ≤ 10 mA (DC 5V)<br>
Operating Temp: ≤ 80℃<br>
Operating humidity: 35%-90%RH<br>
Allow compression: Water pressure 1.75 Mpa below<br>
Insulation resistance: >100M OHM<br>
Storage Temperature: -25-80℃<br>
Storage humidity: 25%-95%RH<br>
Output Waveform: Square Wave, output pulse signal.<br>
ROHS Compliant.<br>
Sensor:Hall effect<br>
Cable length: 15cm.<br>

## IMPORTANT!<br>
Input MUST go through voltage divider circuit!!!<br>
Input -> 4.7k ohm resistor -> RPi pin 13 + 10k ohm resistor-> Gnd RPi & SR04<br>

Referece:<br>
https://www.youtube.com/watch?v=wpenAP8gN3c<br>
![image](https://github.com/user-attachments/assets/b40440e6-357d-4685-9196-032503a52f99)

## Other Important Points
- A stopped impeller should not give false readings
- I want an email alert when flow starts and stops
- I want the stop email to tell me how much water passed
