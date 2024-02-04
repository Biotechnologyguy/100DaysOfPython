# ###########DEBUGGING#####################

# Describe Problem.
# Problem is 20 is not inclusive
# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("You got it")
#
#
# my_function()


# # Reproduce the Bug
# # Problem : list index starts from zero, so b will be 5 instead of 6. randint function consider both the end values
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# # Play Computer
# # for 1994, there is no condition. code fails on input of 1994. elif should contain >=
# year = int(input("What's your year of birth?"))
# if 1980 < year < 1994:
#     print("You are a millenial.")
# elif year > 1994:
#     print("You are a Gen Z.")

# # Fix the Errors
# # typecast input to int
# # use f string
# age = input("How old are you?")
# if age > 18:
#     print("You can drive at age {age}.")

# # Print is Your Friend
# # use single = for assignment
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# Use a Debugger
# Scope of new_item is concern here
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    b_list.append(new_item)
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])

