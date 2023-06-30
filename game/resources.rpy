# Images

## Overlay

image overlay black = Solid("#000000")
image underlay white_half_alpha = Solid("#ffffff80")

## Backgrounds (1080p)

# Black background for scene transitions
image bg black = Solid("#000000")

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

# Humans place anchors at leg center, where screen bottom cuts them

# Charlet
image charlet neutral = Transform("images/chars/sc1080p_mc_neutral.png", zoom=0.95, anchor=(0.53, 0.67))
image charlet smile = Transform("images/chars/sc1080p_mc_scared.png", zoom=0.95, anchor=(0.53, 0.67))
# TODO: use dedicated sprite when ready
image charlet exhausted = Transform("images/chars/sc1080p_mc_neutral.png", zoom=0.95, anchor=(0.53, 0.67))
# TODO: use dedicated sprite when ready
image charlet sad = Transform("images/chars/sc1080p_mc_neutral.png", zoom=0.95, anchor=(0.53, 0.67))
# TODO: use dedicated sprite when ready
image charlet surprised = Transform("images/chars/sc1080p_mc_scared.png", zoom=0.95, anchor=(0.53, 0.67))
# TODO: use dedicated sprite when ready
image charlet intrigued = Transform("images/chars/sc1080p_mc_neutral.png", zoom=0.95, anchor=(0.53, 0.67))
image charlet scared = Transform("images/chars/sc1080p_mc_scared.png", zoom=0.95, anchor=(0.53, 0.67))
image charlet shout = Transform("images/chars/sc1080p_mc_shout.png", zoom=0.95, anchor=(0.53, 0.67))
image charlet telepathy = Transform("images/chars/sc1080p_mc_telepathy.png", zoom=0.95, anchor=(0.53, 0.67))
image side charlet shout = Transform("images/chars/mc_shout_side.png", zoom=1.0)
image side charlet telepathy = Transform("images/chars/mc_telepathy_side.png", zoom=1.0)

# Pichit
image pichit neutral = Transform("images/chars/sc1080p_guide_neutral.png", zoom=0.95, anchor=(0.46, 0.67))
image pichit smile = Transform("images/chars/sc1080p_guide_smile.png", zoom=0.95, anchor=(0.46, 0.67))
image pichit intrigued = Transform("images/chars/sc1080p_guide_intrigued.png", zoom=0.95, anchor=(0.46, 0.67))
# TODO: use dedicated sprite when ready
image pichit surprised = Transform("images/chars/sc1080p_guide_intrigued.png", zoom=0.95, anchor=(0.46, 0.67))
image pichit battle serious = Transform("images/chars/sc1080p_guide_battle_serious.png", zoom=0.95, anchor=(0.59, 0.67))
image pichit battle grimace = Transform("images/chars/sc1080p_guide_battle_grimace.png", zoom=0.95, anchor=(0.59, 0.67))
image pichit battle anxious = Transform("images/chars/sc1080p_guide_battle_anxious.png", zoom=0.95, anchor=(0.59, 0.67))
image pichit battle shout = Transform("images/chars/sc1080p_guide_battle_shout.png", zoom=0.95, anchor=(0.59, 0.67))
# TODO: use dedicated sprite when ready
image pichit battle smile = Transform("images/chars/sc1080p_guide_battle_serious.png", zoom=0.95, anchor=(0.59, 0.67))

# Raegan
image raegan neutral = Transform("images/chars/sc1080p_lobbyist_neutral.png", zoom=0.95, anchor=(0.45, 0.75))
image raegan smile = Transform("images/chars/sc1080p_lobbyist_smile.png", zoom=0.95, anchor=(0.45, 0.75))
image raegan intrigued = Transform("images/chars/sc1080p_lobbyist_intrigued.png", zoom=0.95, anchor=(0.45, 0.75))
image raegan thinking = Transform("images/chars/sc1080p_lobbyist_thinking.png", zoom=0.95, anchor=(0.45, 0.75))
image raegan surprised = Transform("images/chars/sc1080p_lobbyist_surprised.png", zoom=0.95, anchor=(0.45, 0.75))
image raegan anxious = Transform("images/chars/sc1080p_lobbyist_anxious.png", zoom=0.95, anchor=(0.45, 0.75))

# Phrarat
image phrarat neutral = Transform("images/chars/assassin proto.png", zoom=0.42, anchor=(0.46, 0.70))
# TODO: use dedicated sprite when ready
image phrarat smile = Transform("images/chars/assassin proto.png", zoom=0.42, anchor=(0.46, 0.70))
# TODO: use dedicated sprite when ready
image phrarat determined = Transform("images/chars/assassin proto.png", zoom=0.42, anchor=(0.46, 0.70))
# TODO: use dedicated sprite when ready
image phrarat surprised = Transform("images/chars/assassin proto.png", zoom=0.42, anchor=(0.46, 0.70))
# TODO: use dedicated sprite when ready
image phrarat anxious = Transform("images/chars/assassin proto.png", zoom=0.42, anchor=(0.46, 0.70))
# TODO: use dedicated sprite when ready
image phrarat shout = Transform("images/chars/assassin proto.png", zoom=0.42, anchor=(0.46, 0.70))

# Spirits place anchors at center
image makara neutral = Transform("images/chars/mc spirit draft 1.png", zoom=0.6, anchor=(0.7, 0.51))
image fan neutral = Transform("images/chars/guide spirit draft 1.png", zoom=1.0, anchor=(0.4, 0.3))
image pen neutral = Transform("images/chars/assassin spirit draft 1.png", zoom=0.5, anchor=(0.62, 0.59))


# Audio

# -1 so it's done just before music_dictionary definition in accessibility_setup.rpy
init -1:
    ## BGM assets
    # define audio.title_theme = "<loop 19.2>audio/bgm/Title.ogg"
    define audio.battle = "<loop 1.807 to 72.289>audio/bgm/Storm Soul.ogg"
    define audio.mystery = "<loop 8.000 to 80.000>audio/bgm/Lore Forgotten.ogg"

    ## BGM mapping (so accessibility feature can get BGM notification text from core name
    ## instead of filepath, which contains the <loop> pattern and is not very convenient)
    define music_to_assets = dict(
        # title = audio.title,
        # chill = audio.chill,
    )

    ## SFX assets
    define audio.sfx.blade_clash1 = "audio/sfx/sfx_blade_clash1.opus"
    define audio.sfx.blade_clash2 = "audio/sfx/sfx_blade_clash2.opus"
    define audio.sfx.block_punch = "audio/sfx/sfx_block_punch.opus"
    define audio.sfx.block_shield1 = "audio/sfx/sfx_block_shield1.opus"
    define audio.sfx.block_shield2 = "audio/sfx/sfx_block_shield2.opus"
    # TODO: use dedicated asset when ready
    define audio.sfx.catch = "audio/sfx/sfx_hit.opus"
    define audio.sfx.fire = "audio/sfx/sfx_fire.opus"
    define audio.sfx.fire_blast = "audio/sfx/sfx_fire_blast.opus"
    define audio.sfx.hit = "audio/sfx/sfx_hit.opus"
    define audio.sfx.impact1 = "audio/sfx/sfx_impact1.opus"
    define audio.sfx.impact2 = "audio/sfx/sfx_impact2.opus"
    define audio.sfx.impact3 = "audio/sfx/sfx_impact3.opus"
    define audio.sfx.running = "audio/sfx/sfx_running.opus"
    define audio.sfx.scarf = "audio/sfx/sfx_scarf.opus"
    define audio.sfx.shower = "audio/sfx/sfx_shower.opus"
    define audio.sfx.slash1 = "audio/sfx/sfx_slash1.opus"
    define audio.sfx.slash2 = "audio/sfx/sfx_slash2.opus"
    define audio.sfx.slash3 = "audio/sfx/sfx_slash3.opus"
    define audio.sfx.slash_impact1 = "audio/sfx/sfx_slash_impact1.opus"
    define audio.sfx.slash_impact2 = "audio/sfx/sfx_slash_impact2.opus"
    define audio.sfx.slash_impact3 = "audio/sfx/sfx_slash_impact3.opus"
    define audio.sfx.smoke = "audio/sfx/sfx_smoke.opus"
    define audio.sfx.summon = "audio/sfx/sfx_summon.opus"
    define audio.sfx.swift_move1 = "audio/sfx/sfx_swift_move1.opus"
    define audio.sfx.swift_move2 = "audio/sfx/sfx_swift_move2.opus"
    define audio.sfx.throw_fireball = "audio/sfx/sfx_throw_fireball.opus"
    define audio.sfx.vines = "audio/sfx/sfx_vines.opus"

    ## SFX mapping (to allow to reuse audio assets for actions with different meanings,
    ## and also so accessibility feature can use short name as dict key rather than filepath)
    define sfx_to_assets = dict(
        # slash = audio.slash,
    )
