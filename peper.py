# run with "nohup python peper.py &"

import os
# import glob
import time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.output(4, 1)



def take_photo(fname, shutterspeed):
    print("taking photo")
    os.system('gphoto2 --set-config /main/capturesettings/shutterspeed = ' + shutterspeed + '\'')
    os.system('gphoto2 --capture-image-and-download --filename \'' + filename + '\'')

if __name__ == '__main__':

    # counter = 1
    #
    # while 1:
    #     fname = projname + "_%05d" % counter
    #     take_photofname
    try:
        while True:
            GPIO.output(relay_pin, 0)
            sleep(5)
            GPIO.output(relay_pin, 1)
            sleep(5)
    except KeyboardInterrupt:
    	pass
    GPIO.cleanup()
