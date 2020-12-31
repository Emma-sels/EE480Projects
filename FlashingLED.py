#!/usr/bin/python3
# A small Python program to set up GPIO4 as an LED that can be
# turned on or off from the Linux console.
# Written by Derek Molloy for the book "Exploring Raspberry Pi"

import RPi.GPIO as GPIO #importing the RPi GPIO library
from time import sleep #function to add in delay later in code

GPIO.setmode(GPIO.BOARD) #physical pin numbers
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW) #pin 7 (GPIO4) as an output that starts off

while True: #runs till I tell it to stop
    GPIO.output(7, GPIO.HIGH) # LED on
    sleep(.5) # stay on .5 seconds
    GPIO.output(7, GPIO.LOW) # LED off
    sleep(.5) # stay on .5 seconds