# VexVR-Compile
### A code simplifier and compiler for VexVR Python, You type the coords, and we do the rest.

We are still developing this, and it will not be finished for a while, but we eventually want to turn this into a program or site to deal with normal Vex code as well as a version for VexVR


## Reference:

**Leave comments of new Ideas to add to the compiler, we really want the input!**


### Pen
* Description:
  * Moves the pen, and sets the color

* Syntax: 

    ```python
    Pen("Position", "Color")
    #Changes the pen position, and or color at the same time
    ```
    or 
    ```python
    Pen.Move("Position")
    Pen.M("Position")
    #Changes the pen position
    ```
    or
    ```python
    Pen.Color("Color")
    Pen.C("Color")
    #Changes the pen color
    ```

    * Both Position and color will be turned into the correct unit, so don't worry about capitalization!
    * Either value can be set to `False` to be ignored


### Brain
* Description:
  * Send console messages, change message color, make new line, and/or clear the console

* Syntax: 

    ```python
    Brain.Print("Message")
    Brain.P("Message")
    #prints in the brain console
    ```
    or
    ```python
    Brain.Color("Color")
    Brain.C("Color")
    #Sets print color in the brain console
    ```
    or
    ```python
    Brain.Newline()
    Brain.Nl()
    #makes a new line in the brain console,
    #although its easier to just have the message end in "\n"
    ```
    or
    ```python
    Brain.Clear()         #clears the Brain console.
    Brain.Cl()
    #Clears the Brain Terminal
    ```
    
    * the Color **DOES NOT** have to follow the VexVR color convention, the program will correct the casing of the colors.

### Move 
* Description:
  * Controls and gives shortcuts for the drivetrain
  
  #### Speed
  * Description:
    * sets the driving and turning speed to a range of 1-100%

  * Syntax: 

    ```python
    Driving_Speed(Driving_Speed)  
    DS(Driving_Speed)
    #Sets Driving Speed
    ```
    or
    ```python
    Turning_Speed(Driving_Speed)  
    TS(Driving_Speed)
    #Sets Turning Speed
    ```
    or
    ```python
    Speed(Driving_Speed, Turning_Speed)  
    S(Driving_Speed, Turning_Speed)
    #Sets Driving Speed, and or Turning Speed
    ```
  
    * Both Speed values are intergers in the range 1-100
    * Either value can be set to `False` to be ignored
    * values above and below the range will be set to the closest value in the range.




  #### To
  * Description:
    * Moves the bot to the desired co-ordinates, calculating the angle with preprocessing

  * Syntax: 

    ```python
    Move([ [x,y] ])
    #turns (if needed), Moves
    ```
    or
    ```python
    Move([ [x,y], [x,y], ... ])
    #turns (if needed), Moves, repeats
    ```

    * Each entry in the array is a co-ordinate pair of x and y in an array
    * There can be **ANY NUMBER OF** co-ordinate pairs to travel to!


  #### Object_Move
  * Description:
    * Activates the ElectroMagnet, goes to position, stops if item is picked up before end coords
    * then it either...
      1. Stops
      2. Returns to previous position
      3. goes to another, final position
  
  * Syntax: 

    ```python
    Object_Move([ [x,y] ])
    Obj([ [x,y] ])
    #Start Magnet, Move
    ```
    or
    ```python
    Object_Move([ [x,y], return ])
    Obj([ [x,y], return ])
    #Start Magnet, Move, Return
    ```
    or
    ```python
    Object_Move([ [x,y], [x,y] ])
    Obj([ [x,y], [x,y] ])
    #Start Magnet, Move, Move
    ```
 
    * Each entry in the array is a co-ordinate pair of x and y in an array
    * There can be **ANY NUMBER OF** co-ordinate pairs to travel to!


  #### Drop_Move
  * Description:
    * Moves, Released Magnet

  * Syntax: 

    ```python
    Drop_Move([ [x,y] ])
    Drop([ [x,y] ])
    #Move, Drop
    ```
    or
    ```python
    Drop_Move([ [x,y], return ])
    Drop([ [x,y], return ])
    #Move, Drop, Return
    ```
    or
    ```python
    Drop_Move([ [x,y], [x,y] ])
    Drop([ [x,y], [x,y] ])
    #Move, Drop, Move
    ```

    * The first coordinate is where it moves to, then it Realeases the EletroMagnet.
    * then it either...
      1. Stops
      2. Returns to previous position
      3. goes to another, final position


### Example
* Description:
  * Describes the thing

* Syntax: 

  ```python
  Some code reference
  ```
  or
  ```python
  Another syntax option
  ```
 
  * inform about Syntax
  * and tell about options


> ### don't sue us VEX, **please**
> \- us
