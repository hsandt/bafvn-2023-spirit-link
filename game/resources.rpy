# Images

## Overlay

image overlay black = Solid("#000000")
image underlay white_half_alpha = Solid("#ffffff80")

## Backgrounds (1080p)

# image bg shop = "images/bg/shop.jpg"

# Useful if force showing standard overlays at some point (e.g. during credits)
image bg main_menu_overlay = "gui/overlay/main_menu.jpg"
image bg game_menu_overlay = "gui/overlay/game_menu.jpg"

## Characters

image charlet neutral = Transform("images/chars/mc proto.png", zoom=0.5)
image pichit neutral = Transform("images/chars/guide proto.png", zoom=0.5)
image raegan neutral = Transform("images/chars/lobbyist proto.png", zoom=0.5)
image phrarat neutral = Transform("images/chars/assassin proto.png", zoom=0.5)



# Audio

# -1 so it's done just before music_dictionary definition in accessibility_setup.rpy
init -1:
    ## BGM assets
    # define audio.title_theme = "<loop 19.2>audio/bgm/bgm_title.ogg"
    # define audio.chill = "<loop 199.92>audio/bgm/bgm_chill.ogg"

    ## BGM mapping (so accessibility feature can get BGM notification text from core name
    ## instead of filepath, which contains the <loop> pattern and is not very convenient)
    define music_to_assets = dict(
        # title = audio.title,
        # chill = audio.chill,
    )

    ## SFX assets
    # define audio.slash = "audio/sfx/sfx_slash.ogg"

    ## SFX mapping (to allow to reuse audio assets for actions with different meanings,
    ## and also so accessibility feature can use short name as dict key rather than filepath)
    define sfx_to_assets = dict(
        # slash = audio.slash,
    )
