#=+=+=+=+=+==+=+=+=+= Info +=+=+=+=+==+=+=+=+=+=#
#                                               #
# 	Project:      Coorindate Numbers            #
#	Author:       ElectroMagnetic Interference  #
#	Created:      1/12/21                       #
#	Description:                                #
#       A Solution to Coorinate Numbers using   #
#       Universal Threading                     #
#                                               #
#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=#
from vexcode import *

def main(e):
    e.init()
    # 22
    e.pen(DOWN)
    e.print("Block 22\n", BLACK)
    e.move([-700,-500])
    # 38
    e.pen(GREEN)
    e.print("Block 38\n", GREEN)
    e.move([500,-300])
    # 64
    e.pen(BLUE)
    e.print("Block 64\n", BLUE)
    e.move([-300,300])
    # 85
    e.pen(RED)
    e.print("Block 85\n", RED)
    e.move([-100,700])

vex_start(main(e))