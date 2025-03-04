# run with "nohup python peper.py &"

import os
import sys
from time import sleep
from datetime import datetime as dt
import RPi.GPIO as GPIO

# pin to control the relay that controls on the lights
relay_pin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)
GPIO.output(relay_pin, 1)

photo_interval = 90 # seconds, can obviously be made variable

def take_photo(fname, shutterspeed):

    # set the shutterspeed (step, shutterspeed_value of something allows actual shuttertime)
    os.system('gphoto2 --set-config-index /main/capturesettings/shutterspeed=' + str(shutterspeed))
    # turn on the lights
    GPIO.output(relay_pin, 1)
    # wait half a second
    sleep(.5)
    # take the photo and save it as "fname"
    os.system('gphoto2 --capture-image-and-download --filename \'' + fname + '\'')
    # wait and turn off the lights
    sleep(.5)
    GPIO.output(relay_pin, 0)

if __name__ == "__main__":
    projname = 'yourProjectName_folder'
    counter = 1
    shutterchoice_day = 14 # shutterspeed step during the day (can also be made variable)

    try:
        while True:
            # filename will have a datestamp and extention (raw in this case)
            fname = projname + "/" + dt.now().strftime("%m_%d") + "/" + projname + dt.now().strftime("_%y%m%d_%H-%M-%S") + ".cr2"
            take_photo(fname, shutterchoice_day)
            counter += 1
            sleep(photo_interval)

    except KeyboardInterrupt:
        pass
    GPIO.cleanup()
