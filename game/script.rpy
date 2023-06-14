# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define male = Character("Valadick")
define female = Character("Elena")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy:
        xalign 0
        yalign 1.0

    # These display lines of dialogue.

    male "Zdarova, ebati. S etogo vseo i nachinaetsia."

    female "Zdarova"


    male "Sozdati eto vseo bilo legko, programma sama delaet osnovu. Dumaiu, u nas esti vse shansi sdelati chto-to adekvatnoe i zarabotati nemnogo deniak!"

    # This ends the game.



    return
