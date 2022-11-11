# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.

from random import randint

n = randint(1, 10)
tries = 5

while tries > 0:
    guess = int(input("Guess my number: "))
    tries -= 1
    if guess == n:
        print("you win!!!")
        break
print("Game over!")
    