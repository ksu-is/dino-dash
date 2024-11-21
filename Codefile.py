import pygame
import random

# start Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dino Run")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Clock and FPS
clock = pygame.time.Clock()
FPS = 60

# Dino settings
DINO_WIDTH = 50
DINO_HEIGHT = 50
GRAVITY = 1

# Load assets 
dino_img = pygame.Surface((DINO_WIDTH, DINO_HEIGHT))
dino_img.fill((0, 255, 0))  # Green placeholder
obstacle_img = pygame.Surface((30, 30))
obstacle_img.fill((255, 0, 0))  # Red placeholder
ground_img = pygame.Surface((SCREEN_WIDTH, 10))
ground_img.fill((100, 100, 100))  # Gray ground

# Dino
class Dino:
    def __init__(self):
        self.x = 50
        self.y = SCREEN_HEIGHT - DINO_HEIGHT - 10
        self.width = DINO_WIDTH
        self.height = DINO_HEIGHT
        self.jump_velocity = -15
        self.velocity = 0
        self.is_jumping = False

    def draw(self):
        screen.blit(dino_img, (self.x, self.y))

    def update(self):
        if self.is_jumping:
            self.velocity += GRAVITY
            self.y += self.velocity
            if self.y >= SCREEN_HEIGHT - self.height - 10:
                self.y = SCREEN_HEIGHT - self.height - 10
                self.is_jumping = False

# Obstacle 
class Obstacle:
    def __init__(self, x):
        self.x = x
        self.y = SCREEN_HEIGHT - 40
        self.width = 30
        self.height = 30

    def draw(self):
        screen.blit(obstacle_img, (self.x, self.y))

    def update(self):
        self.x -= 5
        if self.x + self.width < 0:
            self.x = SCREEN_WIDTH + random.randint(200, 500)

# Initialize game objects
dino = Dino()
obstacles = [Obstacle(SCREEN_WIDTH + i * 300) for i in range(3)]
score = 0

# Main game loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not dino.is_jumping:
                dino.is_jumping = True
                dino.velocity = dino.jump_velocity

    # Update game objects
    dino.update()
    for obstacle in obstacles:
        obstacle.update()

    # Collision detection
    for obstacle in obstacles:
        if (
            dino.x < obstacle.x + obstacle.width
            and dino.x + dino.width > obstacle.x
            and dino.y < obstacle.y + obstacle.height
            and dino.y + dino.height > obstacle.y
        ):
            print("Game Over!")
            running = False

    # Draw game objects
    dino.draw()
    for obstacle in obstacles:
        obstacle.draw()
    screen.blit(ground_img, (0, SCREEN_HEIGHT - 10))

    # Score
    score += 1
    font = pygame.font.SysFont("Arial", 20)
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()

pygame.quit()
