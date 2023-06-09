init python:
    position_dict = {
        "far_left": 0.1,
        "left": 0.23,
        "middle_left": 0.37,
        "middle": 0.5,
        "middle_right": 0.63,
        "right": 0.77,
        "far_right": 0.9,
    }

    def position_name_to_xpos_value(position_name):
        if position_name in position_dict:
            return position_dict[position_name]
        else:
            raise ValueError(f"Invalid position_name: {position_name}")

init:
    transform character_warp_to(target_pos, fade_duration=0.5):
        xpos position_name_to_xpos_value(target_pos)
        ypos 1.0
        # fade in
        alpha 0.0
        easein fade_duration alpha 1.0

    transform companion_warp_to(target_pos, fade_duration=0.5):
        xpos position_name_to_xpos_value(target_pos)
        # companion flies or is on shoulder
        ypos 0.2
        # fade in
        alpha 0.0
        easein fade_duration alpha 1.0

    # Move transforms
    # We assume all characters are opaque when moving, so to avoid issue with character
    # being stuck in interrupted alpha transition after a warp, we force set alpha 1.0
    # See https://github.com/renpy/renpy/issues/4790

    # Move character to left until it exits screen
    # Remember to hide it afterward to avoid keeping the sprite in memory,
    # unless you make it reenter soon
    transform character_exit_to_left(duration=1.0):
        alpha 1.0
        linear duration xpos -0.5
    transform character_exit_to_left_easeout(duration=1.0):
        alpha 1.0
        easeout duration xpos -0.5

    # Move character to right until it exits screen
    # Remember to hide it afterward to avoid keeping the sprite in memory,
    # unless you make it reenter soon
    transform character_exit_to_right(duration=1.0):
        alpha 1.0
        linear duration xpos -0.5
    transform character_exit_to_right_easeout(duration=1.0):
        alpha 1.0
        easeout duration xpos -0.5

    # Move character from outside left to target position
    transform character_enter_from_left_to(target_pos, duration=1.0):
        alpha 1.0
        xpos 0.5
        linear duration xpos position_name_to_xpos_value(target_pos)

    # Move character from outside right to target position
    transform character_enter_from_right_to(target_pos, duration=1.0):
        alpha 1.0
        xpos 0.5
        linear duration xpos position_name_to_xpos_value(target_pos)

    transform character_move_to(target_pos, duration=1.0, _xpos_offset=0.0):
        alpha 1.0
        linear duration xpos position_name_to_xpos_value(target_pos) + _xpos_offset
        ypos 1.0
    transform character_move_to_easein(target_pos, duration=1.0, _xpos_offset=0.0):
        alpha 1.0
        easein duration xpos position_name_to_xpos_value(target_pos) + _xpos_offset
        ypos 1.0
    transform character_move_to_easein_elastic(target_pos, duration=1.0, _xpos_offset=0.0):
        alpha 1.0
        easein_elastic duration xpos position_name_to_xpos_value(target_pos) + _xpos_offset
        ypos 1.0
    transform character_move_to_easeout_elastic(target_pos, duration=1.0, _xpos_offset=0.0):
        alpha 1.0
        easeout_elastic duration xpos position_name_to_xpos_value(target_pos) + _xpos_offset
        ypos 1.0

    # Move companion (higher in the air)
    transform companion_move_to(target_pos, duration=1.0):
        alpha 1.0
        linear duration xpos position_name_to_xpos_value(target_pos)
        # companion flies or is on shoulder
        ypos 0.2

    # Short moves

    transform bump_left(move_duration=0.1, come_back_duration=0.2):
        alpha 1.0
        linear move_duration xoffset -50
        linear come_back_duration xoffset 0

    transform bump_right(move_duration=0.1, come_back_duration=0.2):
        alpha 1.0
        linear move_duration xoffset 50
        linear come_back_duration xoffset 0

    transform fall_left(hop_backward_duration=0.2, fall_duration=0.1):
        alpha 1.0
        easein hop_backward_duration offset (-100, -50)
        easein_elastic fall_duration yoffset 300

    # Misc utilities

    transform half_size:
        xysize 0.5

    transform flip:
        xzoom -1.0

    transform darker:
        # Assume we start at normal color so init to that value to allow transition
        # ` * SaturationMatrix(1.0)` is only to allow future saturation transition
        # See https://www.renpy.org/doc/html/matrixcolor.html#structural-similarity
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 1.0 matrixcolor TintMatrix("#888888") * SaturationMatrix(1.0)

    transform reset_brightness:
        linear 1.0 matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)

    transform sepia:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
        linear 0.5 matrixcolor SepiaMatrix()
