import pygame

pygame.init()

oyna = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Pygame 2 - Keyword')

x = 50
y = 445
width = 50
height = 50
vel = 5

isJump = False
jumpCount = 10

run = True
while run:

    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel

    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel

    if not (isJump):

        if keys[pygame.K_UP] and y > vel:
            y -= vel

        if keys[pygame.K_DOWN] and y < 500 - height - vel:
            y += vel

        if keys[pygame.K_SPACE]:
            isJump = True

    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg

            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    # Agar shu bo`lmasa, rang cho`zilip yurivaradi
    oyna.fill((0, 0, 50))

    pygame.draw.rect(oyna, (0, 0, 255), (x, y, width, height))

    pygame.draw.ellipse(oyna, (0, 255, 0), (x, y, width, height))
    pygame.display.update()
pygame.quit()




