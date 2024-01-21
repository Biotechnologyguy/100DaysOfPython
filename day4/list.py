states_of_america = ["Delaware", "Pennsylvania", "Florida", "Texas"]
# stores data in order

# Get the values from list
print(states_of_america[1])

# -1 is the index of last element
print(states_of_america[-1])

states_of_america[1] = "Pencilvania"
print(states_of_america)

# Appending to last
states_of_america.append("Angelaland")
print(states_of_america)

# extend
states_of_america.extend(["Colorado", "Utah"])
print(states_of_america)

# IndexError
# print(states_of_america[111])

# Nested Lists
# dirty_dozen = [
# #     "Strawberries", "Spinach", "Kale", "Nectarines", "Apples",
# #     "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes",
# #     "Celery", "Potatoes"
# # ]

fruits = ['Strawberries', 'Nectarines', 'Apples', 'Grapes', 'Peaches', 'Cherries', 'Pears']

vegetables = ['Spinach', 'Kale', 'Tomatoes', 'Celery', 'Potatoes']

dirty_dozens = [fruits, vegetables]

print(dirty_dozens)