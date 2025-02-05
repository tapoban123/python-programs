def swapKeysAndValues(dictData: dict):
    newDict = {}
    for key in dictData.keys():
        newDict[dictData[key]] = key

    return newDict


dictData = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday",
}

print(swapKeysAndValues(dictData=dictData))
