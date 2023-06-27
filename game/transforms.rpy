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
    # Move character to left until it exits screen
    # Remember to hide it afterward to avoid keeping the sprite in memory,
    # unless you make it reenter soon
    transform character_exit_to_left(duration=1.0):
        linear duration xpos -0.5
    transform character_exit_to_left_easeout(duration=1.0):
        easeout duration xpos -0.5

    # Move character to right until it exits screen
    # Remember to hide it afterward to avoid keeping the sprite in memory,
    # unless you make it reenter soon
    transform character_exit_to_right(duration=1.0):
        linear duration xpos -0.5
    transform character_exit_to_right_easeout(duration=1.0):
        easeout duration xpos -0.5

    # Move character from outside left to target position
    transform character_enter_from_left_to(target_pos, duration=1.0):
        xpos 0.5
        easein duration xpos position_name_to_xpos_value(target_pos)

    # Move character from outside right to target position
    transform character_enter_from_right_to(target_pos, duration=1.0):
        xpos 0.5
        easein duration xpos position_name_to_xpos_value(target_pos)

    transform character_warp_to(target_pos, fade_duration=0.5):
        xpos position_name_to_xpos_value(target_pos)
        ypos 1.0
        alpha 0.0
        easein fade_duration alpha 1.0

    transform character_move_to(target_pos, duration=1.0):
        easein duration xpos position_name_to_xpos_value(target_pos)
        ypos 1.0

    transform companion_warp_to(target_pos):
        anchor (0.5, 0.5)
        xpos position_name_to_xpos_value(target_pos)
        # companion flies or is on shoulder
        ypos 0.2

    transform companion_move_to(target_pos, duration=1.0):
        anchor (0.5, 0.5)
        easein duration xpos position_name_to_xpos_value(target_pos)
        # companion flies or is on shoulder
        ypos 0.2

    transform half_size:
        xysize 0.5

    transform flip:
        xzoom -1.0

    transform darker:
        linear 0.1 matrixcolor TintMatrix("#888888")

    transform reset_brightness:
        linear 0.1 matrixcolor TintMatrix("#ffffff")

    transform bump_left:
        linear 0.1 xoffset -50
        linear 0.2 xoffset 0
