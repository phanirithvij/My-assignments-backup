# -*- coding: utf-8 -*-

'''
Contains maps, player settings etc
'''

import numpy as np
import sys
import termios
import contextlib

PLAYER = {
    'lives' : 3,
}

DIMENS = {
    "Canvas" : (150,46),
}

X_UP,Y_UP = 2,3

INITIALPOS = {
    "Player": (
        DIMENS['Canvas'][0]/6,
        DIMENS['Canvas'][1]/2
    )
}

TIMELIMIT = 360

LEVELS = np.array([0,1,2,3])


MAPS = [
    {
        'NO_GROUND' : np.array([])
    },
    {
        'NO_GROUND' : np.array([])
    },
    {
        'NO_GROUND' : np.array([])
    }
]

class Level():
    def __init__(self, lvl=1):
        self._map = np.empty((45,100))
        self.level = lvl
        self._mapgen = False

    def get_map(self):
        if not self._mapgen:
            self.generate_map()
        return self._map

    def generate_map(self):
        mapdict = MAPS[self.level]
        return mapdict

def get_level(lvl):
    if lvl in LEVELS:
        return Level(lvl)
    return

@contextlib.contextmanager
def raw_mode(file):
    old_attrs = termios.tcgetattr(file.fileno())
    new_attrs = old_attrs[:]
    new_attrs[3] = new_attrs[3] & ~(termios.ECHO | termios.ICANON)
    try:
        termios.tcsetattr(file.fileno(), termios.TCSADRAIN, new_attrs)
        yield
    finally:
        termios.tcsetattr(file.fileno(), termios.TCSADRAIN, old_attrs)


def read_input():
    with raw_mode(sys.stdin):
        try:
            extradetails = []
            ch = sys.stdin.read(1)
            #if not ch or ch == chr(4):
            #    extradetails = ["not ch or chr(4)"]
            #if ch == "a":
            #    extradetails = ["left function"]
            #if  ch == "w" :
            #    extradetails = ["jump function"]
            #if ch == " ":
            #    extradetails = ["high jump function"]
            #if ch == "d":
            #    extradetails = ["right function"]
            #if ch == "s":
           #     extradetails = ["crouch function"]
           # if ch == "p":
            #    extradetails = ["pause/play function"]
            #if ch == "z" or ch == "x" or ch == "c":
            #    extradetails = ["shoot function"]
            #if ch == "r":
            #    extradetails = ["restart current level function"]
            #if ch == "h":
            #    extradetails = [
            #        "How to play",
            #        "\t p to pause/play",
            ##        "\t a,d keys to move",
             #       "\t h key to show this message",
             #       "\t w or space keys to jump",
             #       "\t z,x,c keys to shoot when powered up",
             #       "\t r key to restart level",
             #       "\t s key to crouch",
             #   ]
            return (ch,extradetails)
            #print("{} is pressed and key is {}".format(ch,ord(ch)))
            #print('%02x' % ord(ch))
        except (KeyboardInterrupt, EOFError):
            pass

class _Getch:

    def __init__(self):
        self.impl = _GetchUnix()

    def __call__(self):
        return self.impl()


class _GetchUnix:

    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


_getch = _Getch()

class AlarmException(Exception):
    pass

def alarmHandler(signum, frame):
    raise AlarmException

def get_input(timeout=1):
    import signal
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    try:
        text = _getch()
        signal.alarm(0)
        return text
    except AlarmException:
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''