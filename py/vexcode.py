class BLACK:
    color = "\u001b[0m"
    str = "black"


class BLUE:
    color = "\u001b[36m"
    str = "blue"


class GREEN:
    color = "\u001b[32m"
    str = "green"


class RED:
    color = "\u001b[31m"
    str = "red"


class RESET:
    color = "\u001b[0m"


class SECONDS:
    unit = "SECONDS"


class MSEC:
    unit = "MSEC"


class FORWARD:
    direction = "FORWARD"


class LEFT:
    direction = "LEFT"


class RIGHT:
    direction = "RIGHT"


class REVERSE:
    direction = "REVERSE"


class DEGREES:
    unit = "DEGREES"


class RADIANS:
    unit = "RADIANS"


class PERCENT:
    unit = "PERCENT"


class MM:
    unit = "MM"


#! inches are for scrubs
class INCH:
    unit = "INCH"


class X:
    axis = "X"


class Y:
    axis = "Y"


class BOOST:
    energy = "BOOST"


class DROP:
    energy = "DROP"


class UP:
    position = "UP"


class DOWN:
    position = "DOWN"


monitor_variable = lambda *v: print(f"Monitoring the variable(s) {v}")
monitor_sensor = lambda *v: print(f"Monitoring the sensor(s) {v}")
wait = lambda t, un: print(f"waiting for {t} {un.unit}")
stop_project = lambda: __endProgram__()


class brain:
    print = lambda msg: print(msg)
    clear = lambda: clear()
    newline = lambda: print("\n")
    set_print_color = lambda col: print(f"set print color to {col.str}")
    timer_reset = lambda: print("reset the timer")
    timer_time = lambda un: print(f"Returned time in {un.unit}")


class drivetrain:
    drive = lambda dir: print(f"Driving {dir}")
    drive_for = lambda dir, dist, un: print(
        f"Driving {dir.direction} for {dist} {un.unit}"
    )
    turn = lambda dir: print(f"Turning {dir}")
    turn_for = lambda dir, ang, un: print(
        f"Turning {dir.direction} for {ang} {un.unit}"
    )
    turn_to_heading = lambda ang, un: print(f"Turning to Heading {ang} {un.unit}")
    turn_to_rotation = lambda ang, un: print(f"Turning to Rotation {ang} {un.unit}")
    stop = lambda: print("Stopped")
    set_drive_velocity = lambda per, un: print(
        f"Set driving Velocity to {per} {un.unit}"
    )
    set_turn_velocity = lambda per, un: print(
        f"Set turning Velocity to {per} {un.unit}"
    )
    set_heading = lambda deg, un: print(f"Changed heading to {deg} {un.unit}")
    set_rotation = lambda deg, un: print(f"Changed rotation to {deg} {un.unit}")
    is_done = lambda: print("Retunring if drivetrain is done moving")
    is_moving = lambda: print("Returns if the drivetrain is moving")
    heading = lambda un: print(f"Returning heading in {un.unit}")
    rotation = lambda un: print(f"Returning rotation in {un.unit}")


class location:
    position = lambda ax, un: print(
        f"Returning Position of the {ax.axis}-axis in {un.unit}"
    )
    position_angle = lambda un: print(f"Returning angle in {un.unit}")


class distance:
    found_object = lambda: print("Searching for Object")
    get_distance = lambda un: print(f"Returning distance in {un.unit}")


class down_eye:
    near_object = lambda: print("Returns if the down eye is near an object")
    detect = lambda col: print(f"Returns if the color {col.str} detected by down eye")
    brightness = lambda un: print(
        f"Returns the Brightness in {un.unit} detected by down eye"
    )


class front_eye:
    near_object = lambda: print("Returns if the front eye is near an object")
    detect = lambda col: print(f"Returns if the color {col.str} detected by front eye")
    brightness = lambda un: print(
        f"Returns the Brightness in {un.unit} detected by front eye"
    )


class left_bumper:
    pressed = lambda: print("Returns if the left bumper is pressed")


class right_bumper:
    pressed = lambda: print("Returns if the right bumper is pressed")


class magnet:
    energize = lambda e: print(f"Magnet set to {e}")


class pen:
    move = lambda pos: print(f"Moved Pen {pos}")
    set_pen_color = lambda col: print(f"Set print color to {col}")


def main(e):
    pass


def vr_thread(f):
    vex_start(f)

# *=+=+=+=+=+=+ Turtle :D
from math import pi, sin
from asyncio import coroutine, iscoroutinefunction as iscoroutine, run as asyncRun
from json import loads as jsonload
from pathlib import Path
from timeit import default_timer as timer
from turtle import *

# *=+=+=+=+= Vars

__mapsf__ = "maps.json"


def __Maps__(map):
    global _user, __mapTurtle
    _user.penup()
    if map == "Grid Map":
        _user.goto([-900, -900])
    elif map == "Number Grid Map":
        _user.goto([-900, -900])
        __mapTurtle.goto([-900, -900])

    elif map == "Art Canvas":
        pass
    elif map == "Disk Maze":
        pass
    elif map == "Wall Maze":
        pass
    elif map == "Disk Mover":
        pass
    elif map == "Disk Transport":
        pass
    elif map == "Castle Crusher":
        pass
    else:
        print(f"{map} is currently not supported, Sorry!")
        __endProgram__()
    _user.pendown()


# Current Accepted maps
"""{
    "Grid Map":"Grid",
    "Number Grid Map": "Number",
    "Art Canvas": "ArtCanvas",
    "Disk Maze": "PuckMaze",
    "Wall Maze": "WallMaze",
    "Disk Mover": "DiskMover",
    "Disk Transport": "Magnet",
    "Castle Crusher": "CastleCrasher",
}"""
# *=+=+=+=+=

# *=+=+=+=+= Init Stuffs
def __init__():
    global __screen, _settings
    _settings = settings()
    __screen = Screen()
    # * Makes screen show the whole map
    __screen.setworldcoordinates(-1000, -1000, 1000, 1000)
    __user__()
    __border__()
    __map__()


def __user__():
    global _user
    _user = Turtle()
    _user.penup()
    _user.pensize(5)


def __border__():
    global __mapTurtle

    # * initallize
    __mapTurtle = Turtle()
    __mapTurtle.hideturtle()
    __mapTurtle.speed(0)

    # * goto edge
    __mapTurtle.penup()
    __mapTurtle.goto([-1000, -1000])
    __mapTurtle.pendown()

    # * frame
    __mapTurtle.width(10)
    _moveto(
        __mapTurtle,
        [[-1000, -1000], [-1000, 1000], [1000, 1000], [1000, -1000], [-1000, -1000]],
    )

    # * Left Y-axis lines
    __mapTurtle.width(1)
    _moveto(
        __mapTurtle,
        [
            [-800, -1000],
            [-800, 1000],
            [-600, 1000],
            [-600, -1000],
            [-400, -1000],
            [-400, 1000],
            [-200, 1000],
            [-200, -1000],
        ],
    )

    # * Y-axis
    __mapTurtle.width(3)
    _moveto(__mapTurtle, [[0, -1000], [0, 1000]])

    # * Right Y-axis Lines
    __mapTurtle.width(1)
    _moveto(
        __mapTurtle,
        [
            [800, 1000],
            [800, -1000],
            [600, -1000],
            [600, 1000],
            [400, 1000],
            [400, -1000],
            [200, -1000],
            [200, 1000],
        ],
    )

    # * Prep for next move
    __mapTurtle.goto([-1000, 1000])

    # * Down X-axis Lines
    __mapTurtle.width(1)
    _moveto(
        __mapTurtle,
        [
            [-1000, -800],
            [1000, -800],
            [1000, -600],
            [-1000, -600],
            [-1000, -400],
            [1000, -400],
            [1000, -200],
            [-1000, -200],
        ],
    )

    # * X-axis]
    __mapTurtle.width(3)
    _moveto(__mapTurtle, [[-1000, 0], [1000, 0]])

    # * Up X-axis Lines
    __mapTurtle.width(1)
    _moveto(
        __mapTurtle,
        [
            [1000, 800],
            [-1000, 800],
            [-1000, 600],
            [1000, 600],
            [1000, 400],
            [-1000, 400],
            [-1000, 200],
            [1000, 200],
        ],
    )


def __map__():
    mapsList = ""
    maps = []
    mapids = []
    i = 0
    try:
        for k, v in __openJson__(__mapsf__).items():
            maps.append(k)  # * add map name to maps[]
            mapids.append(v)  # * add map id to mapids[]
            mapsList += f"{i}. {k}\n"
            i += 1

    except:
        raise Exception(
            f"\n{RED.color}File {BLUE.color}{__mapsf__} {RED.color}Does not exist!\n{RESET.color}"
        )

    # * Has User pick a map
    def choseMap(mapsList):
        global id
        try:
            id = int(__screen.textinput("Chose Map", mapsList))
            id = maps[id]

        except KeyboardInterrupt:
            __endProgram__()

        except:
            mapsList += "\nNot a valid Number"
            id = choseMap(mapsList)

        finally:
            return id

    map = choseMap(mapsList)
    __Maps__(map)
    print(f"{GREEN.color}Map: {BLUE.color}{map}{RESET.color}\n\n")


def vex_start(f):
    global __start
    __start = timer()
    if not iscoroutine(f):
        f = coroutine(f)
    f(e)
    __endProgram__()


__openJson__ = lambda f: jsonload(
    open(Path(__file__).parent.parent / "json" / f).read()
)


def _moveto(t, c):
    for b in c:
        t.goto(b)


def __endProgram__():
    print(f"\n\n{GREEN.color}Time Elasped: {round(timer() - __start,4)} Seconds")
    input("Press any button to end!\n")
    print(f"{RESET.color}Bye!\n")
    exit()


# *=+=+=+=+= Universal Threading Teritory
class settings:
    def __init__(self, unit=MM, strict=True):
        self.unit = unit
        self.strict = strict


def __pickup_drop__(target, endpoint):
    global _user
    _user.pos
    _moveto(_user, target)
    if endpoint == "return":
        _moveto(_user, pos)
    elif endpoint:
        _moveto(_user, endpoint)


class e:
    def init(self,unit=None, strict=None):
        global settings
        __init__()
        settings = settings()
    
    def __init__(self):
        print("test")
        self.init()

    def move(*targets):
        for t in targets:
            _user.goto(t)

    drop = lambda target, endpoint=None, *a: __pickup_drop__(target, endpoint)

    sync = lambda *a: print(
        f"{BLACK.color}Syncing...\n{GREEN.color}Synced\n{RESET.color}"
    )

    print = lambda m, c=BLACK: print(c.color + m + RESET.color)

    def pen(*args):
        for arg in args:
            if arg in [RED, GREEN, BLUE, BLACK]:
                _user.pencolor(arg.str)
            elif arg in [UP, DOWN]:
                if arg.position == "UP":
                    _user.penup()
                else:
                    _user.pendown()
            else:
                raise Exception(
                    f"{arg} is not a pen action.\nThe valid actions are...\nChanging Color: [RED,GREEN,BLUE,BLACK]\nor Changing Position: [UP,DOWN]"
                )

    def polygon(
        self, dir, sides: int, radius: float, heading: float = 0, sidesMax: int = None
    ):
        angle = 360 / sides
        dist = sin(pi / sides) * radius
        self.heading(heading + 90)
        if not sidesMax:
            sidesMax = sides
        for i in range(sidesMax):
            self.turn(dir, angle)
            self.drive(FORWARD, dist)

    def drive(dir, dist):
        if dir == FORWARD:
            _user.forward(dist)
        elif dir == REVERSE:
            _user.back(dist)
        else:
            raise Exception(
                f"{RED.color}{dir} is not a valid direction!\n Use FORWARD or REVERSE!{RESET.color}"
            )

    def turn(dir, angle):
        if dir == LEFT:
            _user.left(angle)
        elif dir == RIGHT:
            _user.right(angle)
        else:
            raise Exception(
                f"{RED.color}{dir} is not a valid direction!\n Use RIGHT or LEFT!{RESET.color}"
            )

    heading = lambda angle=0: _user.setheading(angle)
