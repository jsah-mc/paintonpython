import pygame
pygame.init()

# FPS setting
fps = 60
timer = pygame.time.Clock()
WIDTH = 1280
HEIGHT = 720

# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("I used github copilot to help me and a video tutorial")


#  Define the Menu
def draw_menu():
  pygame.draw.rect(screen, 'gray', [0, 0 , WIDTH, 100])
  pygame.draw.line(screen, 'black', (0, 100), (WIDTH, 100), 3)
  xl_brush = pygame.draw.rect(screen, 'black', [10, 10, 80, 80])
  pygame.draw.circle(screen, 'white', (50, 50), 25)
  l_brush = pygame.draw.rect(screen, 'black', [100, 10, 80, 80])
  pygame.draw.circle(screen, 'white', (140, 50), 20)
  m_brush = pygame.draw.rect(screen, 'black', [190, 10, 80, 80])
  pygame.draw.circle(screen, 'white', (230, 50), 15)
  s_brush = pygame.draw.rect(screen, 'black', [280, 10, 80, 80])
  pygame.draw.circle(screen, 'white', (320, 50), 5)
  brush_list = [xl_brush, l_brush, m_brush, s_brush]

# Colors
  blue = pygame.draw.rect(screen, (0, 0, 255), [WIDTH - 50, 10, 25, 25])
  red = pygame.draw.rect(screen, (255, 0, 0), [WIDTH - 80, 10, 25, 25])
  green = pygame.draw.rect(screen, (0, 255, 0), [WIDTH - 50, 40, 25, 25])
  yellow = pygame.draw.rect(screen, (255, 255, 0), [WIDTH - 80, 40, 25, 25])
  orange = pygame.draw.rect(screen, (255, 165, 0), [WIDTH - 110, 10, 25, 25])
  purple = pygame.draw.rect(screen, (128, 0, 128), [WIDTH - 110, 40, 25, 25])
  black = pygame.draw.rect(screen, (0, 0, 0), [WIDTH - 140, 10, 25, 25])
  white = pygame.draw.rect(screen, (255, 255, 255), [WIDTH - 140, 40, 25, 25])
  pink = pygame.draw.rect(screen, (255, 192, 203), [WIDTH - 170, 10, 25, 25])
  brown = pygame.draw.rect(screen, (165, 42, 42), [WIDTH - 170, 40, 25, 25])
  color_rect = [blue, red, green, yellow, orange, purple, black, white, pink, brown]

  return brush_list, color_rect


# Main loop
run = True
while run:
  timer.tick(fps)
  screen.fill('white')

  brushes, colors = draw_menu()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

    if event.type == pygame.MOUSEBUTTONDOWN:
      for i in range(len(brushes)):
        if brushes[i].collidepoint(event.pos):
          print('Brush', i)
  pygame.display.flip()
pygame.quit()      