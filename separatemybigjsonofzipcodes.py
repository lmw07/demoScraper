import json

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

separate("zipmapFinal.json")