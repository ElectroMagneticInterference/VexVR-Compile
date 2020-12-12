# VexVR-Compile
### A code simplifier and compiler for VexVR Python, You type the coords, and we do the rest.

## Reference:

**Leave comments of new Ideas to add to the compiler, we really want the input!**


### Pen
* Description:
  * Moves the pen, and sets the color

* Syntax: 

    ```python
    Pen.Pen("Position", "Color")  #Changes the pen position, and or color at the same time
    ```
    or 
    ```python
    Pen.Move("Position")        #Changes the pen position
    Pen.M("Position")
    ```
    or
    ```python
    Pen.Color("Color")          #Changes the pen color
    Pen.C("Color")    
    ```

    * Both Position and color will be turned into the correct unit, so don't worry about capitalization!
    * Either value can be set to `False` to be ignored


### Brain
* Description:
  * Send console messages, change message color, make new line, and/or clear the console

* Syntax: 

    ```python
    Brain.P("Message")    #prints in the brain console
    ```
    or
    ```python
    Brain.Color("Color")  #Sets print color in the brain console
    Brain.C("Color")
    ```
    or
    ```python
    Brain.Newline()       #makes a new line in the brain console, 
    Brain.Nl()            #although its easier to just have the message end in "\n"
    ```
    or
    ```python
    Brain.Clear()         #clears the Brain console.
    Brain.Cl()
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
    Drivetrain.Driving_Speed(Driving_Speed)  
    Drivetrain.DS(Driving_Speed)  
    ```
    or
    ```python
    Drivetrain.Turning_Speed(Driving_Speed)  
    Drivetrain.TS(Driving_Speed)  
    ```
    or
    ```python
    Drivetrain.Speed(Driving_Speed, Turning_Speed)  
    Drivetrain.S(Driving_Speed, Turning_Speed)
    ```
  
    * Both Speed values are intergers in the range 1-100
    * Either value can be set to `False` to be ignored
    * values above and below the range will be set to the closest value in the range.




  #### To
  * Description:
    * Moves the bot to the desired co-ordinates, calculating the angle with preprocessing

  * Syntax: 

    ```python
    Move.To([ [x,y] ])
    ```
    or
    ```python
    Move.To([ [x,y], [x,y], ... ])
    ```

    * Each entry in the array is a co-ordinate pair of x and y in an array
    * There can be **ANY NUMBER OF** co-ordinate pairs to travel to!


  #### Object Move
  * Description:
    * Activates the ElectroMagnet, goes to position, stops if item is picked up before end coords
    * then it either...
      1. Stops
      2. Returns to previous position
      3. goes to another, final position
  
  * Syntax: 

    ```python
    Move.Object([ [x,y] ])
    Move.Obj([ [x,y] ])
    ```
    or
    ```python
    Move.Object([ [x,y], "return" ])
    Move.Obj([ [x,y], "return" ])
    ```
    or
    ```python
    Move.Object([ [x,y], [x,y] ])
    Move.Obj([ [x,y], [x,y] ])
    ```
 
    * Each entry in the array is a co-ordinate pair of x and y in an array
    * There can be **ANY NUMBER OF** co-ordinate pairs to travel to!


  #### Drop Move
  * Description:
    * Moves, drops.

  * Syntax: 

    ```python
    Move.Drop([ [x,y] ])
    ```
    or
    ```python
    Move.Drop([ [x,y], "return" ])
    ```
    or
    ```python
    Move.Drop([ [x,y], [x,y] ])
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
