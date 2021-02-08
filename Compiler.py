import os, re
from json import load as __jsLoad__, dump as __jsSave__
from time import sleep

w = "{}"

# =+=+=+=+=+=<
#   ANSI color codes


class c:
    # Reset
    r = "\u001b[0m"
    # Primary
    p = "\u001b[32m"
    # Secondary
    s = "\u001b[0;33m"
    # Input
    i = "\u001b[36m"
    # Exception
    e = "\u001b[31m"


# =+=+=+=+=+=>

# =+=+=+=+=+=<
#   File Functions


class path:
    json = os.path.abspath("./json") + "\\"
    py = os.path.abspath("./py") + "\\"
    vr = os.path.abspath("./vrpython") + "\\"


def loadJson(fileName:str, path:str = path.json, extension:str = ".json") -> object:
    f = open(f"{path}{fileName}{extension}")
    json = __jsLoad__(f)
    f.close()
    return json


def saveJson(path:os.PathLike,fileName:str,json:dict) -> None:
    f = open(path + fileName, "wt")
    __jsSave__(json,f)
    f.close()


def getPythonFiles(l: list = []) -> list:
    for f in os.listdir(path.py):
        if f.endswith(".py") and f != "vexcode.py" and f != "Universal Threading.py":
            l.append(os.path.splitext(f)[0])
    return l


def getVRPythonFiles(l: list = []) -> list:
    for f in os.listdir(path.vr):
        if f.endswith(".vrpython") and f != "Universal Threading.vrpython":
            l.append(os.path.splitext(f)[0])
    return l


# =+=+=+=+=+=>

# =+=+=+=+=+=<
#   User Interaction


def enter(startText: str, list: list, finalText: str = None) -> str:
    rawInput = input(startText)
    try:
        uInput = int(rawInput)
        if uInput < 0:
            raise IndexError()
        string = list[uInput]

    except IndexError:
        print(f"{c.i}{rawInput} {c.e}is not a Valid Slection!{c.p}\nChose Again...")
        sleep(0.5)
        return enter(startText, list, finalText)

    except ValueError:
        print(f"{c.i}{rawInput} {c.e}Not a Valid Number!{c.p}\nChose Again...")
        sleep(0.5)
        return enter(startText, list, finalText)

    if finalText:
        print(finalText.format(string))
    return string


def enterFile(startText: str, List: list, finalText: str) -> str:
    fileName = enter(startText + f"\n{c.p}Chose a file! \n>>> {c.i}", List, finalText)
    if fileName == "All Files":
        return "All"

    try:
        f = open(f"{path.py}{fileName}.py")

    except FileNotFoundError:
        print(f"{c.e}File not found!{c.p}\nChose Again...")
        sleep(0.5)
        return enterFile(startText, List, finalText)

    f.close()
    return fileName


# =+=+=+=+=+=<
#   enter File in Terminal


def choseFile() -> object:

    # st -> Start Text
    startText = f"\n{c.p}Chose a file to compile!\n\n"

    # i -> index
    i = 0

    # l -> List
    list = getPythonFiles(["All Files"])

    for t in list:
        startText += f"{c.p}{i}. {c.s}{t}\n"
        i += 1

    return enterFile(startText, list, f"\n\n{c.p}Selected to Compile {c.i}{w}")


# =+=+=+=+=+=>

# =+=+=+=+=+=<
#   Chose Map


def choseMap(fileName: str = None) -> str:
    # st -> Start Text
    if fileName:
        startText = f"\n{c.p}Chose a Map for {c.i}{fileName}.py{c.p}!\n\n"
    else:
        startText = f"\n{c.p}Chose a Map!\n\n"
    i = 0
    list = [""]
    mapjson = loadJson("maps")
    for map in mapjson:
        i += 1
        startText += f"{c.p}{i}. {c.s}{map}\n"
        list.append(map)

    return mapjson[
        enter(
            startText + f"\n{c.p}Chose a Map! \n>>> {c.i}",
            list,
            f"\n\n{c.p}Selected Map: {c.i}{w}",
        )
    ]


# =+=+=+=+=+=>

# =+=+=+=+=+=<
#   Compiling Function


def start():
    fileName = choseFile()

    print("\n\n")

    if fileName == "All":
        # for file in os.listdir(path.py):
        files = getPythonFiles()
        for t in files:
            compile(t)
        return

    # map -> Map Chosen
    compile(fileName, choseMap(fileName))


def compile(fileName:str, map:str=None) -> None:
    try:
        json = loadJson(fileName,path.vr,".vrpython")

    except FileNotFoundError:
        json = loadJson("vrpython")

    if not json["playground"] and not map:
        json["playground"] = choseMap(fileName)

    elif map:
        json["playground"] = map

    json["textContent"] = extractContents(fileName)

    saveJson(path.vr,fileName + ".vrpython", json)

    print(f"{c.p}Compiled {c.i}{fileName}.py{c.p} to {c.i}{fileName}.vrpython{c.p}!{c.r}")


def extractContents(fileName: str) -> str:
    file = open(f"{path.py}{fileName}.py")
    fileContent = ""

    for line in file:
        if not re.findall(r"vex_start", line):
            fileContent += line.rstrip("\n") + "\n"

    fileContent += "\n\n\n"

    for line in open(f"{path.py}Universal Threading.py"):
        fileContent += line.rstrip("\n") + "\n"

    file.close()

    return fileContent


# =+=+=+=+=+=>

# =+=+=+=+=+=<
#   End Program


def endProgram():
    print(f"{c.e}Keyboard Interruption!{c.p}\n\n\n\nBye!{c.r}\n\n")
    exit()


# =+=+=+=+=+=>


try:
    start()

except KeyboardInterrupt:
    endProgram()