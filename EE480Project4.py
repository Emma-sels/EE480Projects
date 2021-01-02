import RPi.GPIO as GPIO #importing the RPi GPIO library
from time import sleep #function to add in delay later in code

GPIO.setmode(GPIO.BOARD) #physical pin numbers
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW) #pin 7 (GPIO4) as an output that starts off
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW) #pin 11 (GPIO17) as an output that starts off
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW) #pin 13 (GPIO27) as an output that starts off
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW) #pin 15 (GPIO22) as an output that starts off
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW) #pin 16 (GPIO23) as an output that starts off

newnum = ' ';
for i in range(31):
    newnum = "{0:05b}".format(i)
    print(newnum);
    digitOne = newnum[0];
    digitTwo = newnum[1];
    digitThree = newnum[2];
    digitFour = newnum[3];
    digitFive = newnum[4];
    if digitFive == '1' :
        GPIO.output(18, GPIO.HIGH) # LED on
    else :
        GPIO.output(18, GPIO.LOW) # LED off
    sleep(2.5) # stay on 2.5 seconds

    if digitFour == '1' :
        GPIO.output(11, GPIO.HIGH) # LED on
    else :
        GPIO.output(11, GPIO.LOW) # LED off
    sleep(2) # stay on .5 seconds

    if digitThree == '1' :
        GPIO.output(13, GPIO.HIGH) # LED on
    else :
        GPIO.output(13, GPIO.LOW) # LED off
    sleep(1.5) # stay on .5 seconds

    if digitTwo == '1' :
        GPIO.output(15, GPIO.HIGH) # LED on
    else :
        GPIO.output(15, GPIO.LOW) # LED off
    sleep(1) # stay on .5 seconds

    if digitOne == '1' :
        GPIO.output(16, GPIO.HIGH) # LED on
    else :
        GPIO.output(16, GPIO.LOW) # LED off
    sleep(.5) # stay on .5 seconds
    GPIO.output(18, GPIO.LOW) # LED off
    GPIO.output(11, GPIO.LOW) # LED off
    GPIO.output(13, GPIO.LOW) # LED off
    GPIO.output(15, GPIO.LOW) # LED off
    GPIO.output(16, GPIO.LOW) # LED off



