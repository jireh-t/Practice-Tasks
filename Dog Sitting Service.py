# Different functions for each menu choice
roll = []


def drop_off():
    dog_name = input("What is your dog's name? ")
    if dog_name in roll:
        print("Sorry {} is already on the list!".format(dog_name))
    else:
        roll.append(dog_name)
        print("We have added {} to the list, thank you!".format(dog_name))


def pick_up():
    pick_up_name = input("What is the name of the dog you wish to pick up? ")
    if pick_up_name in roll:
        roll.remove(pick_up_name)
        print("We have removed {} from the list".format(pick_up_name))
    else:
        print("Sorry, we don't seem to have {} on our list".format(pick_up_name))


def calc_cost():
    rate = 22.5
    days = int(input("How many days to charge for? "))
    dogs = len(roll)
    cost = rate * days * dogs
    print("Your total cost is ${:.2f}".format(cost))


def print_roll():
    print(f"The dogs currently staying at DogsRus are")
    for dog in roll:
        print(dog)


def exit_():
    print("See you later!")


def main():
    choice = 0
    while choice != 5:
        try:
            print("\nWelcome to DogsRus\n"
                  "What would you like to do today? Select from the menu below\n" 
                  "1) Drop off a dog\n"
                  "2) Pick up a dog\n"
                  "3) Calculate cost\n"
                  "4) Print roll\n"
                  "5) Exit the system\n")
            choice = int(input("Please enter your choice (number between 1 & 5): "))

            if choice == 1:
                drop_off()

            elif choice == 2:
                pick_up()

            elif choice == 3:
                calc_cost()

            elif choice == 4:
                print_roll()

            elif choice == 5:
                exit_()

            else:  # If invalid input is entered
                print("Please enter a valid integer between 1 and 5\n")

        except ValueError:
            print("Please enter a valid integer between 1 and 5\n")


# Main Routine
print(main())
