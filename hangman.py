import random

galgen = """
 /------\\
  |
  |
  |
  |
  |
/TTT\\
"""

dead = """
 /------\\
  |     |
  |     0
  |    /|\\
  |    / \\
  |
/TTT\\
"""

alive1 = """
 /------\\
  |     |
  |
  |
  |
  |
/TTT\\
"""

alive2 = """
 /------\\
  |     |
  |     O
  |
  |
  |
/TTT\\
"""

alive3 = """
 /------\\
  |     |
  |     O
  |     |
  |
  |
/TTT\\
"""

alive4 = """
 /------\\
  |     |
  |     O
  |    /|
  |
  |
/TTT\\
"""

alive5 = """
 /------\\
  |     |
  |     O
  |    /|\\
  |
  |
/TTT\\
"""

alive6 = """
 /------\\
  |     |
  |     O
  |    /|\\
  |    /
  |
/TTT\\
"""

rip = """
    -------
    |     |
  ---     ---
  |  R.I.P  |
  ---     ---
    |     |
    |     |
    |     |
    -------
"""

wordList = ["hello world",
            "dragon",
            "raspberry",
            "hangman",
            "what ever",
            "toothpaste",
            "big ben",
            "pi"]


def getNextWord():
    item = random.randint(1, len(wordList))
    return wordList[item]


def getUnguessed(word):
    unguessed = 0
    for ch in word:
        if guessedLetters.find(ch) == -1:
            if ch != " ":
                unguessed += 1
    return unguessed


def showWord():
    hiddenWord = searchedWord
    for ch in hiddenWord:
        if guessedLetters.find(ch) != -1:
            print(ch, end="")
        else:
            if ch == " ":
                print(" ", end="")
            else:
                print("_", end="")
    print()


guessedLetters = ""
searchedWord = getNextWord()
unguessed = len(searchedWord)

print("you're about to get hanged. if you can solve the puzzle you will live.")
print("i have a chosen a word, you have to guess letters")
print("each time you choose a letter that is not in the word you're a step closer to your hanging.")

currentState = galgen
while currentState != dead:
    print(currentState)
    showWord()
    print()
    print("your choice: ", end="")
    letter = input()
    if guessedLetters.find(letter) != -1:
        print("you already guessed this one: " + letter)
        continue
    guessedLetters += letter
    # print("you selected " + letter)
    unguessed = getUnguessed(searchedWord)
    # print(str(unguessed))
    if searchedWord.find(letter) == -1:
        print("\n\n\n\n\n\n\n\n\n")
        print("the letter " + letter + " is not in the word\n")
        if currentState == galgen:
            currentState = alive1
        elif currentState == alive1:
            currentState = alive2
        elif currentState == alive2:
            currentState = alive3
        elif currentState == alive3:
            currentState = alive4
        elif currentState == alive4:
            currentState = alive5
        elif currentState == alive5:
            currentState = alive6
        elif currentState == alive6:
            currentState = dead

    if unguessed > 0:
        continue

    if unguessed == 0:
        break

if unguessed == 0:
    print("you made it!")
    print("the word was " + searchedWord.upper())

if unguessed > 0:
    print("sorry, no luck. the word was " + searchedWord.upper())
    print("you died.")
    print(dead)
    print(rip)