import math, time

x = 0
y = 0
angle = 0

def Start(x_coord, y_coord):
    global x, y
    x = x_coord
    y = y_coord
    print("def main():")

def Move(coordinates):
    for coordinate in coordinates:
        global x, y, angle
        xt = coordinate[0]
        yt = coordinate[1]
        xd = x - xt
        yd = y - yt

        if not xt:
            xt = 1
        
        if not yt:
            yt = 1

        if xd and yd:
            distance = math.hypot(abs(xd), abs(yd))

            Target_angle = math.atan(abs(yt)/abs(xt))

        elif xd:
            distance = xd
            Target_angle = 0
        elif yd:
            distance = yd
            Target_angle = 0
        else:
            print('\x1b[0;31;40m' + 'FAILED! \n' + '\x1b[0m' + 'The desination coodinates is the same as the bots location!')
            exit('The desination coodinates is the same as the bots location!')

        if yd > 0 and xd < 0:   #90°
            Target_angle += math.pi/2
        elif yd > 0 and xd > 0: #180°
            Target_angle += math.pi
        elif xd > 0 and yd < 0: #270°
            Target_angle += math.pi*1.5
        elif xd < 0 and not yd:    #90°
            Target_angle += math.pi/2
        elif yd < 0 and not xd:    #180°
            Target_angle += math.pi
        elif xd > 0 and not yd:    #270°
            Target_angle += math.pi*1.5

        if Target_angle - math.pi < angle < Target_angle + math.pi:
            direction = "FORWARD"

        else: 
            direction = "REVERSE"
            Target_angle -= math.pi

        print("    #from", x, ",", y ,"to", xt, ",", yt, "\n    drivetrain.turn_to_heading(",round(math.degrees(Target_angle)),",DEGREES)\n    drivetrain.drive_for(",direction,",",round(abs(distance)),",MM)")
        angle = Target_angle
        x = xt
        y = yt


def Speed(drive, turn):
    if drive:
        if 0 < drive < 101:
            print("    drivetrain.set_drive_velocity(", str(drive),", PERCENT)")
        elif drive > 101:
            print("    drivetrain.set_drive_velocity(100, PERCENT)")
        else:
            print("    drivetrain.set_drive_velocity(1, PERCENT)")
    if turn:
        if 0 < turn < 101:
            print("    drivetrain.set_turn_velocity(", turn,", PERCENT)")
        elif turn > 101:
            print("    drivetrain.set_turn_velocity(100, PERCENT)")
        else:
            print("    drivetrain.set_turn_velocity(1, PERCENT)")

def S(drive, turn):
    Speed(drive, turn)

def End():
    print("    stop_project()\nvr_thread(main())")