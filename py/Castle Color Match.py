#=+=+=+=+=+==+=+=+=+= Info +=+=+=+=+==+=+=+=+=+=#
#                                               #
# 	Project:      Castle Color Match            #
#	Author:       ElectroMagnetic Interference  #
#	Created:      1/12/21                       #
#	Description:                                #
#       A Universal Threading Usage for CCM     #
#                                               #
#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=#
from vexcode import *

async def green(e,target,target2="return"):
    e.pickup(target,target2)
    e.drop([ 700, -700],"return")

async def blue(e,target,target2="return"):
    e.pickup(target,target2)
    e.drop([ -700, -700],"return")

async def red(e,target,target2="return"):
    e.pickup(target,target2)
    e.drop([ 0, -700],"return")

#Asyncio is weird, this one doesn't need async ¯\_(ツ)_/¯
def final(e, target,stop=False):
    e.pickup(target,"return")
    wait(1,MSEC)
    e.move([-250,-450],[-900,-250],[-900,900])
    wait(1,MSEC)
    if not stop:
        e.drop([-500,900],"return")
        wait(1,MSEC)
        e.move([-900,-250],[-250,-450], [0,-200])
        wait(1,MSEC)
    else:
        e.drop([-500,900])

def main(e):
    e.init()
    e.move([140,-100])
    e.pen(DOWN, GREEN)
    e.print("Starting Greens!\n", GREEN)
    await green(e,[ 300, -100],[-140, -100])
    await green(e,[ 500, -100])
    await green(e,[-300,  450])
    e.print("Finshed Greens!\n\n", GREEN)
    e.pen(BLUE)
    e.sync()
    e.print("Starting Blues!\n", BLUE)
    await blue(e,[-300, -100],[140, -100])
    await blue(e,[-500, -100])
    await blue(e,[ 500,  100])
    e.print("Finshed Blues!\n\n", BLUE)
    e.pen(RED)
    e.sync()
    e.print("Starting Reds!\n", RED)
    await red(e,[-450, 100],[0, -200])
    await red(e,[-450, 250])
    await red(e,[ 300,  450])
    e.print("Finished Reds!\n\n", RED)
    e.pen(BLACK)
    e.sync()
    e.move([0,-200])
    e.print("Hiding the Rest!\n")
    #like I was saying before, this should need await, but whatever ¯\_(ツ)_/¯
    final(e, [-450,450])
    final(e, [450,450])
    final(e, [450,250], stop=True)
    e.print("Finished!\n")
