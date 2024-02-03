import pygame
pygame.init()
clock = pygame.time.Clock()

SCREEN = pygame.display.set_mode((1500,500))
BG = pygame.transform.scale(pygame.image.load("Images/obloha.png"),(500,500))
ZEM = pygame.transform.scale(pygame.image.load("Images/Zem2.png"),(500,50))
PLATFORM = pygame.transform.scale(pygame.image.load("Images/Zem2.png"),(200,20))
FINISH = pygame.transform.scale(pygame.image.load("Images/Finish.png"),(200,50))
MENU = pygame.transform.scale(pygame.image.load("Images/Menu.png"),(1500,500))
CREDITS = pygame.transform.scale(pygame.image.load("Images/Credits.png"),(1500,500))
GAMEOVER = pygame.transform.scale(pygame.image.load("Images/GameOver.png"),(1500,500))
WIN = pygame.transform.scale(pygame.image.load("Images/Win.png"),(1500,500))
pygame.display.set_caption("Mario")

GROUNDCOLOR = (28,118,23)
WINCOLOR = (118,23,23)
GOOMBACOLOR = (148,80,4)
FPS = 60

testMario = pygame.transform.scale(pygame.image.load("Images/MarioRunAnim.png").convert_alpha(),(60,80))

def get_image(sheet,width,height):
    image = pygame.Surface((width,height)).convert_alpha()
    image.blit(sheet,(0,0))
    return image

class Mario():
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load("Images/Mario.png"),(50,50))
        self.x = 0
        self.y = 50
        self.vel = 7
        self.jump = False
        self.max_height = 0
        self.win = False
        self.dead = False
    def draw(self):
        SCREEN.blit(self.image, (self.x, self.y))
    def move_right(self):
        self.x += self.vel
    def move_left(self):
        self.x -= self.vel
    def fall(self,):
        if SCREEN.get_at((self.x+25,self.y+50)) != pygame.Color(GROUNDCOLOR):
            self.y +=10
    def jumping(self):
        if self.jump ==True:
            
            if self.y >= self.max_height:
                self.y -=10
            else:
                self.jump = False
                self.can_jump = False          
class Goomba():
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load("Images/Goomba.png"),(50,50))
        self.x = 400
        self.y = 404
        self.vel = 5
        self.left = 200
        self.right = 700
        self.moving =1
    def draw(self):
        SCREEN.blit(self.image, (self.x, self.y))
    def move(self):
        if self.x == self.right or self.x == self.left:
            self.moving *=-1
        self.x += self.vel*self.moving

def move_player(mario):
    keys = pygame.key.get_pressed()
    if SCREEN.get_at((mario.x+25,mario.y+50)) == pygame.Color(WINCOLOR):
        mario.win = True
    if SCREEN.get_at((mario.x+25,mario.y+20)) == pygame.Color(GOOMBACOLOR):
        mario.dead = True
    if keys[pygame.K_a]:
        mario.move_left()
    if keys[pygame.K_d]:
        mario.move_right()
    if keys[pygame.K_w]:
        if SCREEN.get_at((mario.x+25,mario.y+50)) == pygame.Color(GROUNDCOLOR):
            mario.max_height = mario.y - 150
            mario.jump = True
    if mario.jump == True:
        mario.jumping()
    else:
        mario.fall()
    mario.draw()
def chose():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        return 1
    if keys[pygame.K_w]:
        return 2
    if keys[pygame.K_e]:
        return 3
def Play():
    run = True
    goomba = Goomba()
    mario = Mario()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        clock.tick(FPS)
        SCREEN.blit(BG,(0,0))
        SCREEN.blit(BG,(500,0))
        SCREEN.blit(BG,(1000,0))
        SCREEN.blit(ZEM,(0,450))
        SCREEN.blit(ZEM,(500,450))
        SCREEN.blit(ZEM,(1000,450))
        SCREEN.blit(PLATFORM,(500,330))
        SCREEN.blit(FINISH,(1300,450))
        goomba.draw()
        goomba.move()
        move_player(mario)
        pygame.display.update()
        if mario.win == True:
            return 1
        if mario.dead == True:
            return 2
def GameOver():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        SCREEN.blit(GAMEOVER,(0,0))
        pygame.display.update()
def GameWin():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        SCREEN.blit(WIN,(0,0))
        pygame.display.update()
def Credits():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        SCREEN.blit(CREDITS,(0,0))
        pygame.display.update()
    
def Menu():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        SCREEN.blit(MENU,(0,0))
        frame0 = get_image(testMario,60,40)
        SCREEN.blit(frame0,(0,0))

        choice = chose()
        if choice == 1:
            state = Play()
            if state == 1:
                GameWin()
            if state == 2:
                GameOver()
        if choice == 2:
            break
        if choice == 3:
            Credits()
        pygame.display.update()
if __name__ == "__main__":
    Menu()
pygame.quit()