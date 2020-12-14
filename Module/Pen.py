import re
def Pen(p, c):
    if p:
        p = Verify("Position", p)
        print("    pen.move(\"", p, "\")")
    if c:
        c = Verify("Color", c)
        print("    pen.set_pen_color(\"" + c + "\")")
def Move(p):
    p = Verify("Position", p)
    print("    pen.move(\"" + p + "\")")
def M(p): Move(p)
def Color(c): 
    c = Verify("Color", c) 
    print("    pen.set_pen_color(\"" + c + "\")")
def C(c): Color(c)
def Verify(type, thing):
    if type == "Position":
        if   re.search(r"(?i)down", thing):  return "DOWN"
        elif re.search(r"(?i)up",   thing):  return "UP"
        else:
            print('\x1b[0;31;40m' + 'FAILED! \n' + '\x1b[0m' + 'That is not a Valid position! The valid positions are either "UP" or "DOWN" (not cap senstive)')
            exit('That is not a Valid position!')

    elif type == "Color":
        if   re.search(r"(?i)red",   thing):  return "RED"
        elif re.search(r"(?i)green", thing):  return "GREEN"
        elif re.search(r"(?i)blue",  thing):  return "BLUE"
        elif re.search(r"(?i)black", thing):  return "BLACK"
        else:
            print('\x1b[0;31;40m' + 'FAILED! \n' + '\x1b[0m' + 'That is not a Valid Color!\n The valid colors are "BLACK", "RED", "GREEN", and "BLUE" (not cap senstive)')
            exit('That is not a Valid Color!')