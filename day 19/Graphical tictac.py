import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 10
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LINE_COLOR = (50, 50, 50)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
screen.fill(WHITE)

# Board representation
board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
current_player = "X"

# Draw the grid lines
def draw_lines():
    for row in range(1, BOARD_ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (row * SQUARE_SIZE, 0), (row * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Draw X
def draw_x(row, col):
    start_pos = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE)
    end_pos = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
    pygame.draw.line(screen, BLACK, start_pos, end_pos, CROSS_WIDTH)
    start_pos = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE)
    end_pos = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
    pygame.draw.line(screen, BLACK, start_pos, end_pos, CROSS_WIDTH)

# Draw O
def draw_o(row, col):
    center = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
    pygame.draw.circle(screen, BLACK, center, CIRCLE_RADIUS, CIRCLE_WIDTH)

# Mark the board
def mark_square(row, col, player):
    board[row][col] = player
    if player == "X":
        draw_x(row, col)
    elif player == "O":
        draw_o(row, col)

# Check if a player has won
def check_winner(player):
    # Check rows and columns
    for i in range(BOARD_ROWS):
        if all(board[i][j] == player for j in range(BOARD_COLS)) or all(board[j][i] == player for j in range(BOARD_ROWS)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(BOARD_ROWS)) or all(board[i][BOARD_ROWS - i - 1] == player for i in range(BOARD_ROWS)):
        return True
    return False

# Check if the board is full (draw)
def is_draw():
    return all(board[row][col] is not None for row in range(BOARD_ROWS) for col in range(BOARD_COLS))

# Restart the game
def restart_game():
    global board, current_player
    board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    current_player = "X"
    screen.fill(WHITE)
    draw_lines()

# Main game loop
draw_lines()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            clicked_row = mouseY // SQUARE_SIZE
            clicked_col = mouseX // SQUARE_SIZE

            if board[clicked_row][clicked_col] is None:  # Check if square is empty
                mark_square(clicked_row, clicked_col, current_player)
                if check_winner(current_player):
                    pygame.display.set_caption(f"Player {current_player} Wins!")
                    pygame.time.wait(2000)
                    restart_game()
                elif is_draw():
                    pygame.display.set_caption("It's a Draw!")
                    pygame.time.wait(2000)
                    restart_game()
                else:
                    current_player = "O" if current_player == "X" else "X"
                    pygame.display.set_caption(f"Player {current_player}'s Turn")

# Quit pygame
pygame.quit()
sys.exit()
