# -*- coding: utf-8 -*-
import numpy as np

EMPTY = AIR = """\
    
    \
"""

CLOUD = """\
                _                                    
              (`  ).                   _             
             (     ).              .:(`  )`.         
            _(       '`.          :(   .    )        
        .=(`(      .   )          `.  (    ) )       
       ((    (..__.:'-'             ` _`  ) )        
       `(       ) )                    (   )  ._     
         ` __.:'   )                    `-'.-(`  )   
      ( )       --'                       :(      )) 
     (_.'          .')                    `(    )  ))
                  (_  )                     ` __.:'  \
"""

GROUND = """\
⬛⬛⬛
⬛⬛⬛\
"""

GROUND_ALT = """\
☐☐☐☐☐☐☐☐☐
☐☐☐☐☐☐☐☐☐\
"""

BRICK = """\
░▒▓░
░▓▒▓\
"""

WALL = """\
🔲\
"""

MARIO_BABY = """\
m
m
m\
"""

MARIO_NORMAL = """\
MM
MM
MM
MM\
"""

MARIO_POWERED = """\
MP
MP
MP
MP\
"""

BULLET = "️❇️"


EVIL_MUSHROOM = """\
  👀 
|^^^^|
 \\/\\/\
"""

POWERUP_MUSHROOM  = """\
//_\\\\
|P P|
 |_| \
"""

ONEUP_MUSHROOM = """\
//_\\\\
|💖 💖|
 |_| \
"""

TURTLE = """\
"""

POWERUP_STAR = """\
_/\\_
\\👀 /
/--\\\
"""

# Safe text for no unicode errors

POWERUP_MUSHROOM_SAFE = POWERUP_MUSHROOM
ONEUP_MUSHROOM_SAFE = """\
//_\\\\
|1up|
 |_| \
"""
MARIO_BABY_SAFE = MARIO_BABY
MARIO_NORMAL_SAFE = MARIO_NORMAL
MARIO_POWERED_SAFE = MARIO_POWERED
EVIL_MUSHROOM_SAFE = """\
  MM  
|^^^^|
 \\/\\/ \
"""
POWERUP_STAR_SAFE =  """\
_/\\_
\\P /
/--\\\
"""
GROUND_SAFE = """\
|-|
|-|\
"""
GROUND_ALT_SAFE = GROUND_SAFE
WALL_SAFE = """\
=\
"""
EMPTY_SAFE = EMPTY
AIR_SAFE = AIR
CLOUD_SAFE = CLOUD
BRICK_SAFE = """\
[]\
"""

IMAGES = {
    "POWERUP_MUSHROOM" : POWERUP_MUSHROOM,
    "ONEUP_MUSHROOM" : ONEUP_MUSHROOM,
    "MARIO_BABY" : MARIO_BABY,
    "MARIO_NORMAL" : MARIO_NORMAL,
    "MARIO_POWERED" : MARIO_POWERED,
    "EVIL_MUSHROOM" : EVIL_MUSHROOM,
    "POWERUP_STAR" : POWERUP_STAR,
    "GROUND" : GROUND,
    "GROUND_ALT" : GROUND_ALT,
    "WALL" : WALL,
    "EMPTY": EMPTY,
    "AIR" : AIR,
    "CLOUD" : CLOUD,
    "BRICK" : BRICK,
}

SAFEIMAGES = {
    "POWERUP_MUSHROOM" : POWERUP_MUSHROOM_SAFE,
    "ONEUP_MUSHROOM" : ONEUP_MUSHROOM_SAFE,
    "MARIO_BABY" : MARIO_BABY_SAFE,
    "MARIO_NORMAL" : MARIO_NORMAL_SAFE,
    "MARIO_POWERED" : MARIO_POWERED_SAFE,
    "EVIL_MUSHROOM" : EVIL_MUSHROOM_SAFE,
    "POWERUP_STAR" : POWERUP_STAR_SAFE,
    "GROUND" : GROUND_SAFE,
    "GROUND_ALT" : GROUND_ALT_SAFE,
    "WALL" : WALL_SAFE,
    "EMPTY": EMPTY_SAFE,
    "AIR" : AIR_SAFE,
    "CLOUD" : CLOUD_SAFE,
    "BRICK" : BRICK_SAFE,
}

def get_dimens(string_image):
    '''
    Gives width and height of a string
    '''
    # y is no of lines
    lines = string_image.split('\n')
    y = len(lines)
    # x is length of longest string 
    lines.sort(key=len,reverse=True)
    x = len(lines[0])

    return (x,y)

def get_nparray(string_image):
    lines = string_image.split('\n')
    twod = [list(x) for x in lines]
    return np.array(twod)

if __name__ == "__main__":
    for name,img in IMAGES.items():
        print(name)
        print(img,end=' ')
        print(get_dimens(img))
        print(get_nparray(img))
    for name,img in SAFEIMAGES.items():
        print(name)
        print(img,end=' ')
        print(get_dimens(img))
        nparr = get_nparray(img)
        print(nparr)

    
    #for i in [1,2,4,7,8,9,*range(100,107),*range(90,97),*range(40,47),*range(30,37)]:
    #    print(i)
    #    print('\x1b[1;'+ str(i) +'m' + IMAGES['CLOUD'] + endcolor)
        #100-107,90-97,40-47,30-37,1,2,4,7,8,9