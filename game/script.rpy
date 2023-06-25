# The script of the game goes in this file.


# Uncomment this when you have issues with Renpy reloading again and again after the shift manual reload (Shift+R)
# even if there are no changes
# See https://github.com/renpy/renpy/issues/4762
# define config.autoreload = False


# Custom keymap

init python:
    # Add Ctrl+Q => Quit if not already set (a priori it is not set for any OS,
    # although macOS uses Cmd+Q)
    if 'quit' not in config.keymap or 'ctrl_K_q' not in config.keymap['quit']:
        config.keymap['quit'].append('ctrl_K_q')

    # Add Space => Confirm selected button (instead of just Enter, etc.) for convenience
    if 'button_select' not in config.keymap or 'K_SPACE' not in config.keymap['button_select']:
        config.keymap['button_select'].append('K_SPACE')


# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Main characters
define charlet = Character("Charlet", color="#7B68EE")
define pichit = Character("Pichit")
define raegan = Character("Raegan")
define phrarat = Character("Phrarat")
define makara = Character("Makara", color="#6495ED")
define fan = Character("Fan")

# Secondary characters
define mara = Character("Professor Mara")
define man_with_rifle = Character("Man")


# Story event flags

# A1S1
default has_looked_at_booth = False
default has_looked_at_crowd = False

# A1S2
default has_analyzed_assassin_weapon = False
default has_analyzed_assassin_stone = False


# Transforms

transform character_far_left:
    xalign 0.0

transform character_left:
    xalign 0.1

transform character_middle_left:
    xalign 0.3

transform character_middle:
    xalign 0.5

transform character_middle_right:
    xalign 0.7

transform character_right:
    xalign 0.9

transform character_far_right:
    xalign 1.0

transform companion_far_left:
    xalign 0.0
    yalign 0.1

transform companion_left:
    xalign 0.1
    yalign 0.1

transform companion_middle_left:
    xalign 0.3
    yalign 0.1

transform companion_middle:
    xalign 0.5
    yalign 0.5

transform companion_middle_right:
    xalign 0.7
    yalign 0.1

transform companion_right:
    xalign 0.9
    yalign 0.1

transform companion_far_right:
    xalign 1.0
    yalign 0.1

transform half_size:
    xysize 0.5

transform flip:
    xzoom -1.0

# The game starts here.

label start:
    jump a1s1
