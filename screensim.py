# Example file showing a basic pygame "game loop"
import pygame
import random
# pygame setup
pygame.init()
dW = 500
dH = 500
screen = pygame.display.set_mode((dW, dH))
clock = pygame.time.Clock()
def render(w, h, ccx, ccy):
    for y in range(ccy):
        for x in range(ccx):
            b = pygame.Rect(x,y,w,h)
            pygame.draw.rect(screen, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), b)
            b.x += x
        b.y += y
        x = 0



running = True
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    # RENDER YOUR GAME HERE
    render(dW//100, dH//100, 2, 2)
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()