import random

roll = random.randint(1,6)
guess = int(input('Guess the dice roll:\n'))

#print("The computer rolled a " + str(roll))

if guess == roll:
    print("You guessed right. They rolled a " + str(roll))
else:
    print("You guessed wrong. They rolled a " + str(roll))