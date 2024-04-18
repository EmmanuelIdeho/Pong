import pygame as pg

#colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)

#screen size
WIDTH = 800
HEIGHT = 600

#A function to draw any text you want on the screen
def draw_text(surf, text, size, x, y, color):
    font_name = pg.font.match_font('arial')
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

#blueprint for the player
class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([20, 200])
        self.image.fill("green")
        self.rect = self.image.get_rect()
        self.rect.x = 30
        self.rect.y = 200
        self.speed = 5
        self.score = 0
    def update(self):
        if self.rect.top <= 0:
            self.rect.y += self.speed
        if self.rect.bottom >= HEIGHT:
            self.rect.y -= self.speed
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.rect.y -= self.speed
        if keys[pg.K_s]:
            self.rect.y += self.speed

#blueprint of the opponent
class Opponent(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface([20, 200])
        self.image.fill("purple")
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH - 60
        self.rect.y = 200
        self.speed = 5
        self.score = 0
        #self.pos = pg.Vector2(HEIGHT/2, 30)
    def update(self):
        if self.rect.top <= 0:
            self.rect.y += self.speed
        if self.rect.bottom >= HEIGHT:
            self.rect.y -= self.speed
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.rect.y -= self.speed
        if keys[pg.K_DOWN]:
            self.rect.y += self.speed

#blueprint of the ball
class Ball(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.radius = 15
        self.image = pg.Surface((self.radius*2-1, self.radius*2-1))
        pg.draw.circle(self.image, "red", (self.radius, self.radius), self.radius)
        self.speedx = 5
        self.speedy = 5
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH / 2
        self.rect.y = HEIGHT / 2
        #self.pos = pg.Vector2(HEIGHT/2, 30)
    def update(self):
        self.rect.x += self.speedx
        self.rect.y -= self.speedy


        if self.rect.y-self.radius < BOUNDS.top or self.rect.y+self.radius > BOUNDS.bottom:
            self.speedy *= -1
        if self.rect.x < BOUNDS.left:
            opponent.score += 1
            self.rect.x = WIDTH / 2
            self.rect.y = HEIGHT / 2
            self.speedx *= -1
        if self.rect.x+self.radius > BOUNDS.right:
            player.score += 1
            self.rect.x = WIDTH / 2
            self.rect.y = HEIGHT / 2
            self.speedx *= -1


#pygame setup
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Pong")
clock = pg.time.Clock()
FPS = 60
BOUNDS = screen.get_rect()

#setting up sprites in the game
players = pg.sprite.Group()
player = Player()
players.add(player)

opps = pg.sprite.Group()
opponent = Opponent()
opps.add(opponent)

ball = Ball()
all_sprites = pg.sprite.Group()
all_sprites.add(player)
all_sprites.add(opponent)
all_sprites.add(ball)

#main game loop
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    #logic of sprite interactions
    if pg.sprite.spritecollide(ball, opps, False) or pg.sprite.spritecollide(ball, players, False):
        ball.speedx *= -1


    screen.fill("blue")
    #code to render the game
    all_sprites.draw(screen)
    all_sprites.update()
    draw_text(screen, "Player:"+str(player.score), 30, WIDTH/2 - 100, 50, "black")
    draw_text(screen, "Opponent:"+str(opponent.score), 30, WIDTH/2 + 100, 50, "black")
    pg.display.flip()
    clock.tick(FPS) #limits FPS(frames per second) to 60

pg.quit()
