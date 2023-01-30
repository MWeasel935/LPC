
def tank_collision(obj, enemy_obj):
    if obj.get_rect().colliderect(enemy_obj.get_rect()):
        if abs(obj.get_rect().top - enemy_obj.get_rect().bottom) < 20:
            obj.set_top_collision(True)
            obj.move_bottom()
            obj.set_top_collision(False)

        if abs(obj.get_rect().bottom - enemy_obj.get_rect().top) < 20:
            obj.set_bottom_collision(True)
            obj.move_top()
            obj.set_bottom_collision(False)

        if abs(obj.get_rect().right - enemy_obj.get_rect().left) < 20:
            obj.set_right_collision(True)
            obj.move_left()
            obj.set_right_collision(False)

        if abs(obj.get_rect().left - enemy_obj.get_rect().right) < 20:
            obj.set_left_collision(True)
            obj.move_right()
            obj.set_left_collision(False)


def ball_collision(ball, wall_list):
    for wall in wall_list:
        if ball.get_rect().colliderect(wall):
            return True


def wall_collision(obj, rect):
    if obj.get_rect().colliderect(rect):

        if abs(rect.bottom - obj.get_rect().top) < 20:
            obj.set_top_collision(True)
            obj.move_bottom()
            obj.set_top_collision(False)

        if abs(obj.get_rect().bottom - rect.top) < 20:
            obj.set_bottom_collision(True)
            obj.move_top()
            obj.set_bottom_collision(False)

        if abs(obj.get_rect().right - rect.left) < 20:
            obj.set_right_collision(True)
            obj.move_left()
            obj.set_right_collision(False)

        if abs(obj.get_rect().left - rect.right) < 20:
            obj.set_left_collision(True)
            obj.move_right()
            obj.set_left_collision(False)

    else:
        obj.set_top_collision(False)
        obj.set_bottom_collision(False)
        obj.set_right_collision(False)
        obj.set_left_collision(False)
