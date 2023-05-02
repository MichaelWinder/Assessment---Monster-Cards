import easygui

up_bound = 25
low_bound = 1

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
        print("delete_card()")
    elif option == "Print Cards":
        print("print_cards()")
    elif option == "Exit":
        print("exit_program()")


def add_card_organiser():
    name = easygui.enterbox("Enter the Name of the Monster", "Monster Card "
                            "Creator").capitalize()
    monster_cards[name] = {}
    add_card(name, "Strength")
    add_card(name, "Speed")
    add_card(name, "Stealth")
    add_card(name, "Cunning")
    yorn = easygui.ynbox(f"Are the Card details correct?\n\n{name}:\n"
                         f"Strength = {monster_cards[name]['Strength']}\n"
                         f"Speed = {monster_cards[name]['Speed']}\nStealth "
                         f"= {monster_cards[name]['Stealth']}\nCunning = "
                         f"{monster_cards[name]['Cunning']}", "Monster Card "
                                                              "Creator")
    if not yorn:
        del monster_cards[name]
        add_card_organiser()


def add_card(name, stat):
    stat_level = easygui.integerbox(f"{name}:\nEnter the Level of {stat}",
                                    "Monster Card Creator", upperbound=up_bound
                                    , lowerbound=low_bound)
    monster_cards[name][stat] = stat_level
    return stat_level


def change_card():



welcome()
