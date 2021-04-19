import pygame

FPS = 60

clock = pygame.time.Clock()

BLUE = (0, 0, 255)
Yellow = (255, 255, 0)

pygame.init()
screen = pygame.display.set_mode((640, 480))
screen.fill(BLUE)

pygame.draw.rect(screen, Yellow, pygame.Rect((220, 150, 210, 180)))
pygame.display.flip()

while True:
    clock.tick(FPS)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
