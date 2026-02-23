# Images

## Overlay

image overlay black = Solid("#000000")
# Flash overlay - combine with flash transition for a full flash effect
image overlay flash = Solid("#ffffffd2")
image underlay white_half_alpha = Solid("#ffffff80")

## Backgrounds (1080p)

# Black background for scene transitions
image bg black = Solid("#000000")

# White background
image bg white = Solid("#ffffff")

screen white_overlay():
    # don't put on layer "overlay", that would make it disappear on scene change, so keep default
    # (layer "screens")
    add "bg white"

# Proto Solid
# image bg university_outside = Solid("#af9750")
# Replace with asset when ready
image bg university_outside = "images/bg/university_outside.webp"
image bg university_outside_with_characters_for_zoom = "images/bg/university_outside_with_characters_for_zoom.webp"

# Proto Solid
# image bg university_inside = Solid("#6d5e32")
# Replace with asset when ready
image bg university_inside = "images/bg/BG_Hall.webp"
# image bg university_inside = "images/bg/university_inside.webp"

image bg smoke = Solid("#d3d3d3")
# Replace with asset when ready
# image bg smoke = "images/bg/smoke.jpg"

image bg battle_splash = Solid("#a848b7")
# Replace with asset when ready
# image bg battle_splash = "images/bg/battle_splash.jpg"

image bg assassin_cloth = Solid("#bf4040")
# Replace with asset when ready
# image bg assassin_cloth = "images/bg/assassin_cloth.jpg"

# Useful if force showing standard overlays at some point (e.g. during credits)
image bg main_menu_overlay = "gui/overlay/main_menu.png"
image bg game_menu_overlay = "gui/overlay/game_menu.png"

## FX

# Smoke

transform smoke_particle_transform:
    # zpos 10
    zoom renpy.random.uniform(0.5, 1.0)
    rotate renpy.random.uniform(0.0, 360.0)
    pause 5.0
    easein 5.0 alpha 0.0

image fx smoke = SnowBlossom(At("images/fx/fx_smoke_particle.webp", smoke_particle_transform), count=500,
    xspeed=(-60, -10), yspeed=(-100, -50), start=10.0)

# Hack to make smoke appear above characters who appear later
screen smoke():
    layer "fx"
    add "fx smoke"

# We didn't use random rotation in the end since the animation was so short, but kept code
# for reference

init -1 python:
    def apply_random_rotation(transform, time_since_start, time_since_tag, /):
        transform.rotate = renpy.random.uniform(-5.0, 5.0)
        # Return interval (s) between calls to this function
        return 0.2

transform loop_random_rotation:
    xalign 0.5
    yalign 0.5

    function apply_random_rotation
    repeat

# Speed lines showing that camera is moving forward
# image fx speed_lines_forward = At("images/fx/speed_lines_forward_1080p.webp", loop_random_rotation)
image fx_speed_lines_forward = "images/fx/speed_lines_forward_1080p.webp"

image fx_fire_forward = "images/fx/fx_fire_forward.webp"
image fx_fan_summon_base_small = "images/fx/fx_fan_summon_base_small.webp"
image fx_fan_summon_halo_small = "images/fx/fx_fan_summon_halo_small.webp"

## Characters

# Humans place anchors at leg center, where screen bottom cuts them

# Charlet
image charlet neutral = Transform("images/chars/sc1080p_mc_neutral.png", zoom=0.95, anchor=(0.53, 0.67))
image charlet smile = Transform("images/chars/sc1080p_mc_neutral_smile.png", zoom=0.95, anchor=(0.53, 0.67))
image charlet scared = Transform("images/chars/sc1080p_mc_scared.png", zoom=0.95, anchor=(0.53, 0.67))
# TODO: use dedicated sprite when ready
image charlet exhausted = Transform("images/chars/sc1080p_mc_neutral.png", zoom=0.95, anchor=(0.53, 0.67))
# TODO: use dedicated sprite when ready
image charlet sad = Transform("images/chars/sc1080p_mc_neutral.png", zoom=0.95, anchor=(0.53, 0.67))
# TODO: use dedicated sprite when ready
image charlet surprised = Transform("images/chars/sc1080p_mc_scared.png", zoom=0.95, anchor=(0.53, 0.67))
# TODO: use dedicated sprite when ready
image charlet serious = Transform("images/chars/sc1080p_mc_neutral.png", zoom=0.95, anchor=(0.53, 0.67))
# TODO: use dedicated sprite when ready
image charlet intrigued = Transform("images/chars/sc1080p_mc_neutral.png", zoom=0.95, anchor=(0.53, 0.67))
# TODO: use dedicated sprite when ready
image charlet anxious = Transform("images/chars/sc1080p_mc_scared.png", zoom=0.95, anchor=(0.53, 0.67))
# TODO: use dedicated sprite when ready
image charlet relieved = Transform("images/chars/sc1080p_mc_neutral_smile.png", zoom=0.95, anchor=(0.53, 0.67))
image charlet shout = Transform("images/chars/sc1080p_mc_shout.png", zoom=0.95, anchor=(0.53, 0.67))
image charlet telepathy = Transform("images/chars/sc1080p_mc_telepathy.png", zoom=0.95, anchor=(0.53, 0.67))
image side charlet scared = Transform("images/chars/mc_scared_side.png", zoom=1.0)
image side charlet shout = Transform("images/chars/mc_shout_side.png", zoom=1.0)
image side charlet telepathy = Transform("images/chars/mc_telepathy_side.png", zoom=1.0)

# Pichit
image pichit neutral = Transform("images/chars/sc1080p_guide_neutral.png", zoom=0.95, anchor=(0.46, 0.67))
image pichit smile = Transform("images/chars/sc1080p_guide_smile.png", zoom=0.95, anchor=(0.46, 0.67))
image pichit intrigued = Transform("images/chars/sc1080p_guide_intrigued.png", zoom=0.95, anchor=(0.46, 0.67))
# TODO: use dedicated sprite when ready
image pichit surprised = Transform("images/chars/sc1080p_guide_intrigued.png", zoom=0.95, anchor=(0.46, 0.67))
# TODO: use dedicated sprite when ready
image pichit exhausted = Transform("images/chars/sc1080p_guide_intrigued.png", zoom=0.95, anchor=(0.46, 0.67))
image pichit battle serious = Transform("images/chars/sc1080p_guide_battle_serious.png", zoom=0.95, anchor=(0.59, 0.67))
image pichit battle grimace = Transform("images/chars/sc1080p_guide_battle_grimace.png", zoom=0.95, anchor=(0.59, 0.67))
image pichit battle anxious = Transform("images/chars/sc1080p_guide_battle_anxious.png", zoom=0.95, anchor=(0.59, 0.67))
image pichit battle shout = Transform("images/chars/sc1080p_guide_battle_shout.png", zoom=0.95, anchor=(0.59, 0.67))
# TODO: use dedicated sprite when ready
image pichit battle smile = Transform("images/chars/sc1080p_guide_battle_serious.png", zoom=0.95, anchor=(0.59, 0.67))

# Raegan
# Hack: official bottom screen line should be at 0.75 according to artwork scale, but we set 0.7
# So Raegan doesn't look too tall compared to Charlet and Pichit
image raegan neutral = Transform("images/chars/sc1080p_lobbyist_neutral.png", zoom=0.95, anchor=(0.45, 0.7))
image raegan smile = Transform("images/chars/sc1080p_lobbyist_smile.png", zoom=0.95, anchor=(0.45, 0.7))
image raegan intrigued = Transform("images/chars/sc1080p_lobbyist_intrigued.png", zoom=0.95, anchor=(0.45, 0.7))
image raegan thinking = Transform("images/chars/sc1080p_lobbyist_thinking.png", zoom=0.95, anchor=(0.45, 0.7))
image raegan surprised = Transform("images/chars/sc1080p_lobbyist_surprised.png", zoom=0.95, anchor=(0.45, 0.7))
image raegan anxious = Transform("images/chars/sc1080p_lobbyist_anxious.png", zoom=0.95, anchor=(0.45, 0.7))
# TODO: use dedicated sprite when ready (currently, intrigued look more like sad than intrigued)
image raegan sad = Transform("images/chars/sc1080p_lobbyist_intrigued.png", zoom=0.95, anchor=(0.45, 0.7))

# Phrarat
# Hack: official bottom screen line should be at 0.70 but for some reason (zoom?) character still looks too big
# so got to set anchor Y to 0.65
image phrarat neutral = Transform("images/chars/sc1080p_assassin_neutral.png", zoom=0.95, anchor=(0.46, 0.65))
image phrarat smile = Transform("images/chars/sc1080p_assassin_smile.png", zoom=0.95, anchor=(0.46, 0.65))
image phrarat determined = Transform("images/chars/sc1080p_assassin_determined.png", zoom=0.95, anchor=(0.46, 0.65))
image phrarat surprised = Transform("images/chars/sc1080p_assassin_surprised.png", zoom=0.95, anchor=(0.46, 0.65))
image phrarat anxious = Transform("images/chars/sc1080p_assassin_anxious.png", zoom=0.95, anchor=(0.46, 0.65))
image phrarat shout = Transform("images/chars/sc1080p_assassin_shout.png", zoom=0.95, anchor=(0.46, 0.65))
image phrarat silhouette = Transform("images/chars/sc1080p_assassin_silhouette.webp", zoom=0.95, anchor=(0.46, 0.65))

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
    define audio.premonition = "<loop 5.581>audio/bgm/Premonition_v0.1_intro_5.581-loop_end.opus"

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
    define audio.sfx.fire = "audio/sfx/sfx_fire.opus"
    define audio.sfx.fire_blast = "audio/sfx/sfx_fire_blast.opus"
    define audio.sfx.hit = "audio/sfx/sfx_hit.opus"
    define audio.sfx.impact1 = "audio/sfx/sfx_impact1.opus"
    define audio.sfx.impact2 = "audio/sfx/sfx_impact2.opus"
    define audio.sfx.impact3 = "audio/sfx/sfx_impact3.opus"
    define audio.sfx.impact_catch = "audio/sfx/sfx_impact_catch.opus"
    define audio.sfx.impact_glass = "audio/sfx/sfx_impact_glass.opus"
    define audio.sfx.running = "audio/sfx/sfx_running.opus" # unused, but kept for longer running with breath
    define audio.sfx.running2 = "audio/sfx/sfx_running2.opus"
    define audio.sfx.scarf = "audio/sfx/sfx_scarf.opus"
    define audio.sfx.shower = "audio/sfx/sfx_shower.opus" # unused, but kept for continuous rain
    define audio.sfx.shower2 = "audio/sfx/sfx_shower2.opus"
    define audio.sfx.slash1 = "audio/sfx/sfx_slash1.opus"
    define audio.sfx.slash2 = "audio/sfx/sfx_slash2.opus"
    define audio.sfx.slash3 = "audio/sfx/sfx_slash3.opus"
    define audio.sfx.slash_impact1 = "audio/sfx/sfx_slash_impact1.opus"
    define audio.sfx.slash_impact2 = "audio/sfx/sfx_slash_impact2.opus"
    define audio.sfx.slash_impact3 = "audio/sfx/sfx_slash_impact3.opus"
    define audio.sfx.smoke = "audio/sfx/sfx_smoke.opus"
    define audio.sfx.summon = "audio/sfx/sfx_summon.opus"
    define audio.sfx.swift_move1 = "audio/sfx/sfx_swift_move1_no_lag.opus"
    define audio.sfx.swift_move2 = "audio/sfx/sfx_swift_move2.opus"
    define audio.sfx.throw_fireball = "audio/sfx/sfx_throw_fireball.opus"
    define audio.sfx.vines = "audio/sfx/sfx_vines.opus"

    ## SFX mapping (to allow to reuse audio assets for actions with different meanings,
    ## and also so accessibility feature can use short name as dict key rather than filepath)
    define sfx_to_assets = dict(
        # slash = audio.slash,
    )

init python:
    # Shaders

    renpy.register_shader("camera_zoom", variables="""
        attribute vec4 a_position;
        uniform sampler2D tex0;
        uniform vec2 u_model_size;
        uniform float u_zoom_out_power;
        varying vec2 v_uv_rel;
    """, vertex_300="""
        v_uv_rel = a_position.xy / u_model_size - 0.5;
    """, fragment_300="""
        vec2 v_edge_projected;
        float v_squared_ratio_to_edge;
        vec2 v_transformed_uv;
        v_edge_projected = 0.5 * vec2(
            clamp(v_uv_rel.x / abs(v_uv_rel.y), -1.0, 1.0),
            clamp(v_uv_rel.y / abs(v_uv_rel.x), -1.0, 1.0)
        );
        v_squared_ratio_to_edge = dot(v_uv_rel, v_uv_rel) / dot(v_edge_projected, v_edge_projected);
        v_transformed_uv = 0.5 + pow(v_squared_ratio_to_edge, 0.5 * (1.0 / u_zoom_out_power - 1.0)) * v_uv_rel;

        gl_FragColor = texture2D(tex0, v_transformed_uv);
    """)
