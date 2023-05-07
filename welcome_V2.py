import easygui


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
        print("add_card_organiser()")
    elif option == "Change Card":
        print("change_card()")
    elif option == "Delete Card":
        print("delete_card()")
    elif option == "Print Cards":
        print("print_cards()")
    elif option == "Exit":
        print("exit_program()")


while True:
    welcome()
