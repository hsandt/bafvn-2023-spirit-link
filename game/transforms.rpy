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
    transform character_move_left_exit(duration=1.0):
        easeout duration xpos -0.5

    transform character_warp_to(target_pos):
        xpos position_name_to_xpos_value(target_pos)
        ypos 1.0

    transform character_move_to(target_pos, duration=1.0):
        easeout duration xpos position_name_to_xpos_value(target_pos)
        ypos 1.0

    transform companion_warp_to(target_pos):
        anchor (0.5, 0.5)
        xpos position_name_to_xpos_value(target_pos)
        # companion flies or is on shoulder
        ypos 0.1

    transform companion_move_to(target_pos, duration=1.0):
        anchor (0.5, 0.5)
        easeout duration xpos position_name_to_xpos_value(target_pos)
        # companion flies or is on shoulder
        ypos 0.1

    transform half_size:
        xysize 0.5

    transform flip:
        xzoom -1.0

    transform darker:
        linear 0.1 matrixcolor TintMatrix("#888888")

    transform reset_brightness:
        linear 0.1 matrixcolor TintMatrix("#ffffff")
