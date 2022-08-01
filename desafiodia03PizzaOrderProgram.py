print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L ")
pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

if size.lower() == 's':
    if pepperoni.lower() == 'y':
        if extra_cheese.lower() == 'y':
            bill = 18
        else:
            bill = 17
    else:
        bill = 15
elif size.lower() == 'm':
    if pepperoni.lower() == 'y':
        if extra_cheese.lower() == 'y':
            bill = 24
        else:
            bill = 23
    else:
        bill = 20
elif size.lower() == 'l':
    if pepperoni.lower() == 'y':
        if extra_cheese.lower() == 'y':
            bill = 29
        else:
            bill = 28
    else:
        bill = 25
else:
    print("Please, enter a valid letter")
print("Your final bill is: $%d" % bill)
