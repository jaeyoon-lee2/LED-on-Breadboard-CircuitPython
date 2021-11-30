# Created by: Jaeyoon Lee
# Created on: Nov 2021
#
#  Turns an LED on for one second, then off for one second, repeatedly.

import time
import board
import digitalio

led = digitalio.DigitalInOut(board.GP14)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
