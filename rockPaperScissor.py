import random
options = ["rock", "paper", "scissor"]
while True:
    try:
        user_input = input("Enter rock, paper, scissor or quit to exit: ").lower()
        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")
        if user_input not in options:
            print("Invalid choice")
            break


        if user_input == computer_choice:
            print("It's a tie!")
            break
        elif (user_input == "rock" and computer_choice == "scissor") or (user_input == "paper" and computer_choice == "rock") or (user_input == "scissor" and computer_choice == "paper"):
            print("You win!")
            break
        else:
            print("You lose!")
            break
    except ValueError:
        print("Please enter a valid option.")