#! /usr/bin/env python3
import serial
import time
from . import EV3BT
EV3 = serial.Serial('/dev/rfcomm0')
left = 1
right = 2
forward = 3
back = 4

def setup(robot_config):
    pass
    return

def move(args):
    direction = args['button']['command']
    if direction == 'f':
        s = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'abc', forward)
        EV3.write(s)
#        time.sleep(sleeptime)
    if direction == 'b':
        s = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'abc', back)
        EV3.write(s)
 #       time.sleep(sleeptime)
    if direction == 'l':
        s = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'abc', left)
        EV3.write(s)
  #      time.sleep(sleeptime * rotatetimes)
    if direction == 'r':
        s = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'abc', right)
        EV3.write(s)
   #     time.sleep(sleeptime * rotatetimes)
