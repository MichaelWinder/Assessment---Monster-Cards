"""This program is a tool for digitally creating a dictionary of Monster Cards.
The Monster Cards consist of a Name and four different stats. Strength,
Speed, Stealth, and Cunning. The user is able to manipulate the Monster
Cards as they choose to create a list of Cards they want.
"""
import easygui

# Changeable Variables
UP_BOUND = 25
LOW_BOUND = 1

# Main Dictionary for the Monster Cards
monster_cards = {
    "Stoneling":
        {"Strength": 7,
         "Speed": 1,
         "Stealth": 25,
         "Cunning": 15
         },
    "Vexscream":
        {"Strength": 1,
         "Speed": 6,
         "Stealth": 21,
         "Cunning": 19
         },
    "Dawnmirage":
        {"Strength": 5,
         "Speed": 15,
         "Stealth": 18,
         "Cunning": 22
         },
    "Blazegolem":
        {"Strength": 15,
         "Speed": 20,
         "Stealth": 23,
         "Cunning": 6
         },
    "Websnake":
        {"Strength": 7,
         "Speed": 21,
         "Stealth": 10,
         "Cunning": 5
         },
    "Moldvine":
        {"Strength": 21,
         "Speed": 18,
         "Stealth": 14,
         "Cunning": 5
         },
    "Vortexwing":
        {"Strength": 19,
         "Speed": 13,
         "Stealth": 19,
         "Cunning": 2
         },
    "Rotthing":
        {"Strength": 16,
         "Speed": 7,
         "Stealth": 4,
         "Cunning": 12
         },
    "Froststep":
        {"Strength": 14,
         "Speed": 14,
         "Stealth": 17,
         "Cunning": 4
         },
    "Wispghoul":
        {"Strength": 17,
         "Speed": 19,
         "Stealth": 3,
         "Cunning": 2
         }
}


# Provides a home screen for the program allowing the user to use all the
# components of the Program.
def welcome():
    option = easygui.buttonbox("~~~Welcome to the Monster Card creator!~~~\n\n"
                               "Here you can create, change, and delete "
                               "Monster Cards!\nYou have 5 choices of what you"
                               " want to do\n1- Add a Monster Card\n2- Change"
                               " a Monster Card\n3- Delete a Monster Card\n"
                               "4- Print out the Full list of Monster Cards\n"
                               "5- Exit the Program", "Monster Card Menu",
                               choices=["Add Card", "Change Card",
                                        "Delete Card", "Print Cards", "Exit"])
    if option == "Add Card":  # If statements to call on a function to run
        add_card_organiser()
    elif option == "Change Card":
        change_card()
    elif option == "Delete Card":
        delete_card()
    elif option == "Print Cards":
        print_cards()
    elif option == "Exit":
        exit_program()


# The main code for adding a new Monster Card to the dictionary
def add_card_organiser():
    name = ""
    while name == "":  # Stops the user from entering nothing
        name = easygui.enterbox("Enter the Name of the Monster",
                                "Monster Card Creator")
        while name is None:  # Returns the user to main menu if they cancel
            return
    name = name.capitalize()
    monster_cards[name] = {}
    add_card(name, "Strength", "Creator")  # Adds the strength stat to the card
    if monster_cards[name]['Strength'] is None:  # Cancels add_card_organiser()
        del monster_cards[name]
        return
    add_card(name, "Speed", "Creator")
    if monster_cards[name]['Speed'] is None:
        del monster_cards[name]
        return
    add_card(name, "Stealth", "Creator")
    if monster_cards[name]['Stealth'] is None:
        del monster_cards[name]
        return
    add_card(name, "Cunning", "Creator")
    if monster_cards[name]['Cunning'] is None:
        del monster_cards[name]
        return
    yorn = easygui.ynbox(f"Are the Card details correct?\n\n{name}:\n"
                         f"Strength = {monster_cards[name]['Strength']}\n"
                         f"Speed = {monster_cards[name]['Speed']}\nStealth "
                         f"= {monster_cards[name]['Stealth']}\nCunning = "
                         f"{monster_cards[name]['Cunning']}", "Monster Card "
                                                              "Creator")
    if not yorn:  # Checks all details are correct
        del monster_cards[name]  # deletes the card and resets if details
        add_card_organiser()  # are incorrect


# Allows for a much simpler way of creating a Monster Card
def add_card(name, stat, title):
    stat_level = easygui.integerbox(f"{name}:\nEnter the Level of {stat}",
                                    f"Monster Card {title}",
                                    upperbound=UP_BOUND, lowerbound=LOW_BOUND)
    if title == "Changer":
        if stat_level is None:
            return
    monster_cards[name][stat] = stat_level  # Adds stat to Monster Card


# Prints all the Monster Cards to the Console
def print_cards():
    for name, skill_level in monster_cards.items():
        print(f"\nMonster Name: {name}")  # Prints the name of the Card

        for skill in skill_level:
            print(f"{skill}: {skill_level[skill]}")
            # Prints the skills of the Monster Card


# Allows the user to select what part of a certain Monster Card they would
# like to change
def change_card():
    monster_card_names = [i for i in monster_cards]
    name = easygui.buttonbox("Select what Monster Card you would like to "
                             "Change", "Monster Card Changer",
                             choices=monster_card_names)
    choice_list = ["Name", "Strength", "Speed", "Stealth", "Cunning"]
    while True:  # Loop for setting stats
        new_name = ""
        option = easygui.buttonbox(f"Select the part of {name} you would "
                                   f"like to change", "Monster Card Changer",
                                   choices=choice_list)
        if option == "Name":
            while new_name == "":
                new_name = easygui.enterbox(f"Enter the new name for "
                                            f"{name}", "Monster Card Changer")
            if new_name is None:  # If user selects cancel returns to menu
                return
            # Stops the program from deleting the Monster Card if it has the
            # same name
            if new_name != name:
                monster_cards[new_name] = monster_cards[name]
                del monster_cards[name]
                name = new_name
        else:
            add_card(name, option, "Changer")
            while monster_cards[name][option] is None:
                add_card(name, option, "Changer")

        yorn = easygui.ynbox(f"{name}:\nStrength = "
                             f"{monster_cards[name]['Strength']}\nSpeed = "
                             f"{monster_cards[name]['Speed']}\nStealth = "
                             f"{monster_cards[name]['Stealth']}\nCunning = "
                             f"{monster_cards[name]['Cunning']}\nWould you "
                             f"like to change anything else?",
                             "Monster Card Changer")
        if not yorn:  # Stops the loop to change name or another stat
            break


# Deletes the selected Monster Card chosen by the user
def delete_card():
    monster_card_names = [i for i in monster_cards]  # List of all the names
    monster_card_names.append("Exit")  # Adds the exit command for the user
    while True:
        card_name = easygui.buttonbox("Which card would you like to delete?",
                                      "Monster Card Deleter",
                                      choices=monster_card_names)
        if card_name == "Exit":  # Stops function
            return
        yorn = easygui.ynbox(f"Are you sure you want to delete {card_name}?",
                             "Monster Card Deleter")
        if yorn:
            break
    del monster_cards[card_name]  # Deletes Monster Card


# Quits the program
def exit_program():
    print_cards()  # Runs the print_cards() function
    print(f"\nThere are {len(monster_cards.items())} Monster Cards recorded")
    quit()  # Quits the program


# Loop to always bring the user back to the welcome screen
while True:
    welcome()
