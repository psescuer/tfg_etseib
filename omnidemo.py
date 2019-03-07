#!/usr/bin/env python3
from ev3dev.ev3 import *
import math
from time import time, sleep
import os
os.system('setfont Lat15-TerminusBold14')

def check(condition, message1, message2):
        if not condition:
                Sound.beep().wait()
                print(message2)
                sleep(5)
                quit()
        else:
                print(message1)
                sleep(0.1)
                Sound.speak(message1).wait()

class omnidemo:
        def __init__(self):
                self.m1 = LargeMotor('outA')
                self.m2 = LargeMotor('outC')
                self.m3 = LargeMotor('outB')
                motors=[self.m1, self.m2, self.m3]

                for m in motors:
                        m.reset()
                        m.position= 0
                        m.stop_action= 'brake'
        
        def rc_loop(self):
        """
        Enter the remote control loop. RC buttons on channel 1 control the
        robot movement, channel 2 is for shooting things.
        The loop ends when the touch sensor is pressed.
        """

                def roll(motor, led_group, speed):
            """
            Generate remote control event handler. It rolls given motor into
            given direction (1 for forward, -1 for backward). When motor rolls
            forward, the given led group flashes green, when backward -- red.
            When motor stops, the leds are turned off.
            The on_press function has signature required by RemoteControl
            class.  It takes boolean state parameter; True when button is
            pressed, False otherwise.
            """
                        def on_press(state):
                                if state:
                                # Roll when button is pressed
                                        motor.run_forever(speed_sp=speed)
                                        ev3.Leds.set_color(led_group,
                                        ev3.Leds.GREEN if speed > 0 else ev3.Leds.RED)
                                else:
                    # Stop otherwise
                                        motor.stop()
                                        ev3.Leds.set_color(led_group, ev3.Leds.BLACK)

                        return on_press

                rc1 = ev3.RemoteControl(self.ir, 1)
                rc1.on_red_up    = roll(self.lm, ev3.Leds.LEFT,   900)
                rc1.on_red_down  = roll(self.lm, ev3.Leds.LEFT,  -900)
                rc1.on_blue_up   = roll(self.rm, ev3.Leds.RIGHT,  900)
                rc1.on_blue_down = roll(self.rm, ev3.Leds.RIGHT, -900)

if __name__ == '__main__':
        Marvin = omnidemo()
        Marvin.rc_loop()


