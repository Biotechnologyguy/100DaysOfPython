from art import logo, vs
from game_data import data
import random
print(logo)


def get_random_celeb():
    return random.choice(data)


user_is_correct = True
user_score = 0
celeb1 = get_random_celeb()

while user_is_correct:
    celeb2 = get_random_celeb()
    print(f"Compare A: {celeb1["name"]}, a {celeb1["description"]}, from {celeb1["country"]}")
    print(vs)
    print(f"Compare B: {celeb2["name"]}, a {celeb2["description"]}, from {celeb2["country"]}")
    user_answer = input("Who has more followers? Type 'A' or 'B' : ")
    if user_answer.lower() == "a" and celeb1["follower_count"] > celeb2["follower_count"]:
        user_score += 1
        print(f"You're right! Current score : {user_score}")
    elif user_answer.lower() == "b" and celeb2["follower_count"] > celeb1["follower_count"]:
        user_score += 1
        celeb1 = celeb2
        print(f"You're right! Current score : {user_score}")
    else:
        user_is_correct = False
        print(f"Sorry that's wrong. Final score: {user_score}")


