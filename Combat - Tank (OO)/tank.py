import pygame
import math
import bullet


class Tank(object):
    def __init__(self, x, y, color):
        self.img = pygame.image.load("Sprites/tank2.png")
        self.img.fill(color, None, pygame.BLEND_MAX)
        self.color = color
        self.w = self.img.get_width()
        self.h = self.img.get_height()
        self.x = x
        self.y = y
        self.rect = (self.x, self.y, self.w, self.h)
        self.angle = 0
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2,
                     self.y - self.sine * self.h // 2)
        self.tankBullets = []
        self.top_collision = False
        self.bottom_collision = False
        self.right_collision = False
        self.left_collision = False

    def draw(self, screen):
        screen.blit(self.rotatedSurf, self.rotatedRect)

    def turn_left(self):
        self.angle += 5
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2,
                     self.y - self.sine * self.h // 2)

    def turn_right(self):
        self.angle -= 5
        self.rotatedSurf = pygame.transform.rotate(self.img, self.angle)
        self.rotatedRect = self.rotatedSurf.get_rect()
        self.rotatedRect.center = (self.x, self.y)
        self.cosine = math.cos(math.radians(self.angle + 90))
        self.sine = math.sin(math.radians(self.angle + 90))
        self.head = (self.x + self.cosine * self.w // 2,
                     self.y - self.sine * self.h // 2)

    def move_bottom(self):
        if self.top_collision is True:
            self.y = self.y + 4
            self.top_collision = False
            self.rect = (self.x, self.y, self.w, self.h)

    def move_top(self):
        if self.bottom_collision is True:
            self.y = self.y - 4
            self.bottom_collision = False
            self.rect = (self.x, self.y, self.w, self.h)

    def move_left(self):
        if self.right_collision is True:
            self.x = self.x - 4
            self.y = self.y
            self.right_collision = False
            self.rect = (self.x, self.y, self.w, self.h)

    def move_right(self):
        if self.left_collision is True:
            self.x = self.x + 4
            self.y = self.y
            self.left_collision = False
            self.rect = (self.x, self.y, self.w, self.h)

    def move(self):

        if self.top_collision is True or self.bottom_collision is True or self.right_collision is True \
                or self.left_collision is True:
            pass
        else:
            self.x += self.cosine * 6
            self.y -= self.sine * 6

            self.rotatedRect = self.rotatedSurf.get_rect()
            self.rotatedRect.center = (self.x, self.y)
            self.cosine = math.cos(math.radians(self.angle + 90))
            self.sine = math.sin(math.radians(self.angle + 90))
            self.head = (self.x + self.cosine * self.w // 2,
                         self.y - self.sine * self.h // 2)
            self.rect = (self.x, self.y, self.w, self.h)

    def shoot(self):
        self.tankBullets.append(bullet.Bullet(self.head, self.cosine,
                                              self.sine))

    def get_player_bullets(self):
        return self.tankBullets

    def get_rect(self):
        return self.rotatedRect

    def set_top_collision(self, boolean):
        self.top_collision = boolean

    def set_bottom_collision(self, boolean):
        self.bottom_collision = boolean

    def set_right_collision(self, boolean):
        self.right_collision = boolean

    def set_left_collision(self, boolean):
        self.left_collision = boolean
