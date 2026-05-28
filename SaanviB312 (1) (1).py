def check_user_input(userInput):
    if userInput.isdigit():
        return int(userInput)
    else:
        return userInput.casefold()

def does_nothing():
    pass  # does nothing

def add_to_order(item_name):
    order.append(item_name)

def print_order(message, order):
    print(message + " " + order)

def ask_yes_no(prompt):
    answer = input(prompt).lower()

    while answer not in ["yes", "no"]:
        print("Please check spelling")
        print(" ")
        answer = input(prompt).lower()

    return answer

def ask_size(prompt):
    size = input(prompt).lower()

    while size not in ["small", "medium", "large"]:
        print("Please check spelling")
        print(" ")
        size = input(prompt).lower()

    return size

def print_full_order(order, totalprice):
    summary = "Your order summary is:\n"

    for item in order:
        summary = summary + "\n  - " + item

    summary = summary + "\n\nYour grand total is $" + str(format(totalprice, ".2f"))

    print(summary)

order = []

# create variables for input choices
choice1 = ""
choice2 = ""
choice3 = ""
choice4 = ""
ynfries = ""
totalprice = 0
mega = ""
ketchup = 0

# LOOP: keep ordering sandwiches until done

print("Welcome to the Sandwich Shop!")
print(" ")

another_sandwich = "yes"

while another_sandwich == "yes":

    # code for choosing sandwich
    print("What type of sandwich would you like?")
    print(" ")
    print("chicken                           $5.25")
    print("beef                              $6.25")
    print("tofu                              $5.75")
    print(" ")

    choice1 = input("Enter choice here: ").lower()

    while choice1 not in ["chicken", "beef", "tofu"]:
        print("Please check spelling")
        print(" ")
        choice1 = input("Enter choice here: ").lower()

    print(" ")
    print("You chose " + choice1)
    print(" ")
    print(" ")

    if choice1 == "chicken":
        totalprice = totalprice + 5.25

    elif choice1 == "beef":
        totalprice = totalprice + 6.25

    elif choice1 == "tofu":
        totalprice = totalprice + 5.75

    add_to_order(choice1 + " sandwich")

    another_sandwich = ask_yes_no(
        "Would you like to add another sandwich? yes or no?: "
    )

    print(" ")

# LOOP: keep ordering beverages until done

print("Would you like a beverage?")
print(" ")

choice2 = ask_yes_no("yes or no?: ")

while choice2 == "yes":

    print(" ")
    print("What size beverage would you like?")
    print(" ")
    print("small                             $1.00")
    print("medium                            $1.75")
    print("large                             $2.25")
    print(" ")

    choice3 = ask_size("Enter choice here: ")

    print(" ")
    print("You chose " + choice3 + " beverage.")
    print(" ")
    print(" ")

    if choice3 == "small":
        totalprice = totalprice + 1.00

    elif choice3 == "medium":
        totalprice = totalprice + 1.75

    elif choice3 == "large":
        totalprice = totalprice + 2.25

    add_to_order(choice3 + " beverage")

    choice2 = ask_yes_no(
        "Would you like to add another beverage? yes or no?: "
    )

    print(" ")

print("So far your total price is $" + str(format(totalprice, ".2f")))
print(" ")
print(" ")
print(" ")

# LOOP: keep ordering fries until done

print("Would you like french fries?")
print(" ")

ynfries = ask_yes_no("yes or no?: ")

while ynfries == "yes":

    print(" ")
    print("What size of french fries would you like?")
    print(" ")
    print("small                             $1.00")
    print("medium                            $1.50")
    print("large                             $2.00")
    print(" ")

    choice4 = ask_size("Enter choice here: ")

    print(" ")
    print("You chose size " + choice4 + " of french fries.")
    print(" ")
    print(" ")

    if choice4 == "small":

        mega = input(
            "Would you like to mega-size your fries? yes or no?: "
        ).lower()

        while mega not in ["yes", "no"]:
            print("Please check spelling")
            print(" ")
            mega = input("yes or no?: ").lower()

        if mega == "yes":

            choice4 = "large (mega-sized from small)"

            print(
                "You chose size "
                + choice4
                + " of french fries."
            )

            # mega-size fries total price
            totalprice = totalprice + 2.25

            add_to_order(choice4 + " fries")

        else:

            totalprice = totalprice + 1.00

            add_to_order(choice4 + " fries")

    elif choice4 == "medium":

        totalprice = totalprice + 1.50

        add_to_order(choice4 + " fries")

    elif choice4 == "large":

        totalprice = totalprice + 2.00

        add_to_order(choice4 + " fries")

    ynfries = ask_yes_no(
        "Would you like to add another fries? yes or no?: "
    )

    print(" ")

print("So far your total price is $" + str(format(totalprice, ".2f")))
print(" ")
print(" ")
print(" ")

# code for choosing ketchup

while True:

    ketchup = input(
        "How many ketchup packets would you like? ($0.25 each): "
    )

    try:

        ketchup = int(ketchup)

        if ketchup >= 0:
            break

        else:
            print("Please enter a positive number (0 or higher).")

    except ValueError:

        print(
            "Error: '"
            + ketchup
            + "' is not a valid number. Please try again."
        )

print("You've selected " + str(ketchup) + " packets of ketchup.")
print(" ")
print(" ")
print(" ")

if ketchup > 0:
    add_to_order(str(ketchup) + " ketchup packets")

totalprice = totalprice + (ketchup * 0.25)

print("So far your total price is $" + str(format(totalprice, ".2f")))
print(" ")
print(" ")
print(" ")

# Check if order has both a beverage and fries for combo deal

has_beverage = False
has_fries = False

for item in order:

    if "beverage" in item:
        has_beverage = True

    if "fries" in item:
        has_fries = True

if has_beverage and has_fries:

    print(
        "CONGRATS! You got the Combo Meal Deal! "
        "$1.00 has been discounted."
    )

    totalprice = totalprice - 1.00

print(" ")
print(" ")

# Print full order summary

print_full_order(order, totalprice)