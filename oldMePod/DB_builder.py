#!/usr/bin/env python
import os
import sys
from ast import literal_eval

path = os.getcwd()
system = sys.platform


def auto_file():
    autoFile = input("enter file path: ").upper()
    check = autoFile
    workingFile = open(check, "r")
    str1 = workingFile.read()
    return str1


def max_text_to_dict():
    file1 = auto_file()
    tool = input("tool name: ").upper()
    list1 = file1.split(tool)
    autoDict = {}

    for x in list1:
        key = x.split(" ")[1:2:]
        sKey = ""
        value1 = x.split(" ")[2:3]
        sValue1 = ""
        value2 = x.split(" ")[3:]
        sValue2 = ""
        for x in key:
            sKey += x
        for x in value1:
            sValue1 += x
        for x in value2:
            sValue2 += x + " "
        autoDict[sKey] = sValue1, sValue2
        check = tool.replace('/', ':')
        print1 = open(check + ".txt", "w")
        print1.write(str(autoDict))

        # grabs tool manufacture name and jumps down to next function


def tool_brand():
    return tool_model(input("enter tool brand: ").upper())

# grabs tool madel and checks directory if exhists, makes file and path and jumps down


def tool_model(brandPath):
    toolModel = input("Enter tool model: ").upper()
    dir1 = brandPath
    check = toolModel.replace('/', ':')
    if not os.path.exists(path + "/" + "TOOL_DATABASE" + "/" + dir1):
        os.mkdir(path + "/" + "TOOL_DATABASE" + "/" + dir1)
        file1 = os.path.join(path + "/" + "TOOL_DATABASE" +
                             "/" + dir1, check + ".txt")
    else:
        file1 = os.path.join(path + "/" + "TOOL_DATABASE" +
                             "/" + dir1, check + ".txt")
    return file1

# decides if the file info is there or not and makes its


def tool_info():
    finalPath = tool_brand()
    # if the file doesnt exist
    if os.path.isfile(finalPath) == False:
        toolFile = open(finalPath, "w")
        toolDict = {}

        while 0 == 0:
            print("TYPE ( exit ) WHEN DONE!!")
            key = input("schematic #: ").upper()
            if key == "EXIT":
                break
            else:
                value1 = input("part #: ").upper()
                value2 = input("description: ").upper()
                toolDict[key] = value1, value2
        breakpoint

        toolFile.write(str(toolDict))
        print("complete")
        exit()
    else:
        toolFile = open(finalPath, "r")
        oldDict = toolFile.read()
        newDict = {}

        while 0 == 0:
            print("TYPE ( exit ) WHEN DONE!!")
            key = input("schematic #: ")
            if key == "exit":
                break
            else:
                value1 = input("part #: ")
                value2 = input("description: ")
                newDict[key] = value1, value2
        breakpoint

        strToDict = literal_eval(oldDict)
        finalDict = {**strToDict, **newDict}
        toolFile = open(finalPath, "w")
        toolFile.write(str(finalDict))
        print("complete")
        exit()


def select_method():
    method = input("type file or manual: ").upper()
    if method == "FILE":
        brand = input("BRAND: ").upper()
        if brand == "MAX":
            max_text_to_dict()
    elif method == "MANUAL":
        tool_info()
    else:
        print("not an option")
    exit()
    return 0


select_method()
