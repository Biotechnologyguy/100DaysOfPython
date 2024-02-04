programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# How to access elements from dictionary
print(programming_dictionary["Bug"])

# adding new elements to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

# How to create empty dictionary
empty_dictionary = {}

# Edit an item in dictionary
programming_dictionary["Bug"] = ("An error in a program that prevents the program from running as expected "
                                 "and makes you cry.")

# loop through dictionary
for key in programming_dictionary:
    print(key, ":", programming_dictionary[key])
