"""
File: DoubleBeepers.py
Name:
-------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will double the beepers
    """
    move()
    while on_beeper():
        pick_beeper()
        move()
        put_beeper()
        put_beeper()
        turn_around()
        move()
        turn_around()


    move()
    turn_around()

    while on_beeper():
        pick_beeper()
        move()
        put_beeper()
        turn_around()
        move()
        turn_around()



def turn_around():
    turn_left()
    turn_left()




















####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)