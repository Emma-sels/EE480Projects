import RPi.GPIO as GPIO #importing the RPi GPIO library
from time import sleep #function to add in delay later in code

GPIO.setmode(GPIO.BOARD) #physical pin numbers
GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW) #pin 5 (GPIO3) as an output that starts off
GPIO.setup(7, GPIO.OUT, initial=GPIO.LOW) #pin 7 (GPIO4) as an output that starts off
GPIO.setup(11, GPIO.OUT, initial=GPIO.LOW) #pin 18 (GPIO27) as an output that starts off
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW) #pin 11 (GPIO17) as an output that starts off
GPIO.setup(15, GPIO.OUT, initial=GPIO.LOW) #pin 13 (GPIO27) as an output that starts off
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW) #pin 15 (GPIO22) as an output that starts off
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW) #pin 16 (GPIO23) as an output that starts off
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW) #pin 22 (GPIO25) as an output that starts off
GPIO.setup(29, GPIO.OUT, initial=GPIO.LOW) #pin 16 (GPIO23) as an output that starts off
GPIO.setup(31, GPIO.OUT, initial=GPIO.LOW) #pin 16 (GPIO23) as an output that starts off
GPIO.setup(36, GPIO.OUT, initial=GPIO.LOW) #pin 16 (GPIO23) as an output that starts off
GPIO.setup(37, GPIO.OUT, initial=GPIO.LOW) #pin 16 (GPIO23) as an output that starts off


# creating a menu to present to the user for options 
menu = {}
menu['1']="Majority Function"
menu['2']="Minority Function"
menu['3']="Comparitor Function"

while True: # continuously prompts user for a response until program is terminated 
    options = menu.keys() #options based off user keys 
    options.sort()
    for entry in options: # for loop to print off the menu for user to see 
        print entry, menu[entry]
    
    selection=raw_input("Enter your choice (1-3):") #gaining input from the user on option they would like 
        
    if selection == '1': #if selection is one the Majority function program runs 
            
            MAJ_First = input("Enter either a 0 or a 1:")
            MAJ_Second = input("Enter either a 0 or a 1:")
            MAJ_Third = input("Enter either a 0 or a 1:")
            
            if MAJ_First == '1' :
                GPIO.output(37, GPIO.HIGH) # LED on
            else :
                GPIO.output(37, GPIO.LOW) # LED off
                
            if MAJ_Second == '1' :
                GPIO.output(5, GPIO.HIGH) # LED on
            else :
                GPIO.output(5, GPIO.LOW) # LED off
                
            if MAJ_Third == '1' :
                GPIO.output(7, GPIO.HIGH) # LED on
            else :
                GPIO.output(7, GPIO.LOW) # LED off
            
        
                
    if selection == '2' : # program to sweep through LEDs right to left 
              
            MIN_First = input("Enter either a 0 or a 1:")
            MIN_Second = input("Enter either a 0 or a 1:")
            MIN_Third = input("Enter either a 0 or a 1:")
            
            if MIN_First == '1' :
                GPIO.output(11, GPIO.HIGH) # LED on
            else :
                GPIO.output(11, GPIO.LOW) # LED off
                
            if MIN_Second == '1' :
                GPIO.output(13, GPIO.HIGH) # LED on
            else :
                GPIO.output(13, GPIO.LOW) # LED off
                
            if MIN_Third == '1' :
                GPIO.output(15, GPIO.HIGH) # LED on
            else :
                GPIO.output(15, GPIO.LOW) # LED off
              
              
    if selection == '3' : # Comparator Circuit
              
            First = input("Enter either a 0 or a 1:")
            Second = input("Enter either a 0 or a 1:")
            Third = input("Enter either a 0 or a 1:")
            Fourth = input("Enter either a 0 or a 1:")
            FIFTH = input("Enter either a 0 or a 1:")
            SIXTH = input("Enter either a 0 or a 1:")
            
            if First == '1' :
                GPIO.output(16, GPIO.HIGH) # LED on
            else :
                GPIO.output(16, GPIO.LOW) # LED off
                
            if Second == '1' :
                GPIO.output(18, GPIO.HIGH) # LED on
            else :
                GPIO.output(18, GPIO.LOW) # LED off
                
            if Sixth == '1' :
                GPIO.output(22, GPIO.HIGH) # LED on
            else :
                GPIO.output(22, GPIO.LOW) # LED off
                
            if Third == '1' :
                GPIO.output(29, GPIO.HIGH) # LED on
            else :
                GPIO.output(29, GPIO.LOW) # LED off
            
            if Fourth == '1' :
                GPIO.output(31, GPIO.HIGH) # LED on
            else :
                GPIO.output(31, GPIO.LOW) # LED off
                
            if Fifth == '1' :
                GPIO.output(36, GPIO.HIGH) # LED on
            else :
                GPIO.output(36, GPIO.LOW) # LED off
                