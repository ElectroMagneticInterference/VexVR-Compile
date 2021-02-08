# ![VEXCODE VR logo](Assets/VEXVR.png)
### A code framework for VexVR Python. You type the coords, and we do the rest.

These docs are also on our [website](http://vexvr.orangehersheys.dev/)

## Disclaimer:
This project is just for fun, and getting into the door for further vex coding shenanigans.

We also don't recommend using this for any classes using vexvr, you should learn to code not cheat.

## Reference:

**Leave comments of new Ideas to add to the framework, we really want the input!**

Currently, you cannot use the normal commands in main().
This is a issue due to the threading and preprocessor, so it would be all messed up.
With this in mind, We are porting all of the commands into the classes so it can also be used normally.
We are also adding shortcuts, sensor detection, and the like to improve the effectiveness of your programming.


####   Legend:
- str::value = `type::what_it_is`
    - example:
        ```cs
        int::interger
        bool::boolean
        str::string
        float::float
        ```
- Coord =
    ```cs
    [int::x, int::y]
    ```
- Colors = 
    ```python
    BLACK, BLUE, RED, or GREEN
    ```
- Positions = 
    ```python
    UP or DOWN
    ```
- `*something` = any amount of {something}
- `(thing1\|thing2)` = accepts either value
- `something?` = arg is optional

#### `e.move(*Coord)`
- Move to coordinates, then next if specified

#### `e.pickup(Coord)`
- active magnet, move to coord

#### `e.pickup(Coord, "return")`
- normal, but returns to previous coord

#### `e.pickup(Coord, Coord)`
- normal, but after first move, it goes to second.


#### `e.drop(Coord)`
- move to coord, deactive magnet

#### `e.drop(Coord, "return")`
- normal, but returns to previous coord

#### `e.drop(Coord, Coord)`
- normal, but after first move, it goes to second.


#### `e.pen(*Color\|Position)`
- enter a Pen color or position, and it does that.
- WARNING: this slows down the bot a lot!

#### `e.print(message, color?)`
- prints Message in color specified, else, black

#### `e.sync()`
- syncs the threads to improve accuracy after a few moves.

#### `e.settings(options?)`
- This must be the first line in main(), or else the custom settings would only act thoughout part of the program and mess up the program.
- lets you choose the settings for the program.
- options:
    - unit= `(INCH\|MM)`:   changes the unit the program is in, default is MM
    - strict= boolean: If True, syncs after every move
          - WARNING: slows down the bot, but improves accuracy.



> ### don't sue us VEX, **please**
> \- us


