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
                                        "Delete Card", "Print Cards",
                                        "Exit"])
    if option == "Add Card":
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
    while len(name) == 0:
        name = easygui.enterbox("Enter the Name of the Monster",
                                "Monster Card Creator")
        while name is None:
            return
    name = name.capitalize()
    monster_cards[name] = {}
    add_card(name, "Strength", "Creator")
    if monster_cards[name]['Strength'] is None:
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
    if not yorn:
        del monster_cards[name]
        add_card_organiser()


# Allows for a much simpler way of creating a Monster Card
def add_card(name, stat, title):
    stat_level = easygui.integerbox(f"{name}:\nEnter the Level of {stat}",
                                    f"Monster Card {title}",
                                    upperbound=UP_BOUND, lowerbound=LOW_BOUND)
    monster_cards[name][stat] = stat_level


# Prints all the Monster Cards to the Console
def print_cards():
    for name, skill_level in monster_cards.items():
        print(f"\nMonster Name: {name}")

        for skill in skill_level:
            print(f"{skill}: {skill_level[skill]}")


# Allows the user to select what part of a certain Monster Card they would
# like to change
def change_card():
    monster_card_names = [i for i in monster_cards]
    new_name = ""
    name = easygui.buttonbox("Select what Monster Card you would like to "
                             "Change", "Monster Card Changer",
                             choices=monster_card_names)
    choice_list = ["Name", "Strength", "Speed", "Stealth", "Cunning"]
    while True:
        option = easygui.buttonbox(f"Select the part of {name} you would "
                                   f"like to change", "Monster Card Changer",
                                   choices=choice_list)
        if option == "Name":
            while new_name == "" or new_name is None:
                new_name = easygui.enterbox(f"Enter the new name for "
                                            f"{name}", "Monster Card Changer")
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
        if not yorn:
            break


# Deletes the selected Monster Card chosen by the user
def delete_card():
    monster_card_names = [i for i in monster_cards]
    monster_card_names.append("Exit")
    o = 1
    while o == 1:
        card_name = easygui.buttonbox("Which card would you like to delete?",
                                      "Monster Card Deleter",
                                      choices=monster_card_names)
        if card_name == "Exit":
            return
        yorn = easygui.ynbox(f"Are you sure you want to delete {card_name}?",
                             "Monster Card Deleter")
        if yorn:
            o = 2
    del monster_cards[card_name]


# Quits the program
def exit_program():
    print_cards()
    print(f"\nThere are {len(monster_cards.items())} Monster Cards recorded")
    quit()


while True:
    welcome()
