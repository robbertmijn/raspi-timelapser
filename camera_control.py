# camera_control.py
# import gphoto2 as gp
import os
from time import sleep

def take_photo(fname, shutterspeed):

    # set the shutterspeed (step, shutterspeed_value of something allows actual shuttertime)
    os.system('gphoto2 --set-config-index /main/capturesettings/shutterspeed=' + str(shutterspeed))

    # wait half a second
    sleep(.5)

    # take the photo and save it as "fname"
    os.system('gphoto2 --capture-image-and-download --filename \'' + fname + '\'')