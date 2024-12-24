# Importing and initializing pygame
import pygame
pygame.init()

# Setting up the screen
fps = 60
width, height = 1280, 720

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Paint Program")

def draw_menu():
  pygame.draw.rect(screen, 'gray', (0, 0, width, 70))
  pygame.draw.line(screen, 'black', (0, 70), (width, 70), 3)
  xl_brush = pygame.draw.rect(screen, 'black', (10, 10, 60, 60))
  pygame.draw.circle(screen, 'white',(40, 40), 20)
  l_brush = pygame.draw.rect(screen, 'black', (80, 10, 60, 60))
  pygame.draw.circle(screen, 'white',(110, 40), 15)
  m_brush = pygame.draw.rect(screen, 'black', (150, 10, 60, 60))
  pygame.draw.circle(screen, 'white',(180, 40), 10)
  s_brush = pygame.draw.rect(screen, 'black', (220, 10, 60, 60))
  pygame.draw.circle(screen, 'white',(250, 40), 5)



# Main loop
run = True
while run :
    screen.fill((255, 255, 255))

    draw_menu()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
    # Updating the display
    pygame.display.update()