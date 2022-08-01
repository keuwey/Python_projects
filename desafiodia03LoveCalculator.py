print("Welcome to the love calculator!")
name1 = input("What is your name: ").lower()
name2 = input("What is their name: ").lower()
nomes = name1 + name2
t = nomes.count("t")
r = nomes.count("r")
u = nomes.count("u")
e = nomes.count("e")
true = t + r + u + e

l = nomes.count("l")
o = nomes.count("o")
v = nomes.count("v")
e = nomes.count("e")
love = l + o + v + e

love_score = int(str(true) + str(love))
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")
