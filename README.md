# pi-flow-meter
Raspberry Pi + DIGITEN flow meter

This is a Python 3 program for the DIGITEN (https://www.digiten.shop/collections/counter/products/digiten-g1-2-water-flow-hall-sensor-switch-flow-meter-1-30l-min) flow meter (or similar device) using interrupts.

- Input MUST go through voltage divider circuit!!!
  - Input -> 4.7k ohm resistor -> RPi pin 13 + 10k ohm resistor-> Gnd RPi & SR04

- A stopped impeller should not give false readings
- I want an email alert when flow starts and stops
- I want the stop email to tell me how much water passed

Documentation from the flow meter manufacturer:
Frequency:
- F = 7.5 * Q (L / min)
- F = Constant * units of flow (L / min) * time (seconds)
- 450 output pulses/liters

 ![image](https://github.com/user-attachments/assets/218f624c-8fda-490f-9e78-54b206185ca0)
