# Counts

count = 0
comp_score = 0
player_score = 0


# If the user enters paper

def paper():
    global count
    global player_score
    global comp_score
    import random
    options = ["paper", "scissors", "rock"]
    option = random.choice(options)
    print(f"Computer chose {option}")

    if option == "paper":
        print("It was a draw!")

    elif option == "rock":
        print("You won!")
        count += 1
        player_score += 1

    else:
        print("Sorry you lost")
        count += 1
        comp_score += 1


# If the user enters scissors

def scissors():
    global count
    global player_score
    global comp_score
    import random
    options = ["paper", "scissors", "rock"]
    option = random.choice(options)
    print(f"Computer chose {option}")

    if option == "scissors":
        print("It was a draw!")

    elif option == "paper":
        print("You won!")
        count += 1
        player_score += 1

    else:
        print("Sorry you lost")
        count += 1
        comp_score += 1


# If the user enters rock

def rock():
    global count
    global player_score
    global comp_score
    import random
    options = ["paper", "scissors", "rock"]
    option = random.choice(options)
    print(f"Computer chose {option}")

    if option == "rock":
        print("It was a draw!")

    elif option == "scissors":
        print("You won!")
        count += 1
        player_score += 1

    else:
        print("Sorry you lost")
        count += 1
        comp_score += 1


# Main function


name = input("What is your name? ")
print(f"Hello {name}, let's play Paper, Scissors, Rock (Best of 3)")

while count != 3:

    answer = input("\nChoose paper, scissors, or, "
                   "rock ").lower()
    if answer == "paper":
        print(paper())

    elif answer == "scissors":
        print(scissors())

    elif answer == "rock":
        print(rock())

    else:
        print("\nPlease choose a valid answer (paper, scissors or rock)")

print(f"\nComputer won {comp_score} games, and you won {player_score} games!")

if comp_score > player_score:
    print("Computer is the winner!")

else:
    print("You are the winner!")
