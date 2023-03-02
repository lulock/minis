"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (255,105,180)
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
ROWS = 50
COLS = 50
MARGIN = 2
CELL_WIDTH = (WINDOW_WIDTH/ROWS) - MARGIN
CELL_HEIGHT = (WINDOW_HEIGHT/COLS) - MARGIN

GRID = []

for i in range(ROWS):
    GRID.append([])
    for j in range(COLS):
        GRID[i].append(0)

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (WINDOW_WIDTH, WINDOW_HEIGHT)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("This is Life.")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_pos, y_pos = pygame.mouse.get_pos()
            col = x_pos // (CELL_WIDTH+MARGIN)
            row = y_pos // (CELL_HEIGHT+MARGIN)
            GRID[int(row)][int(col)] = 1
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    for i in range(ROWS):
        for j in range(COLS):
            if GRID[i][j] == 1:
                colour = PINK
            else: 
                colour = WHITE
            pygame.draw.rect(screen, colour, pygame.Rect((CELL_WIDTH + MARGIN)*j + MARGIN/2,(CELL_HEIGHT + MARGIN)*i + MARGIN/2,CELL_WIDTH, CELL_HEIGHT))

 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)

 
# Close the window and quit.
pygame.quit()