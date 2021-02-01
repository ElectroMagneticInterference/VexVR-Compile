
#=+=+=+=+=+==+=+=+=+= Info +=+=+=+=+==+=+=+=+=+=#
#                                               #
# 	Project:      Find Your Age                 #
#	Author:       ElectroMagnetic Interference  #
#	Created:      1/28/21                       #
#	Description:                                #
#       A Universal Solution to the "find your  #
#       age" task using Universal Threading     #
#                                               #
#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=#
from .vexcode import *

def num(e,num,col=BLACK):
    num = str(num - 1)

    if len(num) == 1:
        num = f"0{num}"

    x = (int(num[1]))*200-950
    y = int(num[0])*200-950

    e.move([x,y])

    e.pen(DOWN, col)

    e.move([x+100,y+100])

    e.pen(UP)

def age(e,year):
    num(e,year,GREEN)

    num(e,35 - year,BLACK)

def main(e):
    e.init()

    day = 1     #day
    month = 13  #month
    year = 97   #year
    #day (blue)
    num(e,day,BLUE)

    #month (red)
    num(e,month,RED)

    #year (green) and age in 2035 (black)
    age(e,year)

    e.move([0,0])

vex_start(main(e))