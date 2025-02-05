def mergeDict(dict1: dict, dict2: dict):
    newDict = dict1
    key2 =""
    for key in dict2.keys():
        if key in list(dict1.keys()):
            key2 += key + str(list(newDict.keys()).count(key) + 1)
            newDict[key2] = dict2[key]
        else:
            newDict[key] = dict2[key]

        
    return newDict


dict1 = {
    "Name": "Tapoban Ray",
    "Stream": "CSE",
    "Age": 19,
}

dict2 = {
    "Name": "John",
    "Year": "2025",
    "Sem": "4th",
}

print(mergeDict(dict1=dict1, dict2=dict2))
