import pygame

# Create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650

# Game Caption
GAME_CAPTION = "Street Fight Pygame"

# Frame Rate
clock = pygame.time.Clock()
FPS = 60

# Define colours
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define Fighter 1 variables
WARRIOR_SIZE = 162
WARRIOR_SCALE = 4
WARRIOR_OFFSET = [72, 56]
WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
CONTROL_1 = {'Forward': pygame.K_a, 'Back': pygame.K_d,
             'Jump': pygame.K_w, 'Attack1': pygame.K_f, 'Attack2': pygame.K_e}
# Define Fighter 2 variables
WIZARD_SIZE = 250
WIZARD_SCALE = 3
WIZARD_OFFSET = [112, 107]
WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]
CONTROL_2 = {'Forward': pygame.K_LEFT, 'Back': pygame.K_RIGHT,
             'Jump': pygame.K_UP, 'Attack1': pygame.K_n, 'Attack2': pygame.K_m}

# Define number of steps in each animation
WARRIOR_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7]
WIZARD_ANIMATION_STEPS = [8, 8, 1, 8, 8, 3, 7]
