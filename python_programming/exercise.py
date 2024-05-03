import sys, pygame, time


pygame.init()

bg_color1 = (0,128,128)
bg_color2 = (60,60,60)
bg_color3 = (255,0,0)

screen_im = pygame.display.set_mode((1900,1500))
screen_rectangle =  screen_im.get_rect()

pygame.display.set_caption('Evil Alien')

screen_im.fill(bg_color1)
ship__image = pygame.image.load('Images/rocket-306209_1280.png')

ship_rect = ship__image.get_rect()
ship_rect.center = screen_rectangle.center


tx_font = pygame.font.SysFont(None,50)
tx_image = tx_font.render('attack alien', True, bg_color2, bg_color3)

bullet_rect = pygame.Rect(0,0,3,15)
pygame.draw.rect(screen_im, bg_color2, ship_rect)
tx_rect = tx_image.get_rect()

screen_im.blit(ship__image,ship_rect)
bullet_rect.midbottom = ship_rect.midtop
screen_im.blit(tx_image, tx_rect)
pygame.display.flip()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()