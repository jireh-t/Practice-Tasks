# Functions
def fun_sun():
    global fun_sun_total
    fun_sun_total = 0
    global fun_sun_age
    fun_sun_age = []
    try:
        age = int(input("How old is your child? "))
        if age < 5 or age > 15:
            print("Sorry, your child has to be between 5 and 15 to be in the programme")
        else:
            fun_sun_total += 1
            fun_sun_age.append(age)

    except ValueError:
        print("Please enter an integer")


def active_():
    global active_total
    active_total = 0
    global active_age
    active_age = []
    try:
        age = int(input("How old is your child? "))
        if age < 5 or age > 15:
            print("Sorry, your child has to be between 5 and 15 to be in the programme")
        else:
            active_total += 1
            active_age.append(age)

    except ValueError:
        print("Please enter an integer")


def average(age):
    avg = sum(age) / len(age)
    return avg


# Main Routine

program = ""
while program != "x":
    program = input("\nWhich programme would you like to attend?\n"
      "Fun in the Sun, or Active Kidz\n"
      "Or enter X to see the average when you are finished\n").lower()

    if program == "fun in the sun":
        fun_sun()

    elif program == "active kidz":
        active_()

    elif program == "x":
        print(f"\nThere is a total of {fun_sun_total} in the Fun in the Sun "
              f"programme, and a total of {active_total} in the "
              f"Active Kidz "
              f"programme\n"
              f"The average age for Fun in the Sun is "
              f"{round(average(fun_sun_age))} "
              f"years old, and the average age for Active Kidz, is "
              f"{round(average(active_age))} years old")

    else:
        print("Please enter a valid program or 'X' to see the average when "
              "you are finished")






