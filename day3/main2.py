print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
total_bill = 0
if height > 120:
    print("You can ride rollercoaster!!")
    age = int(input("What is your age?"))
    if age < 12:
        total_bill += 5
    elif age < 18:
        total_bill += 7
    elif 18 <= age < 45:
        total_bill += 12
    else:
        print("Everything is going to be ok. Have a free ride on us!!")
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        total_bill += 3
    print(f"Your total bill is ${total_bill}")
else:
    print("You can't ride rollercoaster")

