import RPi.GPIO as GPIO #importing the RPi GPIO library
from time import sleep #function to add in delay later in code

GPIO.setmode(GPIO.BOARD) #physical pin numbers
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW) #pin 18 (GPIO27) as an output that starts off
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW) #pin 11 (GPIO17) as an output that starts off
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW) #pin 13 (GPIO27) as an output that starts off
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW) #pin 15 (GPIO22) as an output that starts off
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW) #pin 16 (GPIO23) as an output that starts off

# creating a menu to present to the user for options 
menu = {}
menu['1']="Sequential Count in Binary"
menu['2']="Sweeping Light Movement from Left to Right"
menu['3']="Sweeping Light Movement from Right to left"
menu['4']="Continuous Sweeping Light Movement"
menu['5']="User input decimal to Binary conversion"

while True: # continuously prompts user for a response until program is terminated 
    options = menu.keys() #options based off user keys 
    options.sort()
    for entry in options: # for loop to print off the menu for user to see 
        print entry, menu[entry]
    
    selection=raw_input("Please select from the menu:") #gaining input from the user on option they would like 
        
    if selection == '1': #if selection is one the Binary counter program runs 
            
            newnum = ' ';
            for i in range(32):
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
                sleep(.2) # stay on 1 sec

                if digitFour == '1' :
                    GPIO.output(11, GPIO.HIGH) # LED on
                else :
                    GPIO.output(11, GPIO.LOW) # LED off
                sleep(.2) # stay on 1 sec

                if digitThree == '1' :
                    GPIO.output(13, GPIO.HIGH) # LED on
                else :
                    GPIO.output(13, GPIO.LOW) # LED off
                sleep(.2) # stay on 1 sec

                if digitTwo == '1' :
                    GPIO.output(15, GPIO.HIGH) # LED on
                else :
                    GPIO.output(15, GPIO.LOW) # LED off
                sleep(.2) # stay on 1 sec 

                if digitOne == '1' :
                    GPIO.output(16, GPIO.HIGH) # LED on
                else :
                    GPIO.output(16, GPIO.LOW) # LED off
                sleep(.2) # stay on 1 sec 
                
                GPIO.output(18, GPIO.LOW) # LED off
                GPIO.output(11, GPIO.LOW) # LED off
                GPIO.output(13, GPIO.LOW) # LED off
                GPIO.output(15, GPIO.LOW) # LED off
                GPIO.output(16, GPIO.LOW) # LED off
                
    if selection == '2' :
              
                GPIO.output(18, GPIO.HIGH) # LED on
                sleep(.5)
                GPIO.output(18, GPIO.LOW) # LED off

                GPIO.output(11, GPIO.HIGH) # LED on
                sleep(.5)
                GPIO.output(11, GPIO.LOW) # LED off

                GPIO.output(13, GPIO.HIGH) # LED on
                sleep(.5)
                GPIO.output(13, GPIO.LOW) # LED off

                GPIO.output(15, GPIO.HIGH) # LED on
                sleep(.5)
                GPIO.output(15, GPIO.LOW) # LED off

                GPIO.output(16, GPIO.HIGH) # LED on
                sleep(.5)
                GPIO.output(16, GPIO.LOW) # LED off
              
              
    if selection == '3' :
              
                GPIO.output(16, GPIO.HIGH) # LED on
                sleep(.5)
                GPIO.output(16, GPIO.LOW) # LED off

                GPIO.output(15, GPIO.HIGH) # LED on
                sleep(.5)
                GPIO.output(15, GPIO.LOW) # LED off

                GPIO.output(13, GPIO.HIGH) # LED on
                sleep(.5)
                GPIO.output(13, GPIO.LOW) # LED off

                GPIO.output(11, GPIO.HIGH) # LED on
                sleep(.5)
                GPIO.output(11, GPIO.LOW) # LED off

                GPIO.output(18, GPIO.HIGH) # LED on
                sleep(.5)
                GPIO.output(18, GPIO.LOW) # LED off

              
    if selection == '4' :
              while True: 
    
                GPIO.output(18, GPIO.HIGH) # LED 	on
                sleep(.5)
                GPIO.output(18, GPIO.LOW) # LED off

                GPIO.output(11, GPIO.HIGH) # LED on
                sleep(.5)
                GPIO.output(11, GPIO.LOW) # LED off

                GPIO.output(13, GPIO.HIGH) # LED on
                sleep(.5)
                GPIO.output(13, GPIO.LOW) # LED off

                GPIO.output(15, GPIO.HIGH) # LED on
                sleep(.5)
                GPIO.output(15, GPIO.LOW) # LED off

                GPIO.output(16, GPIO.HIGH) # LED on
                sleep(.5)
                GPIO.output(16, GPIO.LOW) # LED off

                GPIO.output(15, GPIO.HIGH) # LED on
                sleep(.5)
                GPIO.output(15, GPIO.LOW) # LED off

                GPIO.output(13, GPIO.HIGH) # LED on
                sleep(.5)
                GPIO.output(13, GPIO.LOW) # LED off

                GPIO.output(11, GPIO.HIGH) # LED on
                sleep(.5)
                GPIO.output(11, GPIO.LOW) # LED off

                GPIO.output(18, GPIO.HIGH) # LED on
                sleep(.5)
                GPIO.output(18, GPIO.LOW) # LED off

              
    if selection == '5' :
              
              while True :
    
                number = input("Enter a number between 0 and 31:")

                if number in range(31) : 

                    newnum = "{0:05b}".format(number)
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
                        sleep(1) # stay on 1 sec

                    if digitFour == '1' :
                        GPIO.output(11, GPIO.HIGH) # LED on
                    else :
                        GPIO.output(11, GPIO.LOW) # LED off
                        sleep(1) # stay on 1 sec

                    if digitThree == '1' :
                        GPIO.output(13, GPIO.HIGH) # LED on
                    else :
                        GPIO.output(13, GPIO.LOW) # LED off
                        sleep(1) # stay on 1 sec

                    if digitTwo == '1' :
                        GPIO.output(15, GPIO.HIGH) # LED on
                    else :
                        GPIO.output(15, GPIO.LOW) # LED off
                        sleep(1) # stay on 1 sec 

                    if digitOne == '1' :
                        GPIO.output(16, GPIO.HIGH) # LED on
                    else :
                        GPIO.output(16, GPIO.LOW) # LED off
                        sleep(1) # stay on 1 sec 
                        
                    GPIO.output(18, GPIO.LOW) # LED off
                    GPIO.output(11, GPIO.LOW) # LED off
                    GPIO.output(13, GPIO.LOW) # LED off
                    GPIO.output(15, GPIO.LOW) # LED off
                    GPIO.output(16, GPIO.LOW) # LED off

                else:
                    
                    for i in range(5) :
                        GPIO.output(18, GPIO.HIGH) # LED on
                        GPIO.output(11, GPIO.HIGH) # LED on
                        GPIO.output(13, GPIO.HIGH) # LED on
                        GPIO.output(15, GPIO.HIGH) # LED on
                        GPIO.output(16, GPIO.HIGH) # LED on
                        sleep(.5)
                        GPIO.output(18, GPIO.LOW) # LED off
                        GPIO.output(11, GPIO.LOW) # LED off
                        GPIO.output(13, GPIO.LOW) # LED off
                        GPIO.output(15, GPIO.LOW) # LED off
                        GPIO.output(16, GPIO.LOW) # LED off
                        sleep(.5)
                    
                    
                    number = input("Please enter a new number between 0 and 31:")        
                    

                        
