import pygame

from config import BG_COLOR, RECTS_COLOR, SCREEN_HEIGHT, SCREEN_WIDTH, \
    TANK_1_COLOR, TANK_2_COLOR, TOP_BAR_HEIGHT


class Screen:
    surface: pygame.Surface

    def __init__(self) -> None:
        self.surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.arena = self.surface.subsurface(
            (0, TOP_BAR_HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT - TOP_BAR_HEIGHT))
        self.font = pygame.font.Font("font/Megafont.ttf", 54)

    def draw(self, map, score):
        self.surface.fill(BG_COLOR)

        score_p1 = self.font.render(
            str(score[0]), True, TANK_1_COLOR)
        score_p2 = self.font.render(
            str(score[1]), True, TANK_2_COLOR)

        self.surface.blit(score_p1, (220, 10))
        self.surface.blit(score_p2, (550, 10))

        for rect in map:
            pygame.draw.rect(self.arena, RECTS_COLOR, rect)