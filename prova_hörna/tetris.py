import pygame
import random

pygame.init()

# Set up the game window
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tetris")

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Set up the fonts
FONT = pygame.font.SysFont(None, 30)

# Set up the clock
clock = pygame.time.Clock()

# Define the Tetris blocks
block_shapes = [
    [(1, 1, 1),
     (0, 1, 0)],

    [(0, 2, 2),
     (2, 2, 0)],

    [(3, 3, 0),
     (0, 3, 3)],

    [(4, 0, 0),
     (4, 4, 4)],

    [(0, 0, 5),
     (5, 5, 5)],

    [(6, 6),
     (6, 6)],

    [(7, 7, 7, 7)],
]

block_colors = [
    BLUE,
    GREEN,
    RED,
    YELLOW,
    WHITE,
    BLACK,
    BLUE
]

# Define the Tetris board
board_width = 10
board_height = 20

board = [[0 for _ in range(board_width)] for _ in range(board_height)]


# Define the block class
class Block:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.x = int(board_width / 2 - len(shape[0]) / 2)
        self.y = 0

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def rotate(self):
        self.shape = list(zip(*self.shape[::-1]))

    def draw(self):
        for i, row in enumerate(self.shape):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(game_window, self.color, (self.x + j, self.y + i, 1, 1))


# Define the game loop
def game_loop():
    score = 0

    block = Block(random.choice(block_shapes), random.choice(block_colors))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    block.move(-1, 0)

                elif event.key == pygame.K_RIGHT:
                    block.move(1, 0)

                elif event.key == pygame.K_DOWN:
                    block.move(0, 1)

                elif event.key == pygame.K_UP:
                    block.rotate()

        game_window.fill(BLACK)

        # Draw the board
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(game_window, block_colors[cell - 1], (j, i, 1, 1))

        # Draw the block
        block.draw()

        # Check if the block has collided with the bottom or another block
        if any(board[block.y + i][block.x + j] for i, row in enumerate(block.shape) for j, cell in enumerate(row)):
            for i, row in enumerate(block.shape):
                for j, cell in enumerate(row):
                    if cell:
                        board[block.y + i][block.x + j] = cell

            block = Block(random.choice(block_shapes), random.choice(block_colors))

        # Check if a row is full and needs to be cleared
        for i, row in enumerate(board):
            if all(row):
                del board[i]
                board.insert(0, [0 for _ in range(board_width)])
                score += 10

        # Draw the score
        score_text = FONT.render(f"Score: {score}", True, WHITE)
        game_window.blit(score_text, (10, 10))

        # Update the screen
        pygame.display.update()

        # Set the game speed
        clock.tick(10)

if __name__ == '__main__':
    game_loop()
