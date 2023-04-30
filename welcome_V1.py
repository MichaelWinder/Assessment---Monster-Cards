import easygui


def welcome():
    easygui.buttonbox("~~~Welcome to the Monster Card creator!~~~\n\nHere you "
                      "can create, change, and delete Monster Cards!\nYou "
                      "have 5 choices of what you want to do\n1- Add a "
                      "Monster Card\n2- Change a Monster Card\n3- Delete a "
                      "Monster Card\n4- Print out the Full list of Monster "
                      "Cards\n5- Exit the Program", "Monster Card Menu",
                      choices=["Add Card", "Change Card", "Delete Card",
                               "Print all Cards", "Exit"])


while True:
    welcome()
