import numpy as np
import sys, os, time, datetime
from images import get_dimens
from config import INITIALPOS, PLAYER, X_UP, Y_UP

class Object():
    '''
    Every non-living thing \
    will be extending this class

    ground, \
    brick, \
    coinblock, \
    flowerblock, \
    mushrommblock, \
    wall, \
    cloud, \
    flagpole. \

    '''

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._image = np.chararray((x,y))
        self._color = ''
        self.can_die = False

    def dimens(self):
        return get_dimens(self._image)

class Person():
    '''
    Every living thing will inherit his class

    player, \
    evilmushroom, \
    turtle, \
    powerupstar, \
    bullet, \
    flag, \

    flyingturtle, \
    '''

    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._image = np.empty((x,y),dtype=str)
        self.can_die = True
        self.onscreen = False

    def dimens(self):
        return get_dimens(self._image)

    def move(self, new_x, new_y):
        self._x = new_x
        self._y = new_y
    
    def get_xy(self):
        return self._x,self._y

class Player(Person):

    def __init__(self, x=INITIALPOS['Player'][0], y=INITIALPOS['Player'][1]):
        super().__init__(int(x),int(y))
        self.lives = PLAYER['lives']
        # for mario self.state = ["s","b","p"] small or big or poweredup
        self.state = 's'
        self.onscreen = True
        self.alive = True

#    def move(self,x,y):
#        #change _x,_y array
#        pass

    def jump(self,height):
        #change _x,_y with a timer
        start_t = datetime.datetime.now()
        while(datetime.datetime.now()-start_t <= datetime.timedelta(seconds=1.2)):
            self._y += Y_UP
        del start_t
    
    def kill(self):
        #Do these before calling kill on player
        #play death sound
        #end game befor kill
        del self

    def __repr__(self):

        return "%s" % "Mario object"

if __name__ == "__main__":

    pla = Player()
    print(pla.__dict__)
    print(pla._x,pla._y)
    print(pla.move(22,230))
    print(pla._x,pla._y)


    for i in pla._image:
        x = ''
        for j in i:
            x += str(j)
        print(x)