"""
File: BeeperRow.py
Name:
-------------------------
This program makes Karel fill up
Street 1 with beepers
(This program should be world insensitive)
"""

from karel.stanfordkarel import *

"""
<Nested if>
連鎖條件(取交集)
"""


def main():
    if front_is_clear():
        if on_beeper():
            pick_beeper()
            move()


"""
<2 if in a row>
不倫如何都會跑到if
"""


    if front_is_clear():
        move()
    if on_beeper():
        pick_beeper()
















####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)