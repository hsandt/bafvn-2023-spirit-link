# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("MC", image="")
define g = Character("Guide", image="")
define l = Character("Lobbyist", image="")

transform left_side:
    xalign 0.1

transform right_side:
    xalign 0.9


# The game starts here.

label start:
    jump a1s1
