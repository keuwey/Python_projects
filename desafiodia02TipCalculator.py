print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? "))
percentage = int(input("What percentage tip would you like to give? 10,  12, or 15? "))
people = int(input("How many people to split the bill? "))
if percentage == 10:
    tip = (percentage / 100) * total_bill
    final_tip = (total_bill + tip) / people
    print(f"Each person should pay: ${final_tip:.2f}")
elif percentage == 12:
    tip = (percentage / 100) * total_bill
    final_tip = (total_bill + tip) / people
    print(f"Each person should pay: ${final_tip:.2f}")
elif percentage == 15:
    tip = (percentage / 100) * total_bill
    final_tip = (total_bill + tip) / people
    print(f"Each person should pay: ${final_tip:.2f}")
else:
    print("Choose an stated value")
