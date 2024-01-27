# creating function that prints 3 lines and accepts some input
def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")


greet()


# Here name is called parameter
def greet_with_name(name):
    print(f"Hello {name}")
    print("How do you do?")
    print("Isn't the weather nice today?")


# Here name is called argument
greet_with_name("Angela")
greet_with_name("Billie")


