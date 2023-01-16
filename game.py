from logging.config import listen
from sqlite3 import Time
from time import time
import pygame
from bullet import Bullet
from config import SCREEN_RECTS, TANK_1_COLOR, TANK_2_COLOR
from screen import Screen
from tank import Tank


class Game:
    def __init__(self) -> None:

        self.playing = True
        self.screen = Screen()
        self.score = (0, 0)

        self.clock = pygame.time.Clock()
        self.map = SCREEN_RECTS
        self.tank1 = Tank((45, 243), TANK_1_COLOR, pygame.K_LEFT,
                          pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN,
                          pygame.K_SPACE)
        self.tank2 = Tank((710, 243), TANK_2_COLOR, pygame.K_a,
                          pygame.K_w, pygame.K_d, pygame.K_s, pygame.K_q)

    def listen_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def listen_keyboard(self):
        self.tank1.move(
            self.map, self.tank2.get_rect())
        self.tank2.move(
            self.map, self.tank1.get_rect())

        if self.tank1.has_shooted_enemy() and not self.tank2.spin:
            self.tank2.spin = True
            self.score = (self.score[0] + 1, self.score[1])

        if self.tank2.has_shooted_enemy() and not self.tank2.spin:
            self.tank1.spin = True
            self.score = (self.score[0], self.score[1]+1)

    def loop(self):
        while self.playing:
            self.listen_events()
            self.listen_keyboard()

            self.screen.draw(self.map, self.score)
            self.tank1.draw(self.screen.arena)
            self.tank2.draw(self.screen.arena)

            pygame.display.flip()
            self.clock.tick(60)