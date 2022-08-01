print('''Welome to the treasure island
Your mission is to find the treasure''')
where = input('You are at a cross road. Where do you want to go? Type "left" or "right": ').lower()
if where == 'right':
    print("You fell into a hole. Game over")
else:
    lake = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. '
                 'Type "swim" to swim across: ').lower()
    if lake == 'swim':
        print("You got attacked by crocodiles. Game over")
    else:
        door = input("You arrive at the island unharmed. There is a house with three doors. One red, one yellow and "
                     "one blue. Which color do you choose? ").lower()
        if door == 'red':
            print("You got burned by fire. Game over")
        elif door == 'blue':
            print("You got eaten by beasts. Game over")
        else:
            print("You found the treasure. You win!")