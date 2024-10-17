# I'm putting this here so that Luke remembers that this is where we can test out code we don't want to test out in his assignments folder hehe :)

import random as r
score = 0

def mainChoice():
    mChoice = int(input("What do you want to do with Gorgeia?\n  1. Ask her questions\n  2. Do things with her\n  3. Go places with her\n  4. \n  5. Leave her\n"))
    if mChoice == 1:
        questions(score)
    elif mChoice == 2:
        do(score)
    elif mChoice == 3:
        go(score)
    elif mChoice == 4:
        advent(score)    
    else:
        print("Your score is " + score + "\nBye!")

def questions(score):
    talk_len = int(input("Gorgeia is constantly changing her emotions.\n How long do you want to talk to her?:"))
    len = 0

    while len != talk_len:
        random = r.randrange(0,3)
        death = r.randrange(0,10)

        choiceAsk = int(input("Ask Gorgeia if she's tired(1), hungry(2), bored(3), or sad(4)?: "))
        score += 1
        # Sleepiness Level
        if choiceAsk == 1:
            if random == 1:
                score += 1
                mood = "alert"
            elif random == 2:
                mood = "awake"
            else:
                mood = "fatigued"
        # Hunger Level
        elif choiceAsk == 2:
            if random == 1:
                score += 1
                mood = "full"
            elif random == 2:
                mood = "fine"
            else:
                mood = "starving"
        # Bored Level
        elif choiceAsk == 3:
            if random == 1:
                score += 1
                mood = "entertained"
            elif random == 2:
                mood = "content"
            else:
                mood = "bored"
        # Happy Level
        elif choiceAsk == 4:
            if random == 1:
                score += 1
                mood = "overjoyed"
            elif random == 2:
                mood = "ok"
            else:
                mood = "depressed"
        else:
            print("Incorrect") 
            questions()
        print("Gorgeia is", mood)
        if death == 5:
            print("Gorgeia died")
            score -= 10
            len = talk_len - 1  
        len += 1
    print("")
    mainChoice()

def do(score):
    talk_len = int(input("How many games?: "))
    len = 0
    while len != talk_len:
        random = r.randrange(2)
        choiceDo = int(input("What do you want to do?\n Eat Food(1) Play a Game(2) Read a book(3) Fight(4):\n"))
        #Eat
        if choiceDo == 1:
            choice = int(input("Which game do you want to play?\n Monopoly(1) Chess(2) MarioKart(3) Pokemon(4):\n"))
            if choice == 1 or 2 or 3:
                if random == 1:
                    score += 1
                    print("You won!")
                else:
                    score -= 1
                    print("Oh no! You lost!")
            elif choice == 4:
                # Do this later!!!!!!!!!!!!!!!!!!!
                print("You had a fun time")

            
            
def go(score):
    choiceGo = int(input("Where do you want to go?\n (1) (2) (3) (4):\n"))
def advent(score):
    choiceAdvent = int(input("Which adventure do you want to go on?\n (1) (2) (3) (4):\n"))

mainChoice()

#choice = int(input("Which one do you?\n (1) (2) (3) (4):\n"))

#if == 1:
        #print()