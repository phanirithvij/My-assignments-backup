# -*- coding: utf-8 -*-
import sys
import numpy as np
from time import sleep
import datetime
from drawutils import clear
from drawutils import Canvas, COLORS
from config import INITIALPOS, DIMENS, get_input, TIMELIMIT

def main():
    game = Canvas(DIMENS['Canvas'][0],DIMENS['Canvas'][1])

    start_t = datetime.datetime.now()
    time_now = start_t

    while ((datetime.datetime.now() - start_t) <= datetime.timedelta(seconds=TIMELIMIT)):
        input_ = get_input()
        game.update_frame()
        game.rerender()
        timeleft = (TIMELIMIT - (datetime.datetime.now() - start_t).seconds)

        print("""print 'q' to quit the game {} {}""".format(input_,timeleft))

        if input_ == 'q':
            exit(0)

    exit(0)
        

if __name__ == '__main__':
#    for i in emojis:
#        zeta = ''
#        for k,v in colors.items():
#            zeta += v+" "+i
#        print(zeta)
    main()
