# Create your game in this file!
from pygame import *
window_width = 700
window_height = 500
window = display.set_mode((window_width, window_height))
display.set_caption("Maze")
back = (119, 210, 223)
window.fill(back)
clock = time.Clock()
run = True
finish = False

class GameSprite(sprite. Sprite):
    def __init__(self, player_image, x, y, w, h):
        super(). __init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def __init__(self, player_image, x, y, w, h, x_speed, y_speed):
        super(). __init__(player_image, x, y, w, h)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self .x_speed > 0:
                for p in platforms_touched:
                    self.x_speed = 0
        elif self. x_speed < 0:
                    for p in platforms_touched:
                        self.x_speed = 0
        if self. y_speed > 0:
            for p in platforms_touched:
                self.y_speed = 0
        elif self. y_speed < 0:
            for o in platforms_touched:
                self.y_speed = 0
    def fire(self):
        bullet = Bullet("bullet.png", self.rect.right, self.rect.centery, 15, 20, 15)
        bullets.add(bullet)


            
class Enemy(GameSprite):
    def __init__(self, player_image, x, y, w, h, speed):
        super(). __init__(player_image, x, y, w, h)
        self.direction = "left"
        self.speed = speed
    def update(self):
        if self.rect.x <= 420: 
            self.direction = "right"
        if self.rect.x >= window_width - 85:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Bullet(GameSprite):
    def __init__(self, player_image, x, y, w, h, speed):
        super(). __init__(player_image, x, y, w, h)
        self.speed = speed
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > window_width + 10:
            self.kill()
enemy = Enemy("cyborg.png", 450, 200, 80, 80, 5)
final = GameSprite("pac-1.png", 550, 400, 80, 80)
wall1 = GameSprite("platform2.png",100, 200 , 300, 50)
wall2 = GameSprite("platform2_v.png", 350, 100, 75, 300)
barriers = sprite.Group()
barriers.add(wall1)
barriers.add(wall2)
hero = Player("hero.png", 5, window_height - 80, 80, 80, 0 , 0)
enemys = sprite.Group()
bullets = sprite.Group()
enemys.add(enemy)

while run:

    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_a:
                hero.x_speed = -5
            elif e.key == K_d:
                hero.x_speed = 5
            elif e.key == K_w:
                hero.y_speed = -5
            elif e.key == K_s:
                hero.y_speed = 5
            elif e.key == K_SPACE:
                hero.fire()
        elif e.type == KEYUP:
            if e.key == K_a:
                hero.x_speed = 0
            elif e.key == K_d:
                hero.x_speed = 0
            elif e.key == K_w:
                hero.y_speed = 0
            elif e.key == K_s:
                hero.y_speed = 0
    if finish == False:


        time.delay(50)
        window.fill(back)
        final.reset()
        barriers.draw(window)
        enemys.update()
        enemys.draw(window)
        bullets.update()
        bullets.draw(window)


        hero.reset()
        hero.update()
        if sprite.collide_rect(hero, final):
            finish = True
            img = image.load('thumb.jpg')
            window.fill((255,255,255))
            window.blit(transform.scale(img, (700, 500)), (0, 0))
        if sprite.collide_rect(hero, enemy):
            finish = True
            img = image.load('game-over_1.png')
            window.fill((255,255,255))
            window.blit(transform.scale(img, (700, 500)), (0, 0))
        sprite.groupcollide(enemys, bullets, True, True)
        sprite.groupcollide(bullets, barriers, True, False)

    clock.tick(40)
    display.update()
display.update()
