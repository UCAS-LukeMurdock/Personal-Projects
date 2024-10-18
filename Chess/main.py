#Chess
"""
_|__|_
_|__|_
 |  |
"""
import random as r
randomR = r.randrange(0,10)

startMap = """
1_|_2_|_3
4_|_5_|_6
7 | 8 | 9
"""

def intro():
    randomC = r.randrange(0,2)
    choice = int(input("Do you want to be X(1), O(2), or Random(3)?:"))
    if choice == 3:
        if randomC == 1:
            uToken = "X"
        elif randomC == 0:
            uToken = "O"
    elif choice == 1:
        uToken = "X"
    elif choice == 2:
        uToken = "O"
    
    return uToken

def cIntro(userToken):
    if userToken == "X":
        compToken = "O"
    elif userToken == "O":
        compToken = "X"
    return compToken
    
def uAction(currentMap, userToken):
    choiceA = int(input("Where do you want to place your token?: "))
    if choiceA == 1:
        aMap = action1(currentMap,userToken)
    elif choiceA == 2:
        aMap = action2(currentMap, userToken)
    elif choiceA == 3:
        aMap = action3(currentMap, userToken)
    elif choiceA == 4:
        aMap = action4(currentMap, userToken)
    elif choiceA == 5:
        aMap = action5(currentMap, userToken)
    elif choiceA == 6:
        aMap = action6(currentMap, userToken)
    elif choiceA == 7:
        aMap = action7(currentMap, userToken)
    elif choiceA == 8:
        aMap = action8(currentMap, userToken)
    elif choiceA == 9:
        aMap = action9(currentMap, userToken)
    else:
        print("Incorrect")
        uAction()
    return aMap

def cAction(currentMap, cToken):
    randomR = r.randrange(0,10)
    if randomR == 1:
        return action1(currentMap, cToken)
    elif randomR == 2:
        return action2(currentMap, cToken)
    elif randomR == 3:
        return action3(currentMap, cToken)
    elif randomR == 4:
        return action4(currentMap, cToken)
    elif randomR == 5:
        return action5(currentMap, cToken)
    elif randomR == 6:
        return action6(currentMap, cToken)
    elif randomR == 7:
        return action7(currentMap, cToken)
    elif randomR == 8:
        return action8(currentMap, cToken)
    elif randomR == 9:
        return action9(currentMap, cToken)

def action1(currentMap, Token):
    return currentMap.replace("1", Token)
def action2(currentMap, Token):
    return currentMap.replace("2", Token)
def action3(currentMap, Token):
    zMap = currentMap.replace("3", Token)
    return zMap
def action4(currentMap, Token):
    currentMap = currentMap.replace("4", Token)
    return currentMap
def action5(currentMap, Token):
    currentMap = currentMap.replace("5", Token)
    return currentMap
def action6(currentMap, Token):
    currentMap = currentMap.replace("6", Token)
    return currentMap
def action7(currentMap, Token):
    currentMap = currentMap.replace("7", Token)
    return currentMap
def action8(currentMap, Token):
    currentMap = currentMap.replace("8", Token)
    return currentMap
def action9(currentMap, Token):
    currentMap = currentMap.replace("9", Token)
    return currentMap

def game(userToken, cToken):
    if userToken == "X":
        map1 = uAction(startMap, userToken)
        print(map1)
        map2 = cAction(map1, cToken)
        print(map2)
        map3 = uAction(map2, userToken)
        print(map3)
        map4 = cAction(map3, cToken)
        print(map4)
        map5 = uAction(map4, userToken)
        print(map5)
        map6 = cAction(map5, cToken)
        print(map6)
        map7 = uAction(map6, userToken)
        print(map7)
        map8 = cAction(map7, cToken)
        print(map8)
        map9 = uAction(map8, userToken)
        print(map9)
    elif userToken == "O":
        map1 = cAction(startMap, cToken)
        print(map1)
        map2 = uAction(map1, userToken)
        print(map2)
        map3 = cAction(map2, cToken)
        print(map3)
        map4 = uAction(map3, userToken)
        print(map4)
        map5 = cAction(map4, cToken)
        print(map5)
        map6 = uAction(map5, userToken)
        print(map6)
        map7 = cAction(map6, cToken)
        print(map7)
        map8 = uAction(map7, userToken)
        print(map8)
        map9 = cAction(map8, cToken)
        print(map9)
print(startMap)
userToken = intro()
print(userToken)
cToken = cIntro(userToken)
print(cToken)
game(userToken, cToken)
