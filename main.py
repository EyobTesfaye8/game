import pygame
import random

class Enemy:
    def __init__(self, surface,color):
        self.surf = surface
        self.rect = self.surf.get_rect(bottomright = (random.randint(220,1500),100))
        self.color = color
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
            bullet_rect.y -= 20
            screen.blit(bullet, bullet_rect)
        bullets = [bullet for bullet in bullets if bullet_rect.y > 0]
        return bullets
    else: return []    

def villans(villans):
    if villans:
        for villan_rect in villans:
            villan_rect.rect.y += 5
            if villan_rect.color == "yellow":
                screen.blit(villan1.surf, villan_rect)
                print("yellow")
            elif villan_rect.color == "gray":
                screen.blit(villan2.surf, villan_rect)
                print("gray")
            elif villan_rect.color == "purple":
                screen.blit(villan3.surf, villan_rect)
                print("purple")
         
        villans = [villan_rect for villan_rect in villans if villan_rect.rect.top < 1500]
        return villans
    else:return []

pygame.init()
screen = pygame.display.set_mode((1500,1500))
bullet_rect_list = []
villan_rect_list = [Enemy(surface = pygame.Surface((0,0)).convert_alpha(), color = "")]
speed = 5

background_surf = pygame.transform.rotozoom(pygame.image.load("background/black.jpeg").convert_alpha(),0,2.5)
back_rect = background_surf.get_rect(center = (750,750))

char = pygame.Surface((100,100)).convert_alpha()
char_rect = char.get_rect(midbottom = (750,1500))
char.fill('red')

bullet = pygame.Surface((25,25)).convert_alpha()
bullet_rect = bullet.get_rect(midbottom = char_rect.midtop)
bullet.fill('blue')

villan1 = Enemy(pygame.Surface((75,150)).convert_alpha(), "yellow")
# villan1_rect = villan1.get_rect(bottom = 0)
villan1.surf.fill("yellow")

villan2 = Enemy(pygame.Surface((50,50)).convert_alpha(), "gray")
# villan2_rect = villan2.get_rect(bottom = 0)
villan2.surf.fill("gray")

villan3 = Enemy(pygame.Surface((110,50)).convert_alpha(), "purple")
# villan3_rect = villan3.get_rect(bottom = 0)
villan3.surf.fill("purple")



shotT = 700
shootTiming = pygame.USEREVENT + 1
pygame.time.set_timer(shootTiming, shotT)
villansTime = pygame.USEREVENT + 2
pygame.time.set_timer(villansTime, 1500)

clock = pygame.time.Clock()
while True:
    movement()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == shootTiming:
            bullet_rect_list.append(bullet.get_rect(midbottom = char_rect.midtop))
        if event.type == villansTime:
            # print ("spawning monsters")
            c = random.randint(0,2)
            if c == 0:
                villan_rect_list.append(villan1)
            elif c == 1:
                villan_rect_list.append(villan2)
            else:
                villan_rect_list.append(villan3)

    
    screen.blit(background_surf, back_rect)
    screen.blit(char, char_rect)
    bullet_rect_list = shooting(bullet_rect_list)
    villan_rect_list = villans(villan_rect_list)
   
    
    pygame.display.update()
    clock.tick(60)
