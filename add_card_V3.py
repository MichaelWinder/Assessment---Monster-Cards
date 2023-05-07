import easygui

UP_BOUND = 25
LOW_BOUND = 1

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
        print("change_card()")
    elif option == "Delete Card":
        print("delete_card()")
    elif option == "Print Cards":
        print("print_cards()")
    elif option == "Exit":
        print("exit_program()")


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


def add_card(name, stat, title):
    stat_level = easygui.integerbox(f"{name}:\nEnter the Level of {stat}",
                                    f"Monster Card {title}",
                                    upperbound=UP_BOUND, lowerbound=LOW_BOUND)
    monster_cards[name][stat] = stat_level


while True:
    welcome()
