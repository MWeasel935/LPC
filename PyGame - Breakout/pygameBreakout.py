# pygame setup
import pygame
import random
import math

pygame.init()

# colors
BLACK = (0, 0, 0)
RED = (200, 0, 0)
ORANGE = (200, 100, 0)
YELLOW = (200, 200, 0)
GREEN = (0, 125, 25)
BLUE = (0, 150, 200)
WHITE = (255, 255, 255)

# score and lives
score = 0
lives = 3

# window setup
width = 600
height = 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Breakout")
clock = pygame.time.Clock()

# sound setup
bounce_block_sound = pygame.mixer.Sound("sounds/brick.wav")
bounce_paddle_sound = pygame.mixer.Sound("sounds/paddle.wav")
bounce_wall_sound = pygame.mixer.Sound("sounds/wall.wav")

# paddle setup / controls
paddle_width = 56.25
paddle_height = 10
paddle_speed = 15
paddle = pygame.Rect(width // 2 - paddle_width // 2,
                     height - paddle_height - 20, paddle_width, paddle_height)


def move_paddle():
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    if key[pygame.K_RIGHT] and paddle.right < width:
        paddle.right += paddle_speed


# ball setup
ball_radius = 5
ball_speed = 5
ball_max_speed = 15
ball_hits = 0
ball_rect = int(ball_radius * 2)
ball = pygame.Rect(random.randrange(ball_rect, width - ball_rect),
                   height // 2, ball_rect, ball_rect)
dx, dy = 1, -1

# blocks setup
block_list = []
for i in range(14):
    for j in range(8):
        block = pygame.Rect(5 + 42.5 * i, 150 + 15 * j, 37.5, 10)
        block_list.append(block)

color_list = []
for i in range(14):
    for j in range(8):
        if j == 0 or j == 1:
            color = RED
        elif j == 2 or j == 3:
            color = ORANGE
        elif j == 4 or j == 5:
            color = GREEN
        else:
            color = YELLOW
        color_list.append(color)


# collision detection between ball and block
def detect_collision(x, y, ball_object, rect):
    if x > 0:
        delta_x = ball_object.right - rect.left
    else:
        delta_x = rect.right - ball_object.left
    if y > 0:
        delta_y = ball_object.bottom - rect.top
    else:
        delta_y = rect.bottom - ball_object.top

    if abs(delta_x - delta_y) < 5:
        x, y = -x, -y
    elif delta_x > delta_y:
        y = -y
    elif delta_x < delta_y:
        x = -x
    return x, y


# game loop
game_loop = True
while game_loop:

    # game update
    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.quit:
            game_loop = False

    # draw objects
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [0, 0], [width, 0], 1)
    pygame.draw.line(screen, WHITE, [0, 0], [0, height], 1)
    pygame.draw.line(screen, WHITE, [600, 0], [600, height], 1)
    pygame.draw.rect(screen, WHITE, ball)
    pygame.draw.rect(screen, BLUE, paddle)

    for color, block in enumerate(block_list):
        pygame.draw.rect(screen, color_list[color], block)

    # draw hud
    font = pygame.font.Font("font/AGENCY.TTF", 70)
    text = font.render(str(score), True, WHITE)
    screen.blit(text, (50, 30))
    text = font.render(str(lives), True, WHITE)
    screen.blit(text, (450, 30))

    # ball movement / speed
    ball.x += ball_speed * dx
    ball.y += ball_speed * dy

    if ball_hits >= 4:
        ball_hits = 0
        ball_speed += 0.25

    if ball_speed >= ball_max_speed:
        ball_speed = 15

    # collision with left and right wall
    if ball.centerx < ball_radius or ball.centerx > width - ball_radius:
        dx = -dx
        ball_hits += 1
        bounce_wall_sound.play()

    # collision with top wall
    if ball.centery < ball_radius:
        dy = -dy
        ball_hits += 1
        bounce_wall_sound.play()

    # collision with paddle
    if ball.colliderect(paddle) and dy > 0:
        angle = -90 + 120 * ((ball.centerx - paddle.centerx) / paddle.width)
        dy = math.sin(angle*(math.pi/180))
        ball_hits += 1
        bounce_paddle_sound.play()

    # collision with blocks
    hit_index = ball.collidelist(block_list)
    if hit_index != -1:
        hit_rect = block_list.pop(hit_index)
        hit_color = color_list.pop(hit_index)
        dx, dy = detect_collision(dx, dy, ball, hit_rect)

        if hit_color == YELLOW:
            score += 1
            ball_hits += 1
        elif hit_color == GREEN:
            score += 3
            ball_hits += 1
        elif hit_color == ORANGE:
            score += 5
            ball_hits += 1
            ball_speed += 0.25
        elif hit_color == RED:
            score += 7
            ball_hits += 1
            ball_speed += 0.25

        bounce_block_sound.play()

    # victory / game over
    if ball.bottom > height:
        ball_speed = 5
        if lives > 0:
            lives -= 1
            ball = pygame.Rect(random.randrange(ball_rect, width - ball_rect),
                               height//2, ball_rect, ball_rect)
        else:
            text = font.render("GAME OVER!", True, WHITE)
            screen.blit(text, (width//2 - 140, height//2))
            pygame.display.update()
            pygame.time.wait(2500)
            game_loop = False

    elif not len(block_list):
        block_list = []
        for i in range(14):
            for j in range(8):
                block = pygame.Rect(5 + 42.5 * i, 45 + 20 * j, 37.5, 15)
                block_list.append(block)

        color_list = []
        for i in range(14):
            for j in range(8):
                if j < 2:
                    color = RED
                elif 2 <= j < 4:
                    color = ORANGE
                elif 4 <= j < 6:
                    color = GREEN
                else:
                    color = YELLOW
                color_list.append(color)
        for color, block in enumerate(block_list):
            pygame.draw.rect(screen, color_list[color], block)
        ball = pygame.Rect(random.randrange(ball_rect, width - ball_rect),
                           height//2, ball_rect, ball_rect)

    move_paddle()

# quit on end
pygame.quit()
