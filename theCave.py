import time
import random

def printIntro():
    print("you are in a land full of dragons."
          "in front of you, you see two caves."
          "in one cave, the dragon is friendly and"
          "will share his treasure with you. the other"
          "dragon is greedy and hungry and will eat you."
          "")
    print()

def chooseCave():
    cave = ""
    while cave != "1" and cave != "2":
        print("which cave will you go into? 1 or 2?")
        cave = input()
    return cave

def checkChosenCave(theCave):
    print("you approach the cave")
    time.sleep(2)
    print("it's dark and spooky...")
    time.sleep(2)
    print("you can hardly see in here.")
    time.sleep(1)
    print("it's getting hotter.", end="")
    time.sleep(1)
    print(".", end="")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("now you can really feel the heat!")
    time.sleep(1)
    print("a large draggon jums out in front of you, opens his jaws and ")
    print()
    time.sleep(1)

    friendlyCave = random.randint(1,2)

    if theCave == str(friendlyCave):
        print("shares his treasure with you.")
    else:
        print("gobbles you down in one bite.")

playAgain = "y"
while playAgain == "y" or playAgain == "yes":
    printIntro()
    checkChosenCave(chooseCave())

    print("do you want to play again? yes or no?")
    playAgain = input()