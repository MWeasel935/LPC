import pygame
from tank import Tank
import arena
import collision

GREEN = (100, 200, 75)
BLUE = (50, 75, 200)
BACKGROUND = (100, 30, 10)
MAP_COLOR = (200, 150, 50)


class Game:
    def __init__(self) -> None:

        self.width = 1280
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Combat - Tank")

        self.game_over = False
        self.game_loop = True

        self.player_1 = Tank(180, 400, GREEN)
        self.player_2 = Tank(1100, 400, BLUE)
        self.bullets_1 = self.player_1.get_player_bullets()
        self.bullets_2 = self.player_2.get_player_bullets()

        self.wall_list = arena.create_arena()
        self.tank_list = [self.player_1, self.player_2]

        self.font = pygame.font.Font("Font/Press_Start.ttf", 54)
        self.score_1 = 0
        self.score_2 = 0
        self.clock = pygame.time.Clock()

    def draw_hud(self):
        score_p1 = self.font.render(str(self.score_1), True, GREEN)
        score_p2 = self.font.render(str(self.score_2), True, BLUE)

        self.screen.blit(score_p1, (350, 15))
        self.screen.blit(score_p2, (930, 15))

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_loop = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    if not self.game_over:
                        self.player_1.shoot()
                if event.key == pygame.K_SPACE:
                    if not self.game_over:
                        self.player_2.shoot()

    def keyboard_binding(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.player_1.turn_left()
        if keys[pygame.K_d]:
            self.player_1.turn_right()
        if keys[pygame.K_w]:
            self.player_1.move()

        if keys[pygame.K_LEFT]:
            self.player_2.turn_left()
        if keys[pygame.K_RIGHT]:
            self.player_2.turn_right()
        if keys[pygame.K_UP]:
            self.player_2.move()

    def main_loop(self):
        while self.game_loop:
            if not self.game_over:
                for b in self.bullets_1:
                    b.move()
                for b in self.bullets_2:
                    b.move()

            self.screen.fill(BACKGROUND)

            for b in self.bullets_1:
                if collision.ball_collision(b, self.wall_list):
                    self.bullets_1.remove(b)
                if b.rect.colliderect(self.player_2.rect):
                    self.score_2 += 1
                    self.bullets_1.remove(b)
                b.draw(self.screen)

            for b in self.bullets_2:
                if collision.ball_collision(b, self.wall_list):
                    self.bullets_2.remove(b)
                if b.rect.colliderect(self.player_1.rect):
                    self.score_1 += 1
                    self.bullets_2.remove(b)
                b.draw(self.screen)

            collision.tank_collision(self.player_1, self.player_2)
            collision.tank_collision(self.player_2, self.player_1)

            for wall in self.wall_list:
                collision.wall_collision(self.player_1, wall)
                collision.wall_collision(self.player_2, wall)

            for wall in self.wall_list:
                pygame.draw.rect(self.screen, MAP_COLOR, wall)

            self.player_1.draw(self.screen)
            self.player_2.draw(self.screen)

            self.draw_hud()

            self.get_events()
            self.keyboard_binding()

            pygame.display.update()
            self.clock.tick(60)
