import pygame

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
fps = 60
BACKGROUND_COLOR = 'white'

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")
timer = pygame.time.Clock()

# Variables
active_color = (0, 0, 0)
active_size = 10
painting = []

def draw_menu():
    blue = pygame.draw.rect(screen, (0, 0, 255), [WIDTH - 50, 10, 25, 25])
    red = pygame.draw.rect(screen, (255, 0, 0), [WIDTH - 50, 40, 25, 25])
    green = pygame.draw.rect(screen, (0, 255, 0), [WIDTH - 80, 10, 25, 25])
    yellow = pygame.draw.rect(screen, (255, 255, 0), [WIDTH - 80, 40, 25, 25])
    orange = pygame.draw.rect(screen, (255, 165, 0), [WIDTH - 110, 10, 25, 25])
    purple = pygame.draw.rect(screen, (128, 0, 128), [WIDTH - 110, 40, 25, 25])
    black = pygame.draw.rect(screen, (0, 0, 0), [WIDTH - 140, 10, 25, 25])
    white = pygame.draw.rect(screen, (255, 255, 255), [WIDTH - 140, 40, 25, 25])
    pink = pygame.draw.rect(screen, (255, 192, 203), [WIDTH - 170, 10, 25, 25])
    brown = pygame.draw.rect(screen, (165, 42, 42), [WIDTH - 170, 40, 25, 25])
    small = pygame.draw.rect(screen, (200, 200, 200), [WIDTH - 200, 10, 25, 25])
    medium = pygame.draw.rect(screen, (150, 150, 150), [WIDTH - 200, 40, 25, 25])
    large = pygame.draw.rect(screen, (100, 100, 100), [WIDTH - 200, 70, 25, 25])
    eraser = pygame.draw.rect(screen, (255, 255, 255), [WIDTH - 230, 10, 25, 55], 2)  # Eraser button
    color_rect = [blue, red, green, yellow, orange, purple, black, white, pink, brown]
    size_rect = [small, medium, large]
    rgb_list = [(0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 255, 0), (255, 165, 0), (128, 0, 128), (0, 0, 0), (255, 255, 255), (255, 192, 203), (165, 42, 42)]
    size_list = [5, 10, 20]
    return color_rect, size_rect, rgb_list, size_list, eraser

def draw_painting(painting):
    for item in painting:
        pygame.draw.circle(screen, item[2], item[0], item[1])

# Main loop
run = True
while run:
    timer.tick(fps)
    screen.fill(BACKGROUND_COLOR)
    colors, sizes, rgb_list, size_list, eraser = draw_menu()
    mouse = pygame.mouse.get_pos()
    left_click = pygame.mouse.get_pressed()[0]
    if mouse[1] > 100:
        pygame.draw.circle(screen, active_color, mouse, active_size)
    if left_click and mouse[1] > 100:
        painting.append((mouse, active_size, active_color))
    draw_painting(painting)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgb_list[i]
            for i in range(len(sizes)):
                if sizes[i].collidepoint(event.pos):
                    active_size = size_list[i]
            if eraser.collidepoint(event.pos):
                active_color = BACKGROUND_COLOR  # Set active color to background color for erasing

    pygame.display.flip()

pygame.quit()