# I'm putting this here so that Luke remembers that this is where we can test out code we don't want to test out in his assignments folder hehe :)

import random as r
subPoints = 0
score = 0

def mainChoice(score):
    mChoice = int(input("What do you want to do with Gorgeia?\n  1. Talk with her\n  2. Do things with her\n  3. Go places with her\n  4. Adventure\n  5. Leave her\n  6. Score\n"))
    if mChoice == 1:
        talk(score, subPoints)
    elif mChoice == 2:
        do(score)
    elif mChoice == 3:
        go(score)
    elif mChoice == 4:
        advent(score)    
    elif mChoice == 5:
        score = str(score)
        print("Your score is " + score + "\nBye!")
    elif mChoice == 6:
        score = str(score)
        print("Your score is " + score)
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
    talk_len = int(input("Gorgeia is constantly changing her emotions.\n How many questions do you want to ask?:\n"))
    len = 0

    while len != talk_len:
        random = r.randrange(0,3)
        death = r.randrange(0,10)

        choiceAsk = int(input("Ask Gorgeia if she's tired(1), hungry(2), bored(3), or sad(4)? Leave(5): "))
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
            talk(score)
        else:
            print("Incorrect") 
            ask(score)
        print("Gorgeia is", mood)
        if death == 5:
            print("Gorgeia died")
            score -= 20
            len = talk_len - 1  
        len += 1
    talk(score, subPoints)

def sub(score, subPoints):
    if subPoints > 2:
        score -= 1
        print("Gorgeia doesn't want to talk anymore about subjects")
        talk(score, subPoints)
    else:
        subPoints += 1
        choiceSub = int(input("What Subject? School(1) Family(2) Food(3) Movies(4) Games(5) Leave(6):\n"))
        if choiceSub == 1:
            score -= 5
            print("Gorgeia doesn't like school at all because she couldn't get past preschool.")
            sub(score, subPoints)
        elif choiceSub == 2:
            score += 2
            print("Gorgeia has 1,000 siblings. She likes most of them")
            sub(score, subPoints)
        elif choiceSub == 3:
            score += 3
            print("Gorgeia LOVES food!")
            sub(score, subPoints)
        elif choiceSub == 4:
            score += 2
            print("Georgia loves watching movies at movie theaters")
            sub(score, subPoints)
        elif choiceSub == 5:
            score += 1
            print("Gorgeia is fine with games")
            sub(score, subPoints)
        elif choiceSub == 6:
            talk(score, subPoints)
        else:
            print("Incorrect") 
            sub(score, subPoints)

def poli(score):
    score -= 100000000
    print("Gorgeia and you get into a heated debate where you both end up unsatisfied. You and her hate politics.")
    talk(score, subPoints)


def do(score):

    choiceDo = int(input("What do you want to do?\n Eat Food(1) Play a Game(2) Read a book(3) Fight(4) Leave(5):\n"))
    #Eat Food
    if choiceDo == 1:
        food(score)
    elif choiceDo == 2:
        game(score)
    elif choiceDo == 3:
        #book(score)
        pass
    elif choiceDo == 4:
        #fight(score)
        pass
    elif choiceDo == 5:
        mainChoice(score)
    else:
        print("Incorrect") 
        do(score)

def food(score):
    choicePizza = int(input("Which food do you want?\n Domino's Pizza(1) Little Caesar's Pizza(2) Frezzer Pizza(3) Homemade Pizza(4):\n"))
    if choicePizza == 1 or 2:
        pay = int(input("Do you pay?: "))

def game(score):
    do_len = int(input("How many games?: "))
    len = 0
    pokePoints = 0

    while len != do_len:
        random = r.randrange(3)
        choiceGame = int(input("Which game do you want to play?\n Monopoly(1) Chess(2) MarioKart(3) Pokemon(4) Leave(5):\n"))

        #Competitive Game
        if choiceGame == 1 | 2 | 3:
            if random == 1:
                score += 1
                print("You won!")
            elif random == 2:
                print("It was a draw! Not too fun or too boring")
            else:
                score -= 1
                print("Oh no! You lost!")
        #Pokemon Playing points 
        elif choiceGame == 4:
            score += 1
            pokePoints += 1
            print("You had a fun time playing Pokemon with your friend")
            if pokePoints >= 7:
                score -= 12
                print("You and Gorgeia almost died of boredom")
            elif pokePoints >= 5:
                print("You are getting bored")
        elif choiceGame == 5:
            do(score)
            len = do_len -1
        else:
            print("Incorrect") 
            game(score)
        len += 1
    do(score)


def go(score):
    choiceGo = int(input("Where do you want to go?\n (1) (2) (3) (4) (5):\n"))
    if choiceGo == 1:
        (score)
    elif choiceGo == 2:
        (score)
    elif choiceGo == 3:
        (score)
    elif choiceGo == 4:
        (score)
    elif choiceGo == 5:
        mainChoice(score)
    else:
        print("Incorrect") 
        go(score)


def advent(score):
    choiceAdvent = int(input("Which adventure do you want to go on?\n (1) (2) (3) (4) (5):\n"))
    if choiceAdvent == 1:
        (score)
    elif choiceAdvent == 2:
        (score)
    elif choiceAdvent == 3:
        (score)
    elif choiceAdvent == 4:
        (score)
    elif choiceAdvent == 5:
        mainChoice(score)
    else:
        print("Incorrect") 
        advent(score)

mainChoice(score)

#choice = int(input("Which one do you?\n (1) (2) (3) (4) (5):\n"))

#if == 1:
        #print()