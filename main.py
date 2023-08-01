import pygame

pygame.init()
#размеры экрана

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("pygame valeron game")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

##screen.fill((50, 168, 82))
square = pygame.Surface((50,170))
square.fill('Blue')

myfont = pygame.font.Font('fonts/Handjet-Black.ttf',40)
text_surface = myfont.render('Valeron', False, 'Green')

player = pygame.image.load('images/icon.png')

running = True

while running:
    screen.blit(square, (10,0))

    pygame.draw.circle(square, 'Red', (20,7), 4)

    screen.blit(text_surface, (500, 200))

    screen.blit(player, (200, 100))
    pygame.display.update()

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            running=False
            pygame.quit()




