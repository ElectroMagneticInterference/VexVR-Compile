#=+=+=+=+=+==+=+=+=+= Info +=+=+=+=+==+=+=+=+=+=#
#                                               #
# 	Project:      Universal threading           #
#	Author:       ElectroMagnetic Interference  #
#	Created:      1/12/21                       #
#	Description:                                #
#       A Universal Solution to VEXVR,          #
#       utilizing Threading for optimal speed   #
#                                               #
#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=#
from vexcode import *

def main(e):
    e.init()

    e.print("You can print stuff!\nAnd Change the color!\n\n", GREEN)
    # move to specified coordinates!
    e.move([30,77], [-777, 324], [900, -900])

    # And much, much more!

vex_start(main(e))