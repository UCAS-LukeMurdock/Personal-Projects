# I'm putting this here so that Luke remembers that this is where we can test out code we don't want to test out in his assignments folder hehe :)

import random as r
subPoints = 0
score = 0
full = 0
name = input("What is your friend's name?:")

def mainChoice(score):
    mChoice = int(input(f"\nWhat do you want to do with {name}?\n  1. Talk with them\n  2. Do things with them\n  3. Go places with them\n  4. Adventure\n  5. Leave them\n  6. Score\n"))
    if mChoice == 1:
        talk(score, subPoints)
    elif mChoice == 2:
        do(score)
    elif mChoice == 3:
        go(score)
    elif mChoice == 4:
        advent(score)    
    elif mChoice == 5:
        print("Your score is " + str(score) + "\nBye!")
    elif mChoice == 6:
        print("Your score is " + str(score))
        mainChoice(score)
    else:
        print("Incorrect")
        mainChoice(score)


def talk(score, subPoints):
    choiceTalk = int(input("Which type of talking?:\n Questions(1) Subjects(2) Politics(3) Leave(4)\n"))
    if choiceTalk == 1:
        ask(score)
    elif choiceTalk == 2:
        sub(score, subPoints)
    elif choiceTalk == 3:
        poli(score)
    elif choiceTalk == 4:
        mainChoice(score)
    else:
        print("Incorrect") 
        talk(score, subPoints)

def ask(score):
    talk_len = int(input(f"{name} is constantly changing their emotions.\n How many questions do you want to ask?:\n"))
    len = 0

    while len != talk_len:
        random = r.randrange(0,3)
        death = r.randrange(0,10)

        choiceAsk = int(input(f"Ask {name} if they're tired(1), hungry(2), bored(3), or sad(4)? Leave(5): "))
        score += 1
        # Sleepiness Level
        if choiceAsk == 1:
            if random == 1:
                score += 2
                mood = "alert"
            elif random == 2:
                score += 1
                mood = "awake Hahaha"
            else:
                score -= 2
                mood = "fatigued"
         # Hunger Level
        elif choiceAsk == 2:
            if random == 1:
                score += 2
                mood = "full"
            elif random == 2:
                score += 1
                mood = "fine, Thanks for asking!"
            else:
                score -= 2
                mood = "starving"
        # Bored Level
        elif choiceAsk == 3:
            if random == 1:
                score += 2
                mood = "entertained"
            elif random == 2:
                score -= 1
                mood = "content"
            else:
                score -= 2
                mood = "bored"
        # Happy Level
        elif choiceAsk == 4:
            if random == 1:
                score += 2
                mood = "overjoyed"
            elif random == 2:
                score -= 1
                mood = "ok"
            else:
                score -= 2
                mood = "depressed"
        elif choiceAsk == 5:
            len = talk_len -1
            talk(score, subPoints)
        else:
            print("Incorrect") 
            ask(score)
        print(f"{name} is", mood)
        if death == 5:
            print(f"{name} died")
            score -= 20
            len = talk_len - 1  
        len += 1
    talk(score, subPoints)
def sub(score, subPoints):
    if subPoints > 2:
        score -= 1
        print(f"{name} doesn't want to talk anymore about subjects")
        talk(score, subPoints)
    else:
        choiceSub = int(input("What Subject? School(1) Family(2) Food(3) Movies(4) Games(5) Leave(6):\n"))
        if choiceSub == 1:
            subPoints += 1
            score -= 5
            print(f"{name} doesn't like school at all because they couldn't get past preschool.")
            sub(score, subPoints)
        elif choiceSub == 2:
            subPoints += 1
            score += 2
            print(f"{name} has 1,000 siblings. They like most of them")
            sub(score, subPoints)
        elif choiceSub == 3:
            subPoints += 1
            score += 3
            print(f"{name} LOVES food!")
            sub(score, subPoints)
        elif choiceSub == 4:
            subPoints += 1
            score += 2
            print(f"{name} loves watching movies at movie theaters")
            sub(score, subPoints)
        elif choiceSub == 5:
            subPoints += 1
            score += 1
            print(f"{name} is fine with games")
            sub(score, subPoints)
        elif choiceSub == 6:
            talk(score, subPoints)
        else:
            subPoints += 1
            print("Incorrect") 
            sub(score, subPoints)
def poli(score):
    score -= 100000000
    print(f"{name} and you get into a heated debate where you both end up unsatisfied. You and {name} hate politics.")
    talk(score, subPoints)


def do(score):

    choiceDo = int(input("What do you want to do?\n Eat Food(1) Play a Game(2) Read a book(3) Fight(4) Leave(5):\n"))
    #Eat Food
    if choiceDo == 1:
        food(score)
    elif choiceDo == 2:
        game(score)
    elif choiceDo == 3:
        score += 2
        print("You have a fun time reading a book!")
        do(score)
    elif choiceDo == 4:
        fight(score)
    elif choiceDo == 5:
        mainChoice(score)
    else:
        print("Incorrect") 
        do(score)

def food(score):
    choicePizza = int(input("Which food do you want?\n Domino's Pizza(1) Little Caesar's Pizza(2) Frezzer Pizza(3) Homemade Pizza(4):\n"))
    if choicePizza == 1:
        pay = int(input("Do you pay(1) or them(2)?: "))
        if pay == 1:
            score += 5
            score -= 7
        elif pay == 2:
            score += 1
            score -= 7
        print("The pizza looks super fresh!")
        pizzaEat(score)
        do(score)
    elif choicePizza == 2:
        pay = int(input("Do you pay(1) or them(2)?: "))
        if pay == 1:
            score += 3
            score -= 5
        elif pay == 2:
            score -= 5
        pizzaEat(score)
        do(score)
    elif choicePizza == 3 or choicePizza == 4:
        pizzaEat(score)
        do(score)
    else:
        print("Incorrect")
        food(score)
def pizzaEat(score):
    global full
    if full == 1:
        print(f"{name} is full.")
    else:
        print("You eat the yummy pizza!")
        score += 15
        full += 1

def game(score):
    do_len = int(input("How many games?: "))
    len = 0
    pokePoints = 0

    while len != do_len:
        choiceGame = int(input("Which game do you want to play?\n Monopoly(1) Chess(2) MarioKart(3) Pokemon(4) Leave(5):\n"))
            #Competitive Game
        if choiceGame == 1 or choiceGame == 2 or choiceGame == 3:
            competitive(score)

        #Pokemon Playing points 
        elif choiceGame == 4:
            score += 1
            pokePoints += 1
            print("You had a fun time playing Pokemon with your friend")
            if pokePoints >= 7:
                score -= 12
                print(f"You and {name} almost died of boredom")
            elif pokePoints >= 5:
                print("You are getting bored")
        elif choiceGame == 5:
            do(score)
            break
        else:
            print("Incorrect") 
            game(score)
        len += 1
    do(score)
def competitive(score):
    random = r.randrange(3)
    if random == 1:
        score += 1
        print("You won!")
    elif random == 2:
        print("It was a draw! Not too fun or too boring")
    else:
        score -= 1
        print("Oh no! You lost!")

def fight(score):
    friend = 0
    fBlock = 0
    while friend <= 20:
        block = 0
        rand = r.randrange(0,2)
        rand2 = r.randrange(0,3)
        hit = int(input("Punch(1) Kick(2) Dodge(3) Stop(4):"))
        if hit == 1:
            if fBlock == 1:
                print("You got blocked!")
            else:
                friend += 1
                print("You successfully punched")
        elif hit == 2:
            if fBlock == 1:
                print("You got blocked!")
            else:
                print("You successfully kicked")
                friend += 2
        elif hit == 3:
            block = 1
        elif hit == 4:
            break
        fBlock = 0
        if rand == 0:
            print("Nothing happens")
        elif rand == 1:
            if block == 1:
                score += 2
                print("You successfully dodge!")
            else:
                if rand2 == 0:
                    score -= 1
                    print("You got punched!")
                elif rand2 == 1:
                    score -= 2
                    print("You got kicked!")
                elif rand2 == 2:
                    fBlock = 1
    if friend >= 20:
        print("You Won!")
    else:
        print("The fight ended")
    do(score)
                

    do(score)


def go(score):
    choiceGo = int(input("Where do you want to go?\n Movie Theater(1) Store(2) Woods(3) Space(4) Leave(5):\n"))
    if choiceGo == 1:
        movie(score)
    elif choiceGo == 2:
        store(score)
    elif choiceGo == 3:
        woods()
    elif choiceGo == 4:
        space(score)
    elif choiceGo == 5:
        mainChoice(score)
    else:
        print("Incorrect") 
        go(score)

def movie(score):
    score += 2
    print("You had a great time watching a movie about pizza")
    go(score)
def store(score):
    shopList = []
    len = 0
    shopLen = int(input("How many items do you want to buy?:"))
    score -= shopLen
    while len != shopLen:
        item = input("What do you want to buy?:")
        shopList.append(item)
        print(shopList)
        len += 1
    print(f"You had a fun time buying {shopList}")
    score += 5
    go(score)
def woods():
    print(f"You and {name} go into the woods and never come back...")
def space(score):
    score += 10000000
    print(f"You and {name} colonize a planet and become leaders of a grand government!")
    print(f"Your score is {score}")

def advent(score):
    choiceAdvent = int(input("Which adventure do you want to go on?\n Capital(1) Ocean(2) Tundra(3) Leave(4)\n"))
    if choiceAdvent == 1:
        advent1(score)
    elif choiceAdvent == 2:
        advent2(score)
    elif choiceAdvent == 3:
        advent3(score)
    elif choiceAdvent == 4:
        mainChoice(score)
    else:
        print("Incorrect") 
        advent(score)
def advent1(score):
    choiceA1 = int(input("The Capital of Auoruoa is located in the middle of a the gas planet, Aurua. The castle is the perfect sphere of the core. The gravity levels are high but somehow it is livable.\nWhat do you do?\n Seige The Castle(1) Sneak Into The Castle(2) Live a normal life in the Capitol(3) Leave(4) :\n"))
    
    if choiceA1 == 1:
        choiceA11 = int(input("Which one do you?\n Try to Break in Early(1) Try to Break in later(2) Wait Till They Give Up(3):\n"))
        if choiceA11 == 1:
            score -= -100
            print("Their trained forces destroy you")
        elif choiceA11 == 2:
            score += 20
            print("They are weak enough and so you win!")
        elif choiceA11 == 3:
            score -= 100
            print("You siege the castle for months on end. Eventually you run out of supplies on this forigen planet. You get destroyed by the Auorouaian King.")
        mainChoice(score)

    elif choiceA1 == 2:
        randomA12 = r.randrange(0,2)
        if randomA12 == 0:
            score -= -100
            print("You get caught!")
        elif randomA12 == 1:
            score += 20
            print("You take over the castle!")
        mainChoice(score)
    elif choiceA1 == 3:
        score += 20
        print("You live here in harmony")
        print(f"Your score is {score}")
    elif choiceA1 == 4:
        advent(score)
    else:
        print("Incorrect") 
        advent1(score)
def advent2(score):
    print("The Ocean is endless, omniprescent, and all consuming.")
    choiceA2 = int(input("Which one do you do?\n Sail as Far as You can(1) Sail along the coast(2) Fish(3) Leave(4):\n"))
    if choiceA2 == 1:
        choiceA21 = int(input("You meet a pirate ship. Fight(1) Join(2) Escape(3):\n"))
        if choiceA21 == 1:
            score -= -100
            print("They sink your ship")
            mainChoice(score)
        elif choiceA21 == 2:
            score += 20
            print("You join them and gain soom bounty")
            mainChoice(score)
        elif choiceA21 == 3:
            score -= 100
            print("You get lost in the endless ocean")
            print(f"Score: {score}")
    elif choiceA2 == 2:
        print("Nothing happens")
        mainChoice(score)
    elif choiceA2 == 3:
        score += 20
        print("You fish prosperily until the end of your days.")
        print(f"Your score is {score}")
    elif choiceA2 == 4:
        advent(score)
    else:
        print("Incorrect") 
        advent2(score)
def advent3(score):
    choiceA3 = int(input("Which one do you do?\n Journey to the Center(1) Make Camp(2) Split Up and Scout(3) Leave(4):\n"))
    if choiceA3 == 1 or choiceA3 == 2 or choiceA3 == 3:
        score -= 30
        print("You freeze")
        print(f"Score: {score}")
    elif choiceA3 == 4:
        advent(score)
    else:
        print("Incorrect") 
        advent3(score)

mainChoice(score)

if score >= 50:
    print("Great Job! Game Ended")
elif score >= -10:
    print("You did okay! Game Ended")
elif score < -10:
    print("Do better next time! Game Ended")

#choice = int(input("Which one do you?\n (1) (2) (3) (4) (5):\n"))

#if == 1:
        #print()