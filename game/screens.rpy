################################################################################
## Initialization
################################################################################

init offset = -1

transform circle_rotate_0(_xpos=0, _ypos=0, _depth=0):
    matrixcolor TintMatrix(str("#000"+str(_depth)))
    xpos _xpos
    ypos _ypos
    rotate 0
    
transform circle_rotate(_xpos=0, _ypos=0, _depth=0):
    matrixcolor TintMatrix(str("#000"+str(_depth)))
    xpos _xpos
    ypos _ypos
    rotate 0
    
transform circle_rotate_r(_xpos=0, _ypos=0, _depth=0):
    matrixcolor TintMatrix(str("#000"+str(_depth)))
    xpos _xpos
    ypos _ypos
    rotate 0

transform circle_rotate_old(_xpos=0, _ypos=0, _depth=0):
    matrixcolor TintMatrix(str("#000"+str(_depth)))
    xpos _xpos
    ypos _ypos
    parallel:
      linear 5.0 alpha 1.0
      repeat
    parallel:
      rotate 0
      linear 0.1 rotate 10
      linear 1.0 rotate 10
      linear 0.1 rotate 20
      linear 1.0 rotate 20
      linear 0.1 rotate 30
      linear 1.0 rotate 30
      linear 0.1 rotate 40
      linear 1.0 rotate 40
      linear 0.1 rotate 50
      linear 1.0 rotate 50
      linear 0.1 rotate 60
      linear 1.0 rotate 60
      linear 0.1 rotate 70
      linear 1.0 rotate 70
      linear 0.1 rotate 80
      linear 1.0 rotate 80
      linear 0.1 rotate 90
      linear 1.0 rotate 90
      linear 0.1 rotate 100
      linear 1.0 rotate 100

      linear 0.1 rotate 110
      linear 1.0 rotate 110
      linear 0.1 rotate 120
      linear 1.0 rotate 120
      linear 0.1 rotate 130
      linear 1.0 rotate 130
      linear 0.1 rotate 140
      linear 1.0 rotate 140
      linear 0.1 rotate 150
      linear 1.0 rotate 150
      linear 0.1 rotate 160
      linear 1.0 rotate 160
      linear 0.1 rotate 170
      linear 1.0 rotate 170
      linear 0.1 rotate 180
      linear 1.0 rotate 180
      linear 0.1 rotate 190
      linear 1.0 rotate 190
      linear 0.1 rotate 200
      linear 1.0 rotate 200

      linear 0.1 rotate 210
      linear 1.0 rotate 210
      linear 0.1 rotate 220
      linear 1.0 rotate 220
      linear 0.1 rotate 230
      linear 1.0 rotate 230
      linear 0.1 rotate 240
      linear 1.0 rotate 240
      linear 0.1 rotate 250
      linear 1.0 rotate 250
      linear 0.1 rotate 260
      linear 1.0 rotate 260
      linear 0.1 rotate 270
      linear 1.0 rotate 270
      linear 0.1 rotate 280
      linear 1.0 rotate 280
      linear 0.1 rotate 290
      linear 1.0 rotate 290
      linear 0.1 rotate 300
      linear 1.0 rotate 300

      linear 0.1 rotate 310
      linear 1.0 rotate 310
      linear 0.1 rotate 320
      linear 1.0 rotate 320
      linear 0.1 rotate 330
      linear 1.0 rotate 330
      linear 0.1 rotate 340
      linear 1.0 rotate 340
      linear 0.1 rotate 350
      linear 1.0 rotate 350
      linear 0.1 rotate 360
      linear 1.0 rotate 360
      repeat
      
      
transform circle_rotate_r_old(_xpos=0, _ypos=0, _depth=0):
    matrixcolor TintMatrix(str("#000"+str(_depth)))
    xpos _xpos
    ypos _ypos
    parallel:
      linear 5.0 alpha 1.0
      repeat
    parallel:
      rotate 0
      linear 0.1 rotate -10
      linear 1.0 rotate -10
      linear 0.1 rotate -20
      linear 1.0 rotate -20
      linear 0.1 rotate -30
      linear 1.0 rotate -30
      linear 0.1 rotate -40
      linear 1.0 rotate -40
      linear 0.1 rotate -50
      linear 1.0 rotate -50
      linear 0.1 rotate -60
      linear 1.0 rotate -60
      linear 0.1 rotate -70
      linear 1.0 rotate -70
      linear 0.1 rotate -80
      linear 1.0 rotate -80
      linear 0.1 rotate -90
      linear 1.0 rotate -90
      linear 0.1 rotate -100
      linear 1.0 rotate -100

      linear 0.1 rotate -110
      linear 1.0 rotate -110
      linear 0.1 rotate -120
      linear 1.0 rotate -120
      linear 0.1 rotate -130
      linear 1.0 rotate -130
      linear 0.1 rotate -140
      linear 1.0 rotate -140
      linear 0.1 rotate -150
      linear 1.0 rotate -150
      linear 0.1 rotate -160
      linear 1.0 rotate -160
      linear 0.1 rotate -170
      linear 1.0 rotate -170
      linear 0.1 rotate -180
      linear 1.0 rotate -180
      linear 0.1 rotate -190
      linear 1.0 rotate -190
      linear 0.1 rotate -200
      linear 1.0 rotate -200

      linear 0.1 rotate -210
      linear 1.0 rotate -210
      linear 0.1 rotate -220
      linear 1.0 rotate -220
      linear 0.1 rotate -230
      linear 1.0 rotate -230
      linear 0.1 rotate -240
      linear 1.0 rotate -240
      linear 0.1 rotate -250
      linear 1.0 rotate -250
      linear 0.1 rotate -260
      linear 1.0 rotate -260
      linear 0.1 rotate -270
      linear 1.0 rotate -270
      linear 0.1 rotate -280
      linear 1.0 rotate -280
      linear 0.1 rotate -290
      linear 1.0 rotate -290
      linear 0.1 rotate -300
      linear 1.0 rotate -300

      linear 0.1 rotate -310
      linear 1.0 rotate -310
      linear 0.1 rotate -320
      linear 1.0 rotate -320
      linear 0.1 rotate -330
      linear 1.0 rotate -330
      linear 0.1 rotate -340
      linear 1.0 rotate -340
      linear 0.1 rotate -350
      linear 1.0 rotate -350
      linear 0.1 rotate -360
      linear 1.0 rotate -360
      repeat

screen gear(_style=8, _scale=1.0, _xpos=0, _ypos=0, _direction=1, _depth=0):
        $gearlist = [8,10,11,14, 26, 19, 13]
        if not _style in gearlist:
          $_style = 8
        $offset = int(5*_scale)
        if _direction == 0:
            add im.FactorScale("gui/gears/gear_big_b_"+str(_style)+".png", _scale) at circle_rotate_0(_xpos+offset, _ypos+offset, _depth)
            add im.FactorScale("gui/gears/gear_big_w_"+str(_style)+".png", _scale) at circle_rotate_0(_xpos, _ypos, _depth)
        elif _direction > 0:
            add im.FactorScale("gui/gears/gear_big_b_"+str(_style)+".png", _scale) at circle_rotate(_xpos+offset, _ypos+offset, _depth)
            add im.FactorScale("gui/gears/gear_big_w_"+str(_style)+".png", _scale) at circle_rotate(_xpos, _ypos, _depth)
        else:
            add im.FactorScale("gui/gears/gear_big_b_"+str(_style)+".png", _scale) at circle_rotate_r(_xpos+offset, _ypos+offset, _depth)
            add im.FactorScale("gui/gears/gear_big_w_"+str(_style)+".png", _scale) at circle_rotate_r(_xpos, _ypos, _depth)

screen gear_8(_scale=1.0, _xpos=0, _ypos=0):
        $offset = int(5*_scale)
        add im.FactorScale("gui/gears/gear_big_b_8.png", _scale) at circle_rotate(_xpos+offset, _ypos+offset)
        add im.FactorScale("gui/gears/gear_big_w_8.png", _scale) at circle_rotate(_xpos, _ypos)

screen gear_10(_scale=1.0, _xpos=0, _ypos=0):
        $offset = int(5*_scale)
        add im.FactorScale("gui/gears/gear_big_b_10.png", _scale) at circle_rotate(_xpos+offset, _ypos+offset)
        add im.FactorScale("gui/gears/gear_big_w_10.png", _scale) at circle_rotate(_xpos, _ypos)

screen gear_11(_scale=1.0, _xpos=0, _ypos=0):
        $offset = int(5*_scale)
        add im.FactorScale("gui/gears/gear_big_b_11.png", _scale) at circle_rotate(_xpos+offset, _ypos+offset)
        add im.FactorScale("gui/gears/gear_big_w_11.png", _scale) at circle_rotate(_xpos, _ypos)

screen gear_14(_scale=1.0, _xpos=0, _ypos=0):
        $offset = int(5*_scale)
        add im.FactorScale("gui/gears/gear_big_b_14.png", _scale) at circle_rotate(_xpos+offset, _ypos+offset)
        add im.FactorScale("gui/gears/gear_big_w_14.png", _scale) at circle_rotate(_xpos, _ypos)

################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0) #Solid("#123456") #

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen gear_button(_text="NULL", _size=0.4, _xpos=0, _ypos=0, _action = NullAction(), _id = None, _isQuick=False):
    
    $iconoffset = 0#
    if _isQuick:
      $iconoffset = -3

    $offset = int(5*_size)
    add im.FactorScale("gui/gears/gear_big_b_26.png", _size) at circle_rotate(_xpos+offset, _ypos+offset)

    button:
      if _id:
        id _id
      at circle_rotate(_xpos, _ypos)
      background im.FactorScale("gui/gears/gear_big_w_26.png", _size)
      hover_background im.FactorScale("gui/gears/gear_big_y_26.png", _size)
      selected_idle_background im.FactorScale("gui/gears/gear_big_y_26.png", _size)
      xpos _xpos
      ypos _ypos
      action _action
      xsize int(310 * _size)
      ysize int(310 * _size)
      has vbox:
        yalign 0.5
        xalign 0.5
        if ".png" in _text:
          add "gui/button/icon_"+_text yoffset iconoffset at circle_rotate_r(0, 0)
        else:
          text _text hover_color "#000000"  selected_idle_color "#000000" at circle_rotate_r(0, 0)

    #imagebutton idle im.FactorScale("gui/gears/gear_big_w_26.png", _size) hover im.FactorScale("gui/gears/gear_big_y_26.png", _size)  xpos _xpos  ypos _ypos  action _action



screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu and not renpy.get_screen('choice'):

        use gear(10, 1.4, 1388, 600, 0, 3)

        #frame:
        #    background None
        #    xpos 1480
        #    ypos 700
        #    use gear(26, 0.4, 60, 20, 0)
        #    use gear(26, 0.4, 180, 20, 0)
        #    use gear(26, 0.4, 0, 120, 0)
        #    use gear(26, 0.4, 240, 120, 0)
        #    use gear(26, 0.4, 60, 220, 0)
        #    use gear(26, 0.4, 180, 220, 0)

        frame:
            background None
            xpos 1480
            ypos 700
            style_prefix "quick"

            #xalign 0.5
            #yalign 1.0

            #button :
            #  background im.FactorScale("gui/gears/gear_big_w_26.png", 0.4)
            #  hover_background im.FactorScale("gui/gears/gear_big_y_26.png", 0.4)
            #  xpos 60 ypos 20
            #  action Rollback()
            #  xsize int(310*.4)
            #  ysize int(310*.4)
            #  has vbox:
            #    yalign 0.5
            #    xalign 0.5
            #    text _("Back") hover_color "#000000"
            #use gear_button("Log", 0.4, 180, 20, ShowMenu('history'))


            use gear_button("back.png", 0.4, 60 , 20 ,  Rollback(), _isQuick=True)
            use gear_button("log.png", 0.4, 180 , 20 ,  ShowMenu('history'), _isQuick=True)
            use gear_button("skip.png", 0.4, 0 , 120 ,  Skip(), _isQuick=True) # alternate Skip(fast=True, confirm=True))
            use gear_button("auto.png", 0.4, 240 , 120 ,  Preference("auto-forward", "toggle"), _isQuick=True)
            use gear_button("save.png", 0.4, 60 , 220 ,  ShowMenu('save'), _isQuick=True)
            #textbutton _("Q.Save") action QuickSave()
            #textbutton _("Q.Load") action QuickLoad()
            use gear_button("config.png", 0.4, 180 , 220 ,  ShowMenu('preferences'), _isQuick=True)


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    $new_yoffset = 25
    $new_xoffset = 110
    $new_xpos = 500
    frame:
        background None
        style_prefix "navigation"

        ypos gui.navigation_ypos
        xalign 0.6

        #spacing gui.navigation_spacing

        if not renpy.get_screen('main_menu'):
            use gear_button("return.png", 0.4, new_xpos , new_yoffset , Return())
        $new_yoffset = new_yoffset * -1
        $new_xpos = new_xpos + new_xoffset
        
        if main_menu:

            if not renpy.get_screen('main_menu'):
                use gear_button("Start", 0.4, new_xpos , new_yoffset , Start(), _id="start")
            else:
                use gear_button("Start", 0.8, new_xpos-140 , new_yoffset-140 , Start(), _id="start")
            $new_yoffset = new_yoffset * -1
            $new_xpos = new_xpos + new_xoffset
            #textbutton _("Start"):
            #  action Start()
            #  default_focus 1

        else:

            use gear_button("log.png", 0.4, new_xpos , new_yoffset ,  ShowMenu("history"))
            $new_yoffset = new_yoffset * -1
            $new_xpos = new_xpos + new_xoffset

            use gear_button("save.png", 0.4, new_xpos , new_yoffset ,  ShowMenu("save"))
            $new_yoffset = new_yoffset * -1
            $new_xpos = new_xpos + new_xoffset

        use gear_button("load.png", 0.4, new_xpos , new_yoffset ,  ShowMenu("load"))
        $new_yoffset = new_yoffset * -1
        $new_xpos = new_xpos + new_xoffset

        use gear_button("config.png", 0.4, new_xpos , new_yoffset ,  ShowMenu("preferences"))
        $new_yoffset = new_yoffset * -1
        $new_xpos = new_xpos + new_xoffset

        if _in_replay:

            use gear_button("End Replay", 0.4, new_xpos , new_yoffset ,  EndReplay(confirm=True))
            $new_yoffset = new_yoffset * -1
            $new_xpos = new_xpos + new_xoffset

        elif not main_menu:

            use gear_button("home.png", 0.4, new_xpos , new_yoffset ,  MainMenu())
            $new_yoffset = new_yoffset * -1
            $new_xpos = new_xpos + new_xoffset

        use gear_button("about.png", 0.4, new_xpos , new_yoffset ,  ShowMenu("about"))
        $new_yoffset = new_yoffset * -1
        $new_xpos = new_xpos + new_xoffset

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            use gear_button("help.png", 0.4, new_xpos , new_yoffset ,  ShowMenu("help"))
            $new_yoffset = new_yoffset * -1
            $new_xpos = new_xpos + new_xoffset

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            use gear_button("quit.png", 0.4, new_xpos , new_yoffset ,  Quit(confirm=not main_menu))
            $new_yoffset = new_yoffset * -1
            $new_xpos = new_xpos + new_xoffset


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"

    # default_focus doesn't work on button inside screen (gear_button)
    # so we use the manual method: add id to button and set_focus on show
    on "show" action Function(renpy.set_focus, 'main_menu', 'start')


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 0.5
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen menu_gears():

        use gear(8, 0.3, 230, 500,1,9)
        use gear(8, 0.3, 350, 580, -1,9)

        use gear(11, 0.6, 200, 500, -1,7)
        use gear(10, 0.6, 80, 450 ,1, 5)
        use gear(10, 0.6, 300, 600,1, 5)

        use gear(26, 1.0, 50, 500, -1)
        add "gui/overlay/options_menu_gem.png" yoffset -170 xoffset 15

screen menu_gears2():

        use gear(8, 0.3, -10, 250, 1, 9)
        use gear(8, 0.3, 80, 330, -1, 9)

        use gear(11, 0.6, 0, 180, -1, 7)
        use gear(14, 0.6, -50, 100, 1, 5)
        use gear(14, 0.6, 100, 250, 1, 5)

        use gear(26, 1.0, 0, 0, -1)
        add "gui/overlay/options_menu_gem.png" yoffset -670 xoffset -35

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

            frame:
                style "game_menu_navigation_frame"
    #add "gui/overlay/options_menu_bolts.png"
    use navigation
    if title == "Options":
      add "gui/overlay/options_menu_powerlines2.png" xoffset 4 yoffset 2
    if not title == "History" and not title == "Help":
      frame:
          background None
          yoffset 200
          xoffset -25
          use menu_gears()
      frame:
          background None
          yoffset -50
          xoffset 1450
          use menu_gears2()

    add "gui/overlay/options_menu_titlebox.png"
    label title text_color "#000000" xalign 0.5 yoffset 33 xoffset 3
    label title xalign 0.5 yoffset 30

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    #background "#123456"
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    #background "#223456"
    ysize 420
    xfill True

style game_menu_content_frame:
    #background "#323456"
    left_margin 230
    right_margin 230
    top_margin 0
    bottom_margin 160

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                yalign 0.2
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 0.8

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")
    foreground "gui/button/slot_idle_frame.png"
    hover_foreground "gui/button/slot_hover_frame.png"

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Options"), scroll="viewport"):
        vbox:
            xfill True
            xoffset 200
            yoffset 100

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"
                            xoffset 0
    #frame:
    #    background None
    #    yoffset 200
    #    xoffset -25
    #    use menu_gears()

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/button_[prefix_]foreground.png"
    xoffset 50

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/button_[prefix_]foreground.png"
    xoffset 50

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 336
    ysize 25
    left_bar "gui/slider/slider_full.png"
    right_bar "gui/slider/slider_empty.png"
    thumb None
    xoffset 50

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:
        xsize 725
        ysize 265
        
        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

    frame:
                  background None
                  xsize int(310*.4)
                  ysize int(310*.4)
                  xalign 0.4
                  yalign 0.55
                  use gear_button("Yes", 0.4, 0 , -20 ,  yes_action)
                  use gear_button("No", 0.4, 200 , -20 ,  no_action)

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background None #Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .45

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
