# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define charlet = Character("Charlet", color="#7B68EE")
define pichit = Character("Pichit")
define raegan = Character("Raegan")
define phrarat = Character("Phrarat")
define makara = Character("Makara", color="#6495ED")
define fan = Character("Fan")


# Story event flags

# A1S1
default has_looked_at_booth = False
default has_looked_at_crowd = False

# A1S2
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
