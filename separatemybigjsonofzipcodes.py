import json
import functools
import os
import scratchpad

baseString = 'null'
directory = r'C:\Users\14172\Downloads\all-zips\zip'

def separate(filename):
    with open(filename, "r") as read_file:
        bigFile = json.load(read_file)
    count=1
    for zipName in bigFile:
        percentageDone = count/len(bigFile)
        print(percentageDone)
        count = count + 1
        newFile = "individual_jsons_of_zips_and_neighbors/" + zipName
        with open(newFile, "w") as write_file:
            json.dump(bigFile[zipName], write_file)

def reorder (filename):
    with open(filename, "r") as read_file:
        file = json.load(read_file)
    #for thing in file:
     #   print(thing)
    #print('stop')
    global baseString
    baseString = directory + (filename[-9:])
    file = sorted(file, key=functools.cmp_to_key(cmp))
    with open(filename, "w") as write_file:
        json.dump(file, write_file)
    #for thing in file:
     #   print(thing)


def cmp(stringOne, stringTwo):
    fileOne = directory + stringOne
    fileTwo = directory + stringTwo
    baseFile = baseString
    baseFileCoords = scratchpad.StringToNumArray(scratchpad.GrabCoordinates(baseFile))
    fileOneCoords = scratchpad.StringToNumArray(scratchpad.GrabCoordinates(fileOne))
    fileTwoCoords = scratchpad.StringToNumArray(scratchpad.GrabCoordinates(fileTwo))
    numOne = scratchpad.CoordinateMath(baseFileCoords, fileOneCoords)
    numTwo = scratchpad.CoordinateMath(baseFileCoords, fileTwoCoords)
    return numOne - numTwo

count = 1
workingDir = r'C:\Users\14172\PycharmProjects\demoScraper\individual_jsons_of_zips_and_neighbors'
for file in os.listdir(workingDir):
    f = os.path.join(workingDir, file)
    reorder(f)
    percentageDone = count/33150
    print(percentageDone)
    count = count + 1