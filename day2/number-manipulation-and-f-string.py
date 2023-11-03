
print(8 / 3)

# Way 1 : Make it int, but it will not round number. It will chop everything after decimal
print(int(8 / 3))

# Way 2 : Floor division using // operator. result is same like above.
print(8 // 3)

# way 3 : round() function
print(round(8 / 3, 3))\

score = 9

# Everytime user scores :
score += 1
score /= 2


# When to use f string
print("The score is ", str(score))
# Now we can use f string
iswinning = True
print(f"The score is {score} and iswinning = {iswinning}")


