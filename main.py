from pygame import *
FPS = 60
window = display.set_mode((700, 500))
display.set_caption('ПИНГ ПОНГ')
window.fill((255, 255, 255))
clock = time.Clock()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed,):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def updateL(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 700:
            self.rect.y += self.speed
    def updateR(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 700:
            self.rect.y += self.speed
 
lost = 0
font.init()
font1 = font.SysFont('Arial', 36)
font2 = font.SysFont('Arial', 36)




RACKET = Player('OIP.jpg', 30, 200,100,80, 7)
RACKET567 = Player('Cornilleau-Sport-Raquette-de-tennis-de-table-ping-pong-Mixte-829x1024.jpg', 570, 200,100,80, 7)
ball = GameSprite('ppp.jpg', 260, 200, 60, 60, 7)
speed_x = 3 
speed_y = 3

finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        text_lose = font1.render('HA HA HA, YOU LOSE:' , True, (20,155,40))
        text_lose1 = font2.render('HA HA HA YOU LOSE:', True, (20,155,40))

        window.blit(text_lose1,(20,50))
        window.fill((255, 255, 255))
        RACKET.updateL()
        RACKET567.updateR()
        RACKET.reset()
        RACKET567.reset()
        ball.rect.y += speed_y
        ball.rect.x += speed_x
        if ball.rect.y <= 0 or ball.rect.y >= 450:
            speed_y *= -1
        if sprite.collide_rect(RACKET, ball) or sprite.collide_rect(RACKET567, ball):
            speed_x *= -1
        if ball.rect.x < 0:
            window.blit(text_lose,(20,20))
            finish = True
        if ball.rect.x > 700:
            window.blit(text_lose1,(20,20))
            finish = True
        ball.reset()
    display.update()
    clock.tick(FPS)






























































