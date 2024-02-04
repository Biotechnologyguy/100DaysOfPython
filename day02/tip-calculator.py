print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percent = float(input("What percentage tip would you like to give? 12, 10 or 15? "))
no_of_people = int(input("How many people to split the bill? "))
tip_amount = total_bill * (tip_percent / 100)
total_bill_with_tip = total_bill + tip_amount
per_person_bill = round(total_bill_with_tip / no_of_people, 2)
print(f"Each person should pay ${per_person_bill}")
