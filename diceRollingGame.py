import random

while True:
    querry = input("Let's play the game, do you want to roll? (y/n): ").lower()

    if querry == 'y':
        dir1 = random.randint(1, 6)
        dir2 = random.randint(1, 6)
        print(str(dir1) + "," + str(dir2))

    elif querry == 'n':
        print("Thanks for playing")
        break

    else:
        print("Invalid choice")