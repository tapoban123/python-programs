def addKey(storage: dict, val: dict):
    newKey =list(val.keys())[0] 
    storage[newKey] = val[newKey]


def removeKey(storage: dict, key: str):
    storage.pop(key)


def displayKeys(storage: dict):
    return list(storage.keys())


def displayValues(storage: dict):
    return list(storage.values())


def searchKey(storage: dict, key: str):
    val = storage.get(key)
    if val == None:
        return False
    return val


def menu():
    print("Enter 1 to add a key.")
    print("Enter 2 to remove a key.")
    print("Enter 3 to display all keys.")
    print("Enter 4 to display all values.")
    print("Enter 5 to search a key.")
    print("Enter 0 to exit.")


storageDict = {}

while True:
    menu()
    userChoice = int(input("Enter your choice: "))
    if userChoice == 1:
        key = input("Enter key: ")
        value = input("Enter value: ")
        addKey(storageDict, {key: value})

    elif userChoice == 2:
        key = input("Enter key: ")
        removeKey(storageDict, key)

    elif userChoice == 3:
        print(displayKeys(storageDict))

    elif userChoice == 4:
        print(displayValues(storageDict))

    elif userChoice == 5:
        key = input("Enter the key you want to search: ")
        foundValue = searchKey(storageDict, key)

        if foundValue == False:
            print("Key not found.")
        else:
            print(foundValue)

    elif userChoice == 0:
        print("Program Executed Successfully.")
        break
    else:
        print("Invalid choice.")
        break
