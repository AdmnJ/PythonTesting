#!/usr/bin/env
# We were told to make a list variable of teams, not a big sports person but here we go.
teamlist = ["Kansas","Missouri", "Oklahoma", "Nevada"]
print(teamlist)
for x in teamlist:
    print(x)
# Guess Random Number
import random
x = int(random.randint(1,5))
while True:
    guess = int(input("Guess Number between 1-5: "))
    if guess == x:
        print("Correct Random Integer was: ", x)
        break
    else:
        print("Try again")
# Next

