#!/usr/bin/env python

import os
import socket
from time import sleep
import RPi.GPIO as GPIO

PIN = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN)

######### Configuracion Socket #######
PORT = 1
IP = '10.1.3.30'

TUCAN = 'X0801'   #TUCAN
CARPINTERO = 'X0802'   #CARPINTERO
OROPENDULA = 'X0803'   #OROPENDULA
SARAHUATO = 'X0804'   #SARAHUATO
RANA = 'X0805'   #TARANTULA
MURCIELAGO = 'X0806'   #MURCIELAGO

######################################
cliente = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

def mandar_luces(m):
    try:
        cliente.connect((IP,PORT))
        cliente.send(m)
        print('enviado')
    except Exception as e:
        print e
        pass

while True:
    if (GPIO.input(PIN) != False):
	print('RANA')
        os.system('aplay /home/pi/audios/rana.wav')
        mandar_luces(RANA)
    sleep(0.1)
cliente.close()
