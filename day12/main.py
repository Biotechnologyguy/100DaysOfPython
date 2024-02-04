# ################## Scope ####################

enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# local scope
print("########## Local Scope ###########")


def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()
# print(potion_strength) #not available outside of function

# Global scope
print("########## Global Scope ###########")
player_health = 20


def player_strength():
    print(player_health)


player_strength()
# Also applies to the functions as well i.e. nested functions


# Python does not have block scope i.e. loops, conditiionals, etc
print("########## BLock Scope ###########")
level = 5
enemies = ["Skeleton", "Zombies", "Aliens"]
if level < 5:
    enemy = enemies[0]
else:
    enemy = enemies[2]

print(enemy)


print("########## Modifying Global Scope ###########")
enemies2 = 1


def increase_enemies2():
    # This is how we modify global variables
    # This is not a good idea to modify global variables
    global enemies2
    enemies2 = 2
    print(f"enemies inside function: {enemies2}")


increase_enemies2()
print(f"enemies outside function: {enemies2}")
