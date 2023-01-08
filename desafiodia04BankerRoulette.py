# import random
#
# names_string = input()
# names = names_string.split(", ")
# payer = random.randint(0, len(names)-1)
# if payer == 0:
#     print(f"{names[0]} is going to buy the meal today")
# elif payer == 1:
#     print(f"{names[1]} is going to buy the meal today")
# elif payer == 2:
#     print(f"{names[2]} is going to buy the meal today")
# elif payer == 3:
#     print(f"{names[3]} is going to buy the meal today")
# else:
#     print(f"{names[4]} is going to buy the meal today")
#

import random

names_string = input()
names = names_string.split(", ")
random_choice = random.randint(0, len(names)-1)
payer = names[random_choice]
print(payer + " is going to buy the meal today")
