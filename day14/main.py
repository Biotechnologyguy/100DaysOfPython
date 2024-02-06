# Print logo

# Compare A : name, description from country
#  art of vs
#
# compare B : name, descripption from country

# Who has more followers? Type 'A' or 'B'

# if right, then You're right! Current Score : Score
# Proceed with above step until answer is wrong

# If wrong then==> Sorry, that's wrong. Final score : score


from art import logo, vs
from game_data import data
import random
print(logo)


def get_random_celeb():
    return random.choice(data)


user_is_correct = True
user_score = 0

while user_is_correct:
    celeb1 = get_random_celeb()
    celeb2 = get_random_celeb()
    print(f"Compare A: {celeb1["name"]}, a {celeb1["description"]}, from {celeb1["country"]}")
    print(vs)
    print(f"Compare B: {celeb2["name"]}, a {celeb2["description"]}, from {celeb2["country"]}")
    user_answer = input("Who has more followers? Type 'A' or 'B' : ")
    if user_answer.lower() == "a" and celeb1["follower_count"] > celeb2["follower_count"]:
        user_score += 1
        print(f"You're right! Current score : {user_score}")
    else:
        user_is_correct = False
        print(f"Sorry that's wrong. Final score: {user_score}")


