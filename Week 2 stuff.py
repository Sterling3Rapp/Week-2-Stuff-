import random

secret = random.randint(1,10)

for i in range(0,3):
    guess = int(input("Guess a number: "))
    if guess == secret:
        print("You Win!!")
        break
    else:
        print("You Lose! The number was actually ", secret)

