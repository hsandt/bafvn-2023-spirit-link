# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define charlet = Character("Charlet")
define pichit = Character("Pichit")
define raegan = Character("Raegan")
define phrarat = Character("Phrarat")
define maka = Character("Maka")
define fan = Character("Fan")


# Story event flags

default has_analyzed_assassin_cloth = False
default has_analyzed_assassin_power = False
default has_analyzed_assassin_spirit = False
default has_analyzed_assassin_stone = False


# Transforms

transform character_left:
    xalign 0.1

transform character_middle:
    xalign 0.5

transform character_right:
    xalign 0.9

transform companion_left:
    xalign 0.1
    yalign 0.1

transform companion_middle:
    xalign 0.5
    yalign 0.5

transform companion_right:
    xalign 0.9
    yalign 0.1

transform half_size:
    xysize 0.5


# The game starts here.

label start:
    jump a1s1
