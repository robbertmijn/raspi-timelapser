installeren headless rasbian
ssh
samba fil share
wifi setup
gphoto2


blank raspbian van raspberrypi.org

add ssh file to boot sd

clear ssh keys saved on mac:
> ssh-keygen -R {RPi-IP-Address}

ssh into pi:
> ssh pi@192.168.1.###
pw: #####

change pw
> passwd

#####

===============
build gphoto2
https://pimylifeup.com/raspberry-pi-dslr-camera-control/

1:
sudo apt-get update
sudo apt-get upgrade

2:
sudo apt-get install git make autoconf libltdl-dev libusb-dev libexif-dev libpopt-dev libxml2-dev libjpeg-dev libgd-dev gettext autopoint

3:
git clone https://github.com/gphoto/libgphoto2.git


4:
cd ~/libgphoto2
autoreconf --install --symlink
./configure
make
sudo make install

5:
cd ~
git clone https://github.com/gphoto/gphoto2.git

6:
cd ~/gphoto2
autoreconf --install --symlink
./configure
make
sudo make install


7:
sudo nano /etc/ld.so.conf.d/libc.conf

add this text and save conf if not already there:
# libc default configuration
/usr/local/lib

8:
sudo ldconfig

9:
/usr/local/lib/libgphoto2/print-camera-list udev-rules version 201 group plugdev mode 0660 | sudo tee /etc/udev/rules.d/90-libgphoto2.rules

10:
/usr/local/lib/libgphoto2/print-camera-list hwdb | sudo tee /etc/udev/hwdb.d/20-gphoto.hwdb

11:
gphoto2 --version

=====================
setup wifi
https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md

1:
sudo raspi-config
OR
sudo nano etc/wpa_supplicant/wpa_supplicant.conf

====================
setup fileshare. netatalk kreeg ik niet aan de praat. dus samba:

1:
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install samba samba-common-bin

2:
sudo nano /etc/samba/smb.conf

add:
[global]
netbios name = Pi
server string = The Pi File Center
workgroup = WORKGROUP

[HOMEPI]
path = /home/pi
comment = No comment
writeable=Yes
create mask=0777
directory mask=0777
public=no

3:
sudo smbpasswd -a pi

4:
sudo service smbd restart
============================
for shell commands and cron jobs
https://pimylifeup.com/raspberry-pi-time-lapse/

============================
pip
PIP for python2 - sudo apt-get install python-pip
PIP for python3 - sudo apt-get install python3-pip

============================
GPIO

wit -> GPIO4
rood -> 5v+
bruin -> ground
oranje -> GPIO17
