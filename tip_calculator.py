print("Welcome to tip calculator.")
bill = int(input("What is the amount of bill: "))
tip = int(input("How much bill do you want to give in percent: "))
total = bill + (bill * tip / 100)
person = int(input("How many person's are you: "))
amount_per_person = round(total / person, 2)
print(f"Each person give: {amount_per_person}")
