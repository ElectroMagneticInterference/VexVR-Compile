
#=+=+=+=+=+==+=+=+=+= Info +=+=+=+=+==+=+=+=+=+=#
#                                               #
# 	Project:      Draw a CASTLE!                #
#	Author:       ElectroMagnetic Interference  #
#	Created:      2/2/21                        #
#	Description:                                #
#       A Solution to the Draw a House          #
#       challange using Universal Threading     #
#                                               #
#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=#

from vexcode import *

def Parapets(e,x:float,y:float,n:int):
    for i in range(n):
        x += 30
        e.move([x,y])
        y -= 30
        e.move([x,y])
        x += 30
        e.move([x,y])
        y += 30
        e.move([x,y])
    return x,y


def tower(e,x:float):
    e.move([x,650])
    y=650
    x -= 20
    e.move([x,y])
    y += 100
    e.move([x,y])
    x,y = Parapets(e,x,y,4)
    x += 20
    e.move([x,y])
    y -= 100
    e.move([x,y])
    x-=20
    e.move([x,y])
    return x,y

def main(e):
    e.move([-700,-700])
    e.pen(DOWN)

    e.pen(DOWN,BLACK)
    x,y = tower(e,-700)
    e.move([x,150])
    x,y = Parapets(e,x,150,7)
    x +=30
    e.move([x,y])
    y -=30
    e.move([x,y],[x+60,y],[x+60,y+30])
    y +=30
    x +=60
    x,y = Parapets(e,x,y,7)
    e.move([x+30,y])
    x,y = tower(e,x+30)
    e.move([x,-700],[-700,-700])

    e.move([-150,-700])
    x,y = -150,-700

    for i in range(7):
        e.move([x,y+20],[-x,y+20],[-x,y+40],[x,y+40])
        y += 40

    e.move([x,-400],[150,-400])
    e.polygon(e,LEFT,360,300,0,180)

    e.pen(UP)
    e.move([-900,-900])

vex_start(main(e))