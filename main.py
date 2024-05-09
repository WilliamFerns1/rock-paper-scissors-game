import random
import json

def main():

    # Game loop (breaks if user doesn't want to retry)
    while True:
        # 1. Make a game loop
        user_score = 0
        computer_score = 0
        rounds = []

        # 2. Ask user for their option. Whether that be rock, paper or scissors. If the user input is invalid, handle that case and ask user again for an option.
        print("Welcome to this simple rock paper and scissors game.")
        
        # loop for going back and fourth, user and computer input
        while True:
            while True: # Exit loop if user rounds something valid
                print("\n")
                user_input = int(input("Type in the number for the option you are choosing. \n1. Rock\n2. Paper\n3. Scissors: "))
                if user_input == 1 or user_input == 2 or user_input == 3:
                    break
                else: 
                    print(f"Incorrect input. Pick one of the following: 1, 2, 3")
            
            print("\n")
            computer_input = random.choice(range(1, 4))
            if user_input == computer_input:
                print("Draw! You and the computers choice was both {user_input}")
                print(f"Computer: {computer_input}\nUser: {user_input}")
                rounds.append({
                    "user": user_input,
                    "computer": computer_input,
                    "winner": "draw",
                })

            # Rock, Paper
            elif user_input == 1 and computer_input == 2:
                print("Computer won this round!")
                print(f"Computer: {computer_input}\nUser: {user_input}")
                computer_score = computer_score + 1
                print(f"Computer: {computer_input}\nUser: {user_input}")
                rounds.append({
                    "user": user_input,
                    "computer": computer_input,
                    "winner": "computer",
                })

            # Rock, Scissors 
            elif user_input == 1 and computer_input == 3:
                print("You won this round!")
                print(f"Computer: {computer_input}\nUser: {user_input}")
                user_score = user_score + 1
                rounds.append({
                    "user": user_input,
                    "computer": computer_input,
                    "winner": "user",
                })

            # Paper, Rock 
            elif user_input == 2 and computer_input == 1:
                print("You won this round!")
                user_score = user_score + 1
                print(f"Computer: {computer_input}\nUser: {user_input}")
                rounds.append({
                    "user": user_input,
                    "computer": computer_input,
                    "winner": "user",
                })


            # Paper, Scissors 
            elif user_input == 2 and computer_input == 3:
                print("Computer won this round!")
                computer_score = computer_score + 1
                print(f"Computer: {computer_input}\nUser: {user_input}")
                rounds.append({
                    "user": user_input,
                    "computer": computer_input,
                    "winner": "computer",
                })

            # Scissors, Rock  
            elif user_input == 2 and computer_input == 3:
                print("Computer won this round!")
                computer_score = computer_score + 1
                print(f"Computer: {computer_input}\nUser: {user_input}")
                rounds.append({
                    "user": user_input,
                    "computer": computer_input,
                    "winner": "computer",
                })

            # Scissors, Paper 
            else:
                print("You won this round!")
                user_score = user_score + 1
                print(f"Computer: {computer_input}\nUser: {user_input}")
                rounds.append({
                    "user": user_input,
                    "computer": computer_input,
                    "winner": "user",
                })
            
            print("\n")
            print("Score: ")
            print(f"User: {user_score}")
            print(f"Computer: {computer_score}")

            # check whether or not the computer or user has won.
            if user_score == 3 or computer_score == 3:
                print("\n")
                if user_score == 3:
                    print("You have won!")

                else:
                    print("You have lost!")

                # break when the user or computer has won.
                break

        retry_option = int(input("Retry? (1 = true, 0 = false): "));
        if retry_option != 1:
            for index, round in enumerate(rounds):
                print("\n")
                print(f"Round: {index+1}")
                print(f"User: {round['user']}")
                print(f"Computer: {round['computer']}")
                print(f"Winner: {round['winner']}")
            break


if __name__ == "__main__":
    main()
