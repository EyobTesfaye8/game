import pygame
import random

class Enemy:
    def __init__(self, surface,color):
        self.surf = surface
        self.rect = self.surf.get_rect(bottomright = (random.randint(220,1500),-100))
        self.color = color
    def move(self):
        self.rect.y += 5
def movement():
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and char_rect.right < 1500:
        char_rect.centerx += 15
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and char_rect.left > 0:
        char_rect.centerx -= 15
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and char_rect.top > 0:
        char_rect.centery -= 15 
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and char_rect.bottom < 1500:
        char_rect.centery += 15

def shooting(bullets):
    if bullets:
        for bullet_rect in bullets:
            bullet_rect.y -= 15
            screen.blit(bullet, bullet_rect)
        bullets = [bullet for bullet in bullets if bullet_rect.y > 0]
        return bullets
    else: return []    

def villans(villans):
    if villans:
        for villan_rect in villans:
            villan_rect.move()
            if villan_rect.color == "yellow":
                screen.blit(villan1.surf, villan_rect)
            elif villan_rect.color == "gray":
                screen.blit(villan2.surf, villan_rect)
            elif villan_rect.color == "purple":
                screen.blit(villan3.surf, villan_rect)
        villans = [villan_rect for villan_rect in villans if villan_rect.rect.top < 1500]
        return villans
    else:return []

def Scollisions(charRect, Villain_rect):
    for Vrect in Villain_rect:
        if charRect.colliderect(Vrect.rect):
            print ("collide")
            return True
    else: 
        return False


pygame.init()
screen = pygame.display.set_mode((1500,1500))
bullet_rect_list = []
villan_rect_list = []
speed = 5
game_active = True

background_surf = pygame.transform.rotozoom(pygame.image.load("background/black.jpeg").convert_alpha(),0,2.5)
back_rect = background_surf.get_rect(center = (750,750))

char = pygame.Surface((100,100)).convert_alpha()
char_rect = char.get_rect(midbottom = (750,1500))
char.fill('red')

bullet = pygame.Surface((25,25)).convert_alpha()
bullet_rect = bullet.get_rect(midbottom = char_rect.midtop)
bullet.fill('blue')

villan1 = Enemy(pygame.Surface((75,150)).convert_alpha(), "yellow")
villan1.surf.fill("yellow")

villan2 = Enemy(pygame.Surface((80,80)).convert_alpha(), "gray")
villan2.surf.fill("gray")

villan3 = Enemy(pygame.Surface((110,50)).convert_alpha(), "purple")
villan3.surf.fill("purple")

lobby = pygame.Surface((1500,1500)).convert_alpha()
lobby.fill('black')

shotT = 400
shootTiming = pygame.USEREVENT + 1
pygame.time.set_timer(shootTiming, shotT)
villansTime = pygame.USEREVENT + 2
pygame.time.set_timer(villansTime, random.randint(1000, 3000))

clock = pygame.time.Clock()
while True:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active: 
            if event.type == shootTiming:
                bullet_rect_list.append(bullet.get_rect(midbottom = char_rect.midtop))
            if event.type == villansTime:
                c = random.randint(0,2)
                if c == 0:
                    villan_rect_list.append(Enemy(villan1.surf, "yellow"))
                elif c == 1:
                    villan_rect_list.append(Enemy(villan2.surf, "gray"))
                else:
                    villan_rect_list.append(Enemy(villan3.surf, "purple"))
            if Scollisions:
                print ("Game Over")
                game_active = False    
            
    if game_active:
        movement()
        screen.blit(background_surf, back_rect)
        bullet_rect_list = shooting(bullet_rect_list)
        villan_rect_list = villans(villan_rect_list)
        screen.blit(char, char_rect)
        Scollisions(char_rect, villan_rect_list)
    else: 
        screen.blit(lobby, back_rect)
    
    pygame.display.update()
    clock.tick(60)
