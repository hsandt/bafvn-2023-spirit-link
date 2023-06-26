# Images

## Overlay

image overlay black = Solid("#000000")
image underlay white_half_alpha = Solid("#ffffff80")

## Backgrounds (1080p)

image bg university_outside = Solid("#af9750")
# Replace with asset when ready
# image bg university_outside = "images/bg/university_outside.jpg"

image bg university_inside = Solid("#6d5e32")
# Replace with asset when ready
# image bg university_inside = "images/bg/university_inside.jpg"

image bg smoke = Solid("#9f9f9f")
# Replace with asset when ready
# image bg smoke = "images/bg/smoke.jpg"

image bg battle_splash = Solid("#a848b7")
# Replace with asset when ready
# image bg battle_splash = "images/bg/battle_splash.jpg"

image bg assassin_cloth = Solid("#bf4040")
# Replace with asset when ready
# image bg assassin_cloth = "images/bg/assassin_cloth.jpg"

# Useful if force showing standard overlays at some point (e.g. during credits)
image bg main_menu_overlay = "gui/overlay/main_menu.jpg"
image bg game_menu_overlay = "gui/overlay/game_menu.jpg"

## Characters

# Charlet
image charlet neutral = Transform("images/chars/mc_neutral.png", zoom=0.4, anchor=(0.53, 0.735))
image charlet scared = Transform("images/chars/mc_scared.png", zoom=0.4, anchor=(0.53, 0.735))
image charlet shout = Transform("images/chars/mc_shout.png", zoom=0.4, anchor=(0.53, 0.735))
image side charlet shout = Transform("images/chars/mc_shout_side.png", zoom=1.0)
image charlet smile = Transform("images/chars/mc_smile.png", zoom=0.4, anchor=(0.53, 0.735))
image charlet telepathy = Transform("images/chars/mc_telepathy.png", zoom=0.4, anchor=(0.53, 0.735))
image side charlet telepathy = Transform("images/chars/mc_telepathy_side.png", zoom=1.0)

image pichit neutral = Transform("images/chars/guide proto.png", zoom=0.4, anchor=(0.5, 0.76))
image raegan neutral = Transform("images/chars/lobbyist proto.png", zoom=0.4, anchor=(0.45, 0.75))
image phrarat neutral = Transform("images/chars/assassin proto.png", zoom=0.4, anchor=(0.46, 0.71))
image makara neutral = Transform("images/chars/mc spirit draft 1.png", zoom=0.7)
image fan neutral = Transform("images/chars/guide spirit draft 1.png", zoom=1.0)
image pen neutral = Transform("images/chars/assassin spirit draft 1.png", zoom=0.5)


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
