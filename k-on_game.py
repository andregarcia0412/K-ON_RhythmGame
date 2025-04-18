import pygame

pygame.init()
screen = pygame.display.set_mode((800, 1024))
clock = pygame.time.Clock()
pygame.display.set_caption("K-ON the game")
game_active = True
running = True
font = pygame.font.Font("jogo pygame/font/Pixeltype.ttf",50)

leftArrow_surface = pygame.image.load("jogo pygame/images/left-arrow.png").convert_alpha()
leftArrow_rectangle = leftArrow_surface.get_rect(center = (250,950))

downArrow_surface = pygame.image.load("jogo pygame/images/down arrow.png").convert_alpha()
downArrow_rectangle = downArrow_surface.get_rect(center = (350,950))

upArrow_surface = pygame.image.load("jogo pygame/images/up arrow.png").convert_alpha()
upArrow_rectangle = upArrow_surface.get_rect(center = (450,950))

rightArrow_surface = pygame.image.load("jogo pygame/images/right arrow.png").convert_alpha()
rightArrow_rectangle = rightArrow_surface.get_rect(center = (550,950))

coloredLeftArrow_surface = pygame.image.load("jogo pygame/images/colored-left-arrow.png").convert_alpha()
coloredLeftArrow_rectangle = coloredLeftArrow_surface.get_rect(center = (250,0))

coloredDownArrow_surface = pygame.image.load("jogo pygame/images/colored-down-arrow.png").convert_alpha()
coloredDownArrow_rectangle = coloredDownArrow_surface.get_rect(center = (350,0))

coloredUpArrow_surface = pygame.image.load("jogo pygame/images/colored-up-arrow.png").convert_alpha()
coloredUpArrow_rectangle = coloredUpArrow_surface.get_rect(center = (450, 0))

coloredRightArrow_surface = pygame.image.load("jogo pygame/images/colored-right-arrow.png").convert_alpha()
coloredRightArrow_rectangle = coloredRightArrow_surface.get_rect(center = (550,0))

#points:
points_value = 0
combo = 0
multiplier = 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if game_active:
        points_text = "Points: " + str(points_value) 
        text_surface = font.render(points_text, False, "white")

        combo_text = "Combo: " + str(combo)
        combo_surface = font.render(combo_text, False, "white")

        screen.fill("purple")

        #player arrows & text
        screen.blit(leftArrow_surface, (leftArrow_rectangle))
        screen.blit(downArrow_surface, (downArrow_rectangle))
        screen.blit(upArrow_surface, (upArrow_rectangle))
        screen.blit(rightArrow_surface, (rightArrow_rectangle))
        screen.blit(text_surface , (0,0))
        screen.blit(combo_surface, (600, 0))

        #falling arrows
        screen.blit(coloredLeftArrow_surface , (coloredLeftArrow_rectangle))
        screen.blit(coloredDownArrow_surface , (coloredDownArrow_rectangle))
        screen.blit(coloredUpArrow_surface , (coloredUpArrow_rectangle))
        screen.blit(coloredRightArrow_surface , (coloredRightArrow_rectangle))

        #arrows movement:
        coloredLeftArrow_rectangle.y += 20
        coloredDownArrow_rectangle.y += 20
        coloredUpArrow_rectangle.y += 20
        coloredRightArrow_rectangle.y += 20
        
        if coloredLeftArrow_rectangle.y > 1024:
            coloredLeftArrow_rectangle.y = -150
            points_value -= 1
            combo = 0

        if coloredDownArrow_rectangle.y > 1024:
            coloredDownArrow_rectangle.y = -150
            points_value -= 1
            combo = 0

        if  coloredUpArrow_rectangle.y > 1024:
            coloredUpArrow_rectangle.y = -150
            points_value -= 1
            combo = 0

        if coloredRightArrow_rectangle.y > 1024:
            coloredRightArrow_rectangle.y = -150
            points_value -= 1
            combo = 0

        # inputs:
        keys = pygame.key.get_pressed()
        button_d = keys[pygame.K_d]
        button_f = keys[pygame.K_f]
        button_j = keys[pygame.K_j]
        button_k = keys[pygame.K_k]

        # collisions and points:
        if leftArrow_rectangle.colliderect(coloredLeftArrow_rectangle) and button_d:
            coloredLeftArrow_rectangle.y = -150
            combo += 1
            points_value += 1 * multiplier

        if downArrow_rectangle.colliderect(coloredDownArrow_rectangle) and button_f:
            coloredDownArrow_rectangle.y = -150
            combo += 1
            points_value += 1 * multiplier

        if upArrow_rectangle.colliderect(coloredUpArrow_rectangle) and button_j:
            coloredUpArrow_rectangle.y = -150
            combo += 1
            points_value += 1 * multiplier

        if rightArrow_rectangle.colliderect(coloredRightArrow_rectangle) and button_k:
            coloredRightArrow_rectangle.y = -150
            combo += 1
            points_value += 1 * multiplier

        if combo >= 20:
            multiplier = 2
        elif combo >= 50:
            multiplier = 3
        elif combo >= 100:
            multiplier = 4
        else:
            multiplier = 1
    #game display:
    pygame.display.update()
    clock.tick(60)

pygame.quit()