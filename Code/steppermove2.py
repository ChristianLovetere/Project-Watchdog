#driver code for Project Watchdog. Contains active low push buttons for manual movement,
#active high inputs from the ESP8266 (WiFi microcontroller) to control via buttons on a web page.
#the DRV8825 library is used to control these Nema 17 stepper motors and is relatively straight-forward.
#the lines that allow the RPi to control the neopixel LEDs are commented out and the arduino does this
#work instead. For a possible optimization, try to get the neopixel code working on the RPi so we don't
#need the arduino at all. Please consult the readme file for more information.

import RPi.GPIO as GPIO
import time
from DRV8825 import DRV8825
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP) #button up
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP) #button left
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP) #button down
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP) #button right
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) #button fire
GPIO.setup(10, GPIO.OUT)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #wifi up
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #wifi down
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #wifi right
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #wifi left
#import board
#import neopixel
#pixels = neopixel.NeoPixel(board.D10, 60)

Motor1 = DRV8825(dir_pin=13, step_pin=19, enable_pin=12, mode_pins=(16, 17, 20)) #Motor1 = horizontal movement
Motor2 = DRV8825(dir_pin=24, step_pin=18, enable_pin=4, mode_pins=(21, 22, 27)) #Motor2 = vertical movement
Motor1.SetMicroStep('softward','fullstep') #softward means we use code to move the motors
Motor2.SetMicroStep('softward' ,'fullstep')

        
def demo(): #empty function that is called when the red 'fire' button is pressed.
    print("TBA")        

def main():
    try:
        #pixels.fill((234, 102,35))
        while True:
            if GPIO.input(2) == 0: #button up
                Motor2.TurnStep(Dir='forward', steps=1, stepdelay = 0.005)
                time.sleep(0.01)
                print("Hello")

            elif GPIO.input(14) == 0: #button down
                Motor2.TurnStep(Dir='backward', steps=1, stepdelay = 0.005)
                time.sleep(0.01)

            elif GPIO.input(6) == 1: #wifi up
                Motor2.TurnStep(Dir='forward', steps=1, stepdelay = 0.005)    
                time.sleep(0.01)
                print("Hello")

            elif GPIO.input(5) == 1: #wifi down
                Motor2.TurnStep(Dir='backward', steps=1, stepdelay = 0.005)      
                time.sleep(0.01)

            if GPIO.input(3) == 0: #button left
                Motor1.TurnStep(Dir='backward', steps=1, stepdelay = 0.005)
                time.sleep(0.01)

            elif GPIO.input(15) == 0: #button right
                Motor1.TurnStep(Dir='forward', steps=1, stepdelay = 0.005)
                time.sleep(0.01)

            elif GPIO.input(26) == 1: #wifi left
                Motor1.TurnStep(Dir='forward', steps=1, stepdelay = 0.005)
                time.sleep(0.01)

            elif GPIO.input(25) == 1: #wifi right
                Motor1.TurnStep(Dir='backward', steps=1, stepdelay = 0.005)
                time.sleep(0.01)

            if GPIO.input(23) == 0: #shoot
                demo()
                time.sleep(0.01)

    except Exception as error: #if an error occurs, stop both motors
        Motor1.Stop()
        Motor2.Stop()
        return("error: ",error)
    except KeyboardInterrupt: #if there is a keyboard interrupt, stop both motors
        print("\nMotor Stopped")
        Motor1.stop()
        Motor2.stop()
        GPIO.cleanup()
        exit()

main()
