import random
number = random.randint(0, 50)
chances = 5
attempts = 0 # number of attempts
print("\nWellcome to the Guess the number game\n")
print("-*-" * 30)
print("\nI'm thinking of a number between 0 and 50. You have 5 chances.\n")
while chances > 0:
    guess = int(input("\nTake a guess: "))
    if guess > number:
        print("It's lower")
        chances -= 1
        attempts += 1
        print("Chances: ", chances)
    elif guess < number:
        print("It's bigger")
        chances -= 1
        attempts += 1
        print("Chances: ", chances)
    else:
        print("You got it! It took you %d attempts" % (attempts + 1))
        break

# print("Better luck next time. The number was %d" % number)
print("\n")
print("-*-" * 30)