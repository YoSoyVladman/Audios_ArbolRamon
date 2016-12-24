#!/usr/bin/env python

import os
import socket
from time import sleep

PORT = 1
IP = "10.1.3.30"

TUCAN = 'X0801'   #TUCAN
CARPINTERO = 'X0802'   #CARPINTERO
OROPENDULA = 'X0803'   #OROPENDULA
SARAHUATO = 'X0804'   #SARAHUATO
TARANTULA = 'X0805'   #TARANTULA
MURCIELAGO = 'X0806'   #MURCIELAGO
"""
"""
cliente = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

def mandar_luces(m):
    try:
        cliente.connect((IP,PORT))
        cliente.send(m)
        """
        respuesta = cliente.recv(1024)
        print(respuesta)
        """

        print('enviado' + m )
    except Exception as e:
        print e
        pass

sleep(8)
mandar_luces(TUCAN)
sleep(5)
mandar_luces(OROPENDULA)
sleep(5)

mandar_luces(SARAHUATO)
sleep(5)

mandar_luces(CARPINTERO)
sleep(5)

mandar_luces(TARANTULA)
sleep(5)

mandar_luces(MURCIELAGO)
sleep(5)

cliente.close()
