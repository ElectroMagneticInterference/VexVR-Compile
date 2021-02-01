# =+=+=+= Reference
#
#   legend:
#       e = the class with functions to do, it has a Arbitray variable name
#       str::value: type :: what_it_is
#       Coord: [int::x, int::y]
#       *something: any amount of {something}
#       (thing1|thing2): accepts either value
#       something?: arg is optional
#
#   e.init(options?)
#       Initalizes the program, and lets you choose the settings for the program.
#
#       ! This MUST be the first line of the main() function.
#
#       unit:   changes the unit the program is in (INCH|MM)
#               defaults to MM
#       strict: If True, syncs after every move,
#           slows down the bot, but improves accuracy.
#               defaults to False
#
#   e.move(*Coord)
#
#   e.pickup(Coord)
#       active magnet, move to coord
#   e.pickup(Coord, "return")
#       normal, but returns to previous coord
#   e.pickup(Coord, Coord)
#       normal, but after first move, it goes to second.
#
#   e.drop(Coord)
#       move to coord, deactive magnet
#   e.drop(Coord, "return")
#       normal, but returns to previous coord
#   e.drop(Coord, Coord)
#       normal, but after first move, it goes to second.
#
#   e.pen(*Color|Position)
#       enter a Pen color or position, and it does that.
#
#   e.print(message, color?)
#
#   e.sync()
#       syncs the threads to improve accuracy after a few moves.
#
#
# =+=+=+=

#!=+=+=+=+=+==+=+=+=+=+ BEWARE =+=+=+=+==+=+=+=+=+=!#
#!                                                 !#
#!  BEYOND THIS POINT, IS THE CODING STUFFS DON'T  !#
#!  MESS WITH UNLESS YOU KNOW WHAT YOU ARE DOING,  !#
#!  OR IF YOU JUST WANT TO                         !#
#!                                                 !#
#!=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=!#

# =+=+=+==+=+=+= The Program
"""
Starts 3 Seperate threads each with their own specific tasks.
The threads all interact in specific ways to ensure that the robot goes as fast as possible.
"""

# =+=+=+= Library Imports
from .vexcode import *
import math

# =+=+=+=

# =+=+=+= Settings Class
class settings:
    def __init__(self, unit=MM, strict=True):
        self.unit = unit
        self.strict = strict


# =+=+=+=

# =+=+=+= Calculation Thread
"""
The _calculate() thread calculates the angles
    and positions, then stores them for the _movement()
    thread to use when it gets there.

    This thread needs to be able to effectively calculate
    the movements needed to do the actions in _main()
"""
_coords = []
_calc_wait = True
_move_wait = True
"""
This class is utilized by the preprocessor to calculate the
distances and angles from the coordinates given.
"""


class create_coords:
    # pre established values for the direction
    dir = FORWARD
    P_dir = "Forward"

    # activate function when class is created.
    def __init__(self, target, dir=None):
        """
        The _nextPosCoord is not ideal, but it is the best way I could find
        to preprocess the values. The future _tolerance() thread should dynamically fix
        the issues if they arrise.
        """
        global _nextPosCoord, _current_angle
        # sets the coordinates started from as the _nextPosCoord {needs better name} value.
        self.start = _nextPosCoord
        # sets the _nextPosCoord value to the target value, for the next coord to use.
        _nextPosCoord = target

        self.target = target

        # translate the orgin to the current position, and everything else by that translation.
        # subtract the current position by the position the orgin is Driving to.
        self.target_relative = [
            self.target[0] - self.start[0],
            self.target[1] - self.start[1],
        ]
        x = self.target_relative[0]
        y = self.target_relative[1]

        # find the length of the new target vector, using sqr(x^2+y^2)
        self.dist = math.sqrt(x * x + y * y)

        # round it for logging purposes
        self.P_dist = math.ceil(self.dist)

        """
        Calculates the angle, relative to the x axis, of the vector from the bot's position
        to the destination coords.
        Gets the angle of the vector
        the math for it is explained on the github page
        """
        if x != 0 and y != 0:
            self.angle = math.degrees(math.atan2(x, y))
            # if angle is negative, add 360
            if self.angle < 0:
                self.angle += 360
        # if the angle is a multiple of 90
        elif y > 0:
            self.angle = 0
        elif x > 0:
            self.angle = 90
        elif y < 0:
            self.angle = 180
        elif x < 0:
            self.angle = 270

        # throw error if the coords are the same as the starting coords.
        else:
            raise Exception(
                f"The target coord is the same as the previous!\n movement #{len(_coords)}"
            )

        angle_margin = [_current_angle - 90, _current_angle + 90]
        for i in angle_margin:
            if i < 0:
                i += 360

        if dir:
            if dir == REVERSE:
                self.dir = REVERSE
                self.P_dir = "Reverse"
                self.angle += 180

        elif angle_margin[0] > self.angle < angle_margin[1]:
            self.dir = REVERSE
            self.P_dir = "Reverse"
            self.angle += 180

        _current_angle = self.angle

        self.P_angle = math.ceil(self.angle)


"""
This class is given to the main() function to use.
This class defines the preprocessor versions of the functions used in main
"""


class _calc:
    def init(self, unit=MM, strict=False):
        global _nextPosCoord, _current_angle, settings
        settings = settings(unit=unit, strict=strict)
        _nextPosCoord = [
            location.position(X, settings.unit),
            location.position(Y, settings.unit),
        ]
        _current_angle = location.position_angle(DEGREES)
        _log.append(message("Initated\n\n\n", GREEN))

    """
    the 'hidden' function which the other functions use to move.
    this function has more options for the program then is needed
    for the user.
    """

    def __move(self, target, dir=None, log=False):
        global _coords, _nextPosCoord
        coord = create_coords(target, dir=dir)
        if log:
            coord.log = log
        elif log != None:
            coord.log = (
                f"Driving {coord.P_dir} from {coord.start} to {coord.target}\n\n"
            )
        _nextPosCoord = target
        _coords.append(coord)
        if settings.strict:
            self.__sync()
        wait(3, MSEC)
        return coord

    """
    The move function used by people, this can accept many coordinates
    for each coordinate given, it activates the __move() function with
    that value
    """

    def move(self, *targets1):
        for target in targets1:
            self.__move(target)

    # Function used by pickup() and drop()
    def __pickup_move(self, target, endpoint, log):
        global _nextPosCoord
        # activate __move() with the first coord value
        if endpoint == "return":
            _endPrint = _nextPosCoord
        else:
            _endPrint = endpoint
        log += f" at {target}\n\tDriving Forward from {_nextPosCoord} to {target}\n"
        if endpoint:
            log += f"\tThen, Driving Reverse from {target} to {_endPrint}\n\n"
        else:
            log += "\n"

        coord = self.__move(target, FORWARD, log)
        """
        checks if there is an endpoint value,
        if it equals "return" go to starting coord
        else, go to the coord specified.
        """
        if endpoint == "return":
            _nextPosCoord = coord.start
        elif endpoint:
            self.__move(endpoint, log=None)

    """
    pickup and drop are identical to the preprocessor,
    besides their name, and their logging value.
    """

    def pickup(self, target, endpoint=None):
        # base log value, rest is added on as its identical to self.drop()
        log = "Picking up item"
        self.__pickup_move(target, endpoint, log=log)

    def drop(self, target, endpoint=None):
        log = "Dropping item off"
        self.__pickup_move(target, endpoint, log=log)

    """
    The sync cosettings.unitand is arguabully the most usefill cosettings.unitand.
    This cosettings.unitand stops the _calculate() thread until the _movement()
    thread catches up. This also resets the position know to the
    _calculate() thread, so it can reajust its position and improve accuracy.
    """

    def __sync(self, *args):
        global _calc_wait, _nextPosCoord, _move_wait
        while _calc_wait:
            wait(1, MSEC)
        if not settings.strict:
            _log.append(message("Synced\n\n", GREEN))
        _nextPosCoord = [
            location.position(X, settings.unit),
            location.position(Y, settings.unit),
        ]
        _calc_wait = True
        _move_wait = False
        wait(1, MSEC)

    def sync(self, *args):
        if not settings.strict:
            self.__sync()

    # this is unused in the preprocessor, but is required to not throw errors
    def pen(*args):
        pass

    def print(*args):
        pass


def _calculate():
    main(_calc())
    _end()


# =+=+=+=

# =+=+=+= Movement Thread
"""
The _movement() thread takes the stored values
    from the _calculate() thread, then inteperatest
    the value, finally actually doing them.

    This thread is ment to be as fast as possible,
    taking as little time between movements as possible.
    When currently in movement, the other threads have
    time to do what they need.
"""


class _move:
    def init(self, unit=MM, strict=False, *args1):
        wait(1, MSEC)

    def __move(self, *i):
        global _log
        # gets coord calculated in _calculate()
        coord = _coords[0]

        # turns and moves as specified
        drivetrain.turn_to_heading(coord.angle, DEGREES, True)
        wait(1, MSEC)
        drivetrain.drive_for(coord.dir, coord.dist, settings.unit)

        # pops coords used, and send data to logs.
        try:
            _log.append(message(coord.log))
        except:
            pass
        _coords.pop(0)
        if settings.strict:
            self.__sync()
        return coord

    def move(self, *targets):
        # repeats following function for the amount of
        # parameters in targets
        for i in range(len(targets)):
            self.__move()

    def pickup(self, target, endpoint=None, *args):
        magnet.energize(BOOST)
        # initalizes move, no paramets as its precalculated
        coord = self.__move()
        wait(1, MSEC)
        if endpoint == "return":
            drivetrain.drive_for(REVERSE, coord.dist, settings.unit)
        elif endpoint:
            self.__move()

    # same as pickup() but different magnet usage
    def drop(self, target, endpoint=None, *args):
        coord = self.__move()
        wait(1, MSEC)
        magnet.energize(DROP)
        if endpoint == "return":
            drivetrain.drive_for(REVERSE, coord.dist, settings.unit)
        elif endpoint:
            self.__move()

    # This is the action side of the sync() cosettings.unitand
    def __sync(self, *args1):
        global _calc_wait, _move_wait
        _calc_wait = False
        if not settings.strict:
            _log.append(message("Syncing...\n", BLACK))
        while _move_wait:
            wait(1, MSEC)
        _move_wait = True
        while True:
            try:
                if _coords[0]:
                    break
            except:
                wait(1, MSEC)

    def sync(self, *args1):
        if not settings.strict:
            self.__sync()

    # controls the pen
    def pen(self, *args):
        for arg in args:
            if arg in [RED, GREEN, BLUE, BLACK]:
                pen.set_pen_color(arg)
            elif arg in [UP, DOWN]:
                pen.move(arg)
            else:
                raise Exception(
                    f"{arg} is not a pen action.\nThe valid actions are...\nChanging Color: [RED,GREEN,BLUE,BLACK]\nor Changing Position: [UP,DOWN]"
                )
            wait(1, MSEC)

    # print commands
    def print(self, m, c=None):
        _log.append(message(m, c, True))


def _movement():
    # inital setup!
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_turn_velocity(100, PERCENT)
    # this has to wait long enough for _calculation() thread
    # to calculate the first movement.
    wait(3, MSEC)
    main(_move())
    _end()


# =+=+=+=

# =+=+=+= Misc Thread
"""
The _misc() thread waits for things to appear
    in _log, once it does, it logs the value, cycles
    the color, then pops the log value.

! This is important, as without it, it takes away
    ! alot of time from the other threads, and you cannot
    ! print within class functions, which most of this
    ! Program is.
"""


class message:
    def __init__(self, message, color=None, user=False):
        self.message = message
        self.color = color
        self.user = user


_log = []
_log_color = BLACK


def _misc():
    global _threads_active
    brain.clear()
    brain.set_print_color(BLACK)

    def log():
        global _log, _log_color
        if _log[0]:
            if _log[0].color:
                color = _log[0].color
            else:
                color = _log_color
            brain.set_print_color(color)
            if not _log[0].user:
                if _log_color == BLACK:
                    _log_color = BLUE
                else:
                    _log_color = BLACK

            try:
                brain.print(_log[0].message)
            except:
                brain.print(_log[0])
            _log.pop(0)

    while _threads_active:
        try:
            log()
            wait(1, MSEC)
        except:
            wait(5, MSEC)
    log()
    _end()


# =+=+=+=

# -- testing
# #=+=+=+= Tolerance Testing Thread
#
# _Finshed_coords = []
# _move_finished = None
# def _tolerance():
#     global _move_finished, _threads_active
#     while _threads_active:
#         while not _move_finished:
#             wait(5, MSEC)
#
#         _Finshed_coords.append(_move_finished)
#         brain.print(_move_finished.log)
#         _move_finished = None
#     _end()
# #=+=+=+=
# -- testing

# =+=+=+= Ending
"""
This function activates at the end of every thread.

    The _calculate() and _movement() threads are always
    the first to deactive. Once they do, they both call
    this function, which will keep a tab of how many
    threads have activated it. Once, both the _calculate()
    and _movement() threads have ended, this will tell the
    other threads to initate their final actions.
"""
_threads_active = True
_end_tracker = 0


def _end():
    global _end_tracker, _threads_active
    _end_tracker += 1
    if _end_tracker >= 2:
        _threads_active = False
    if _end_tracker >= 3:
        brain.set_print_color(GREEN)
        brain.print(f"\n\nTime Elasped: {brain.timer_time(SECONDS)}")
        stop_project()


# =+=+=+=

# =+=+=+= Starting
vr_thread(_calculate())
vr_thread(_movement())
vr_thread(_misc())


# =+=+=+= EXPERIMENTAL
# These next ones are still in testing.

# vr_thread(_tolerance())
"""
The _tolerance() thread receives information at the end
    of each movement, and checks if they are in acceptable
    tolerance. If the current angle or coords are outside
    of the tolerance range, it will print a warning, and
    have the _calculation() thread recalculate the movements
    from that point forward.
"""