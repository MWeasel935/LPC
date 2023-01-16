import pygame

from config import SPEED


class Bullet:
    size = 5
    speed = 5
    collided_tank = False
    pygame.mixer.init()

    def __init__(self, x, y,  x_direction, y_direction) -> None:
        self.x = x
        self.y = y
        self.x_velocity = x_direction * self.speed
        self.y_velocity = y_direction * self.speed
        self.x_direction = x_direction if x_direction >= 0 else -x_direction
        self.y_direction = y_direction if y_direction >= 0 else -y_direction
        self.start_time = pygame.time.get_ticks()
        self.end_life = False
        self.sound_collision = pygame.mixer.Sound('sound/collision.mp3')
        self.sound_collision.set_volume(0.4)

    def is_colliding_walls(self, map):
        for rect in map:
            is_in_x = self.x >= rect[0] and self.x + \
                self.size <= rect[0] + rect[2]
            is_in_y = self.y >= rect[1] and self.y + \
                self.size <= rect[1] + rect[3]

            if is_in_x and self.y + self.size >= rect[1] and \
                    self.y + self.size <= rect[1] + rect[3]:
                self.y_velocity = -self.y_direction * self.speed
                pygame.mixer.Channel(0).play(self.sound_collision)
            if is_in_x and self.y <= rect[1] + rect[3] and self.y >= rect[1]:
                self.y_velocity = self.y_direction * self.speed
                pygame.mixer.Channel(0).play(self.sound_collision)

            if is_in_y and self.x <= rect[0] + rect[2] and self.x >= rect[0]:
                self.x_velocity = self.x_direction * self.speed
                pygame.mixer.Channel(0).play(self.sound_collision)
            if is_in_y and self.x + self.size >= rect[0] and \
                    self.x + self.size <= rect[0] + rect[2]:
                self.x_velocity = -self.x_direction * self.speed
                pygame.mixer.Channel(0).play(self.sound_collision)

    def is_colliding_tank(self, tank_rect):
        self.collided_tank = pygame.Rect(
            self.x, self.y, self.size, self.size).colliderect(tank_rect)

    def move(self, map, tank):
        self.is_colliding_walls(map)
        self.is_colliding_tank(tank)

        self.x += self.x_velocity
        self.y += self.y_velocity

        if (pygame.time.get_ticks() - self.start_time)/1000 >= 3:
            self.end_life = True

    def get_rect(self):
        return (self.x, self.y, self.size, self.size)