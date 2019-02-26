#!/usr/bin/python

'''
SETUP:

    -   -->     GND     -->     PIN6
    +   -->     5V      -->     PIN4
    S   -->     GPIO21  -->     PIN40

'''

import RPi.GPIO as GPIO
import subprocess
import time
import sys

sensor = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor, GPIO.IN)

on = 0
off = 0
flag = 0
while flag == 0:
    i=GPIO.input(sensor)
    if i == 0:
        if flag == 1:
            off = time.time()
            diff = off - on
            print 'time: ' + str(diff%60) + ' sec'
            print ''
            flag = 0
            print "No intruders", i
        time.sleep(0.1)
    elif i == 1:
        if flag == 0:
            print "Intruder detected", i
            on = time.time()
            flag = 1
            subprocess.call(['sudo','chrt','-i','98','python','camera.py','frame.jpg'])
            subprocess.call(['sudo', './chrt', '-i','98', './facedetect', 'frame.jpg'])
        time.sleep(0.1)
        
