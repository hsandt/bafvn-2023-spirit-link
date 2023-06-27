# The script of the game goes in this file.


# Uncomment this when you have issues with Renpy reloading again and again after the shift manual reload (Shift+R)
# even if there are no changes
# See https://github.com/renpy/renpy/issues/4762
define config.autoreload = False


# Custom keymap

init python:
    # Add Ctrl+Q => Quit if not already set (a priori it is not set for any OS,
    # although macOS uses Cmd+Q)
    if 'quit' not in config.keymap or 'ctrl_K_q' not in config.keymap['quit']:
        config.keymap['quit'].append('ctrl_K_q')

    # Add Space => Confirm selected button (instead of just Enter, etc.) for convenience
    if 'button_select' not in config.keymap or 'K_SPACE' not in config.keymap['button_select']:
        config.keymap['button_select'].append('K_SPACE')

    def play_delayed_sfx(sfx, delay):
        """Play sfx with delay. You can directly enter sfx alias such as audio.sfx.fire (without quotes) as sfx"""
        ui.timer(delay, Play("sound", sfx))


# Copied and adapted from renpy-sdk/renpy/common/00definitions.rpy
define vpunch_powerful = Move((0, 20), (0, -20), .10, bounce=True, repeat=True, delay=.275)
define hpunch_powerful = Move((30, 0), (-30, 0), .10, bounce=True, repeat=True, delay=.275)


# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Main characters
define charlet = Character("Charlet", color="#b4a9f5")
define pichit = Character("Pichit", color="#a9d978")
define raegan = Character("Raegan", color="#e1cc5e")
define phrarat = Character("Assassin", color="#dd796e")
define makara = Character("Makara", color="#6495ed")
define fan = Character("Fan", color="#89d47d")

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


# The game starts here.

label start:
    jump a1s1
