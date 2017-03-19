import random

print("hello, what's your name?")
name = input()

upperlimit = 50
number = random.randint(1,upperlimit)
print("well, " + name + ", I'm thinking of a number between 1 and " + str(upperlimit) + ".")

for guessesTaken in range(6):
    print("take a guess.")
    guess = input()
    guess = int(guess)

    if guess > number:
        print("your guess is to high.")

    if guess < number:
        print("your guess is too low.")

    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print("great! " + name + ", you guessed my number " + str(number) + " in " + guessesTaken + " guesses.")

if guess != number:
    print("sorry, no luck this time. the number was " + str(number))