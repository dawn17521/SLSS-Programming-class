import pygame as pg,random

# --CONSTANTS--
# COLOURS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH = 1280  # Pixels
HEIGHT = 720
screen_size = (WIDTH, HEIGHT)

class Snowflake(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.Surface((10, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH)
        self.rect.y = random.randrange(-10, -5)
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            self.rect.y = random.randrange(-10, -5)
            self.rect.x = random.randrange(WIDTH)

def start():


    pg.init()

    screen = pg.display.set_mode(screen_size)
    done = False
    clock = pg.time.Clock()
    all_sprites = pg.sprite.Group()
    pg.display.set_caption("<SnowFlake>")
    for _ in range(50):
        snowflake = Snowflake()
        all_sprites.add(snowflake)

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
        all_sprites.update()
        screen.fill(BLACK)
        all_sprites.draw(screen)
        pg.display.flip()
        clock.tick(60) 


def main():
    start()


if __name__ == "__main__":
    main()