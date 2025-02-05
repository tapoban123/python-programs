def createDict(storageDict: dict[str, int], name: str):
    storageDict[name] = len(name)
    
namesDict = {}
while True:    
    name = input("Please Enter your name (Enter 0 to exit.): ")
    if name == "0":
        break
    
    createDict(namesDict, name)
    if len(namesDict.keys()) == 1:
        print(f"Dictionary = {namesDict}")
    else:        
        print(f"New Dictionary = {namesDict}")
    