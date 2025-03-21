import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stone Paper Scissor")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACKGROUND_COLOR = (173, 216, 230)  # Light blue background
YELLOW = (255, 255, 0)  # Yellow

# Load pixel art images
stone_img = pygame.image.load('stone.png').convert_alpha()
paper_img = pygame.image.load('paper.png').convert_alpha()
scissor_img = pygame.image.load('scissor.png').convert_alpha()

# Resize images if necessary
stone_img = pygame.transform.scale(stone_img, (100, 100))
paper_img = pygame.transform.scale(paper_img, (100, 100))
scissor_img = pygame.transform.scale(scissor_img, (100, 100))

# Fonts
font = pygame.font.Font(None, 36)

# Sprinkle particles
class Sprinkle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random.randint(2, 5)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.speed_x = random.uniform(-1, 1)
        self.speed_y = random.uniform(-1, 1)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

def display_message(message, y_offset=0, color=BLACK):
    text = font.render(message, True, color)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2 + y_offset))

def game_loop():
    running = True
    player_choice = None
    computer_choice = None
    result = None
    sprinkles = []

    while running:
        # Set background color based on the result
        if result == "You win!":
            screen.fill(YELLOW)  # Yellow background for victory
        else:
            screen.fill(BACKGROUND_COLOR)  # Default background color

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 100 < x < 200 and 400 < y < 500:
                    player_choice = 'stone'
                elif 300 < x < 400 and 400 < y < 500:
                    player_choice = 'paper'
                elif 500 < x < 600 and 400 < y < 500:
                    player_choice = 'scissor'

                if player_choice:
                    computer_choice = random.choice(['stone', 'paper', 'scissor'])
                    if player_choice == computer_choice:
                        result = "It's a tie!"
                    elif (player_choice == 'stone' and computer_choice == 'scissor') or \
                         (player_choice == 'paper' and computer_choice == 'stone') or \
                         (player_choice == 'scissor' and computer_choice == 'paper'):
                        result = "You win!"
                        # Create sprinkles when the player wins
                        sprinkles = [Sprinkle(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(100)]
                    else:
                        result = "You lose!"

        # Draw buttons
        screen.blit(stone_img, (100, 400))
        screen.blit(paper_img, (300, 400))
        screen.blit(scissor_img, (500, 400))

        if result:
            display_message(result, y_offset=-50)
            # Display computer's choice
            computer_message = f"Computer: {computer_choice}"
            display_message(computer_message, y_offset=50)
            player_message = f"Player: {player_choice}"
            display_message(player_message, y_offset=20)

            # Draw sprinkles if the player wins
            if result == "You win!":
                for sprinkle in sprinkles:
                    sprinkle.move()
                    sprinkle.draw()

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    game_loop()