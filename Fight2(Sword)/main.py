#Fight1 (Punch)
import random as r
oAttLev = 0
uHea = 0
oHea = 0
uBlock = 0
oBlock = 0
uDodge = 0
oDodge = 0
name = ""

def intro ():
    global oAttLev
    global uHea
    global oHea
    global name
    choiOpp = int(input("Who do you want to fight?:\n Bob(Easy)[1] Joe(Medium)[2] Jacob(Hard)[3] Special[4]\n"))
    if choiOpp == 1:
        oAttLev += 1
        name = "Bob"
    elif choiOpp == 2:
        oAttLev += 2
        name = "Joe"
    elif choiOpp == 3:
        oAttLev += 3
        name = "Jacob"
    elif choiOpp == 4:
        oAttLev += 3
        name = "Special"
    else:
        print("Incorrect, Try Again")
        intro()
    uHea = int(input("Your Health?: "))
    oHea = int(input("Opponent's Health?: "))
    fight()

def fight():
    global oAttLev
    global uHea
    global oHea
    global uBlock
    global oBlock
    global uDodge
    global oDodge
    while uHea > 0 and oHea > 0:
        print(f"\nYour Health: {uHea}")
        print(f"{name}'s Health: {oHea}")
        attO = r.randrange(0,4)
        attU = int(input("Punch(1) Kick(2) Block(3) Dodge(4) Wait(5) Give Up(6)\n"))
        uBlock = 0
        if uDodge == 0:
            uDodge = 0
            if attU == 1:
                if oDodge == 1:
                    print(f"{name} dodged your punch!")
                else:
                    oHea -= 1
                    print("You successfully punched")
            elif attU == 2:
                if oBlock == 1 or oDodge == 1:
                    print("Your kick failed!")
                else:
                    oHea -= 2
                    print("You successfully kicked!")
            elif attU == 3:
                uBlock = 1
                print("You take a block stance")
            elif attU == 4:
                uDodge = 1
                print("You prepare to dodge")
            elif attU == 5:
                print("You wait")
            elif attU == 6:
                uHea = 0
                break
            else:
                print("Incorrect, Try Again")
                fight()
        else:
            print("You are too tired")
            uDodge = 0
        
        oBlock = 0
        if oDodge == 0:
            oDodge = 0
            if attO == 0:
                if uDodge == 1:
                    print("You dodged his punch!")
                else:
                    uHea -= oAttLev
                    print(f"{name} successfully punched")
            elif attO == 1:
                if uBlock == 1 or uDodge == 1:
                    print(f"{name}'s kick failed!")
                else:
                    uHea -= oAttLev + 1
                    print(f"{name} successfully kicked!")
            elif attO == 2:
                oBlock = 1
                #print(f"{name} goes into a block stance")
            elif attO == 3:
                oDodge = 1
                #print(f"{name} prepares to dodge")
        else:
            oDodge = 0
            print(f"{name} is tired")
    if uHea <= 0:
        print("You Lost!")
    elif oHea <= 0:
        print(f"You beat {name}! You Won!")

intro()