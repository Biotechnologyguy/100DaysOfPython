class User:

    def __init__(self, user_id, username):
        print("New user is beeing created")
        self.id = user_id
        self.username = username
        self.followers = 0
    pass


user_1 = User(1, "Shubham")
user_2 = User(2, "Angela")

print(user_1)
print(user_2)
