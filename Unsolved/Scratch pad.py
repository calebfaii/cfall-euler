import random

val = random.randint(1,10)
guesses = 0

print "I'm thinking of a number between 1 and 10."

while True:

    x = int(raw_input("What's your guess?: "))
    if x ==val:
        guesses += 1
        print "CORRECT!"
        print "You got that in", guesses, "guesses."
        break
    if x != val:
        print "Try again."
        guesses += 1




