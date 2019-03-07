#!/usr/bin/env python3
from ev3dev.ev3 import *
import math
from time import time, sleep
import os
os.system('setfont Lat15-TerminusBold14')

Sound.speak('Hi!').wait()

print('checking...')
sleep(2)

m1 = LargeMotor('outA')
m2 = LargeMotor('outC')
m3 = LargeMotor('outB')

lcd = Screen()

def check(condition, message1, message2):
        if not condition:
                Sound.beep().wait()
                print(message2)
                sleep(5)
                quit()
        else:
                print(message1)
                sleep(0.5)
                #Sound.speak(message1).wait()


check(m1.connected, 'M1 checked!', 'M1 not connected')
check(m2.connected, 'M2 checked!', 'M2 not connected')
check(m3.connected, 'M3 checked!', 'M3 not connected')

print('ready!')

m1.stop_action = 'hold'
m2.stop_action = 'hold'
m3.stop_action = 'hold'


Sound.speak('I am ready').wait()

lcd.clear()
lcd.update()

sleep(2)

m3.run_to_rel_pos(position_sp= 1785, speed_sp = 250)
m2.run_to_rel_pos(position_sp= 1785, speed_sp = 250)
m1.run_to_rel_pos(position_sp= 1785, speed_sp = 250)
m3.wait_while('running')
m2.wait_while('running')
m1.wait_while('running')