# -*- coding: utf-8 -*-

import os, sys
import numpy as np
from colorama import Fore, Style, Back, init
from images import IMAGES, SAFEIMAGES

from sprites import Player
from config import get_level

init()

def clear():
    """
    clears the screen for re rendering the image(text)
    """
    sys.stdout.flush()
    sys.stdout.write(chr(27) + "[2J")

class Canvas():

    def __init__(self, n, m, level=1):

        self.width = n
        self.height = m
        self.dimen = (n, m)
        self._image = np.empty((m, n),dtype=str)
        self._image[:, :] = IMAGES['AIR']
        self.level = level
        self._storage = []
        self._player = Player
        self.map = get_level(lvl=level).get_map()
        self.rerender(extradetails=["\n\npress h for more help"])

    def rerender(self, extradetails=[]):
        '''
            Re renders board \
            i.e game along with \
            extra lines to \
            print at the bottom \
            like score and stuff.
        '''
        clear()
        for i in self._image:
            x = ''
            for j in i:
                x += str(j)
            print(x)
        for line in extradetails:
            print(line)
    
    def update_frame(self):
        '''#Handle all the movements'''
        pass

    def get_player(self):
        return self._player

    def controls(self, input_key):
        pass

COLORS = {
    'Black'            : '\x1b[0;30m',
    'Blue'             : '\x1b[0;34m',
    'Green'            : '\x1b[0;32m',
    'Cyan'             : '\x1b[0;36m',
    'Red'              : '\x1b[0;31m',
    'Purple'           : '\x1b[0;35m',
    'Brown'            : '\x1b[0;33m',
    'Gray'             : '\x1b[0;37m',
    'Dark Gray'        : '\x1b[1;30m',
    'Light Blue'       : '\x1b[1;34m',
    'Light Green'      : '\x1b[1;32m',
    'Light Cyan'       : '\x1b[1;36m',
    'Light Red'        : '\x1b[1;31m',
    'Light Purple'     : '\x1b[1;35m',
    'Yellow'           : '\x1b[1;33m',
    'White'            : '\x1b[1;37m',
}

endcolor = '\x1b[0m'


def printcolor(st, color):
    try:
        return COLORS[color] + st + endcolor
    except KeyError:
        return st


if __name__ == "__main__":
    cl = Canvas(45,150,1)

    print(cl.__dict__)
    cl.rerender(extradetails=["Press h for help"])

    print(Fore.LIGHTBLUE_EX + 'some lightblue text')
    print(Back.CYAN + 'and with a cyan background')
    print(Style.RESET_ALL)
