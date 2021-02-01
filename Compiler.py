#*=+=+=+=+=+ Imports
import json, os, re
from pathlib import Path

#*=+=+=+=+=+ Variables
#* extentions Base
addonf = "Universal Threading.py"

#* VR Json Base
vrJB = "vrpython.json"

#* maps file
mapsf = "maps.json"


#*=+=+=+=+=+ Colors
cReset = "\u001b[0m"
cPrimary = "\u001b[32m"
cSecondary = "\u001b[0;33m"
cInput = "\u001b[36m"
cException = "\u001b[31m"


#*=+=+=+=+=+ Inital
#* inital Function to run
def init():
    print("\n")

    #* Initalize Json
    initJson()

    #* Get file to compile
    f, fn = enterFile()

    #* Get contents from selected file
    fc = extractContents(f)

    #* Chose the map
    idIndex = choseMap()

    print(f"\n{cPrimary}selected {cInput}{maps[idIndex]}{cPrimary}\n")

    fc["playground"] = maps[idIndex]

    fout = f"{Path(__file__).parent}\\vrpython\\{fn}.vrpython"
    if os.path.exists(fout):
        os.remove(fout)

    fout = open(fout,"wt")
    fout.write(json.dumps(fc, sort_keys=True, indent=4))
    fout.close()

    #* Print when the program is done.
    print(f"{cPrimary}Finished!\nFile {cInput}{fn}.py{cPrimary} has been compiled into {cSecondary}{fn}.vrpython{cPrimary}!{cReset}")

    input("Press Any key to exit...")
    endProgram()


#*=+=+=+=+=+ Initalize Map List
mapids=[]
maps=[]

#*Make a list of maps
mapsList = f"\n{cPrimary}Chose a Map!\n"

def initJson():
    global mapids, maps, mapsList
    try:
        mapsJson = openJson(mapsf)
    except:
        raise Exception(f"\n{cInput}{mapsf} {cException}\nDoes not exist!\n{cReset}")

    i = 0
    for k,v in mapsJson.items():
        #*Add the map name with its index.
        maps.append(k)
        mapids.append(v)
        mapsList += f"{cPrimary}{i}. {cSecondary}{k}\n"
        i += 1


#*=+=+=+=+=+ Enter File
def enterFile():
    fn = input(f"\n{cPrimary}Which file needs to be compiled?\n>>> {cInput}")

    try:
        f = open(f"{Path(__file__).parent}\\py\\{fn}.py", "rt")
        print(f"\n{cPrimary}Compiling {cInput}{fn}.py{cPrimary}")

    except KeyboardInterrupt:
        endProgram()

    except:
        print(f"{cException}file {cInput}{fn}{cException} does not exist{cReset}")
        f, fn = enterFile()

    finally:
        return f, fn


#*=+=+=+=+=+ Extract Contents
#* f => file
#* fb => file base
#* c => content
#* l => line
def extractContents(f):
    fc = openJson(vrJB)
    fb = open(Path(__file__).parent / "py" / addonf)

    for l in f:
        if not re.findall(r"vex_start", l):
            fc["textContent"] += l.rstrip("\n") + "\n"

    fc["textContent"] += "\n\n\n"

    for l in fb:
        fc["textContent"] += l.rstrip("\n") + "\n"
    fc["textContent"] = re.sub(r"\.vexcode", "vexcode", fc["textContent"])

    f.close()

    return fc


#*=+=+=+=+=+ Enter Number
def choseMap():
    try:
        id = int(input(mapsList + f"\n{cPrimary}Enter the Number!\n>>> {cInput}"))

    except KeyboardInterrupt:
        endProgram()

    except:
        print(f"{cException}mNot a Valid Number!{cPrimary}")
        id = choseMap()

    finally:
        return id


#*=+=+=+=+=+ Open Json files + load
openJson = lambda f: json.loads(open(Path(__file__).parent / "json" / f).read())


#*=+=+=+=+=+ End Program
def endProgram():
    print(f"\n\n{cPrimary}Bye!{cReset}\n")
    exit()


#*=+=+=+=+=+ Start
init()
