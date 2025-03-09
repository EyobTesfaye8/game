import pygame
import random

class Enemy:
    def __init__(self, surface, color):
        self.surf = surface
        self.rect = self.surf.get_rect(bottomright = (random.randint(220,1500),random.randint(-700,-100)))
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
        char_rect.centery -= 10
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and char_rect.bottom < 1500:
        char_rect.centery += 10

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
            return False
    else: 
        return True

def Bcollision(bullets, villanis):
    if villanis:
        for Bul in bullets:
            for Vil in villanis:
                if Bul.colliderect(Vil.rect):
                    villanis.remove(Vil)
                    bullets.remove(Bul)

def score(bullets, villanis):
    if not villanis:
        global scoree
        scoree = 0
    else:
        for Bul in bullets:
            for Vil in villanis:
                if Bul.colliderect(Vil.rect) and Vil.color == "yellow":
                    scoree += 75
                elif Bul.colliderect(Vil.rect) and Vil.color == "gray":
                    scoree += 200
                elif Bul.colliderect(Vil.rect) and Vil.color == "purple":
                    scoree += 50
        score_surf = font3.render(f"SCORE: {scoree}", False, "white")    
        score_surf_rect = score_surf.get_rect(topleft = (50,50))
        screen.blit (score_surf,score_surf_rect)
    # return scoree

pygame.init()
screen = pygame.display.set_mode((1500,1500))
bullet_rect_list = []
villan_rect_list = []
speed = 5
game_active = False
level = 1

font1 = pygame.font.Font("font/game_font.otf",100)
font2 = pygame.font.Font("font/game_font.otf",200)
font3 = pygame.font.Font("font/game_font.otf",75)

background_surf = pygame.transform.rotozoom(pygame.image.load("background/black.jpeg").convert_alpha(),0,2.5)
back_rect = background_surf.get_rect(center = (750,750))

char = pygame.transform.rotozoom(pygame.image.load("char/aircraft.png").convert_alpha(),0,2)
char_rect = char.get_rect(midbottom = (750,1400))
char_scaled = pygame.transform.rotozoom(char,0,2)
char_scaled_rect = char_scaled.get_rect(center = (750,750))

bullet = pygame.transform.rotozoom(pygame.image.load("bullet/not_mine.svg").convert_alpha(),0,0.3)
# bullet = pygame.Surface((20,40)).convert_alpha()
bullet_rect = bullet.get_rect(midbottom = char_rect.midtop)
# bullet.fill('#df4211')

villan1 = Enemy(pygame.Surface((100,150)).convert_alpha(), "yellow")
villan1.surf.fill("yellow")

villan2 = Enemy(pygame.Surface((30,80)).convert_alpha(), "gray")
villan2.surf.fill("gray")

villan3 = Enemy(pygame.Surface((110,50)).convert_alpha(), "purple")
villan3.surf.fill("purple")

lobby = pygame.Surface((1500,1500)).convert_alpha()
lobby_rect = lobby.get_rect(topleft = (0,0))
lobby.fill('black')

Vtime = 1500
Stime = 400
shootTiming = pygame.USEREVENT + 1
pygame.time.set_timer(shootTiming, Stime)
villansTime = pygame.USEREVENT + 2
pygame.time.set_timer(villansTime,Vtime)

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
                if c > 0:
                    villan_rect_list.append(Enemy(villan1.surf, "yellow"))
                if c < 2:
                    villan_rect_list.append(Enemy(villan2.surf, "gray"))
                if c == 0 or c == 2:
                    villan_rect_list.append(Enemy(villan3.surf, "purple")) 
        else: 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                bullet_rect_list = []
                villan_rect_list = []
                char_rect.midbottom = (750,1400)
                scoree = 0
    if game_active:
        movement()
        screen.blit(background_surf, back_rect)
        screen.blit(char, char_rect)
        bullet_rect_list = shooting(bullet_rect_list)
        villan_rect_list = villans(villan_rect_list)
        Scollisions(char_rect, villan_rect_list)
        score(bullet_rect_list,villan_rect_list)
        Bcollision(bullet_rect_list,villan_rect_list)

         

        level_surf = font3.render("LEVEL: "+ str(level),False,"white")
        level_surf_rect = level_surf.get_rect(topright = (1450,50))

        
        screen.blit (level_surf,level_surf_rect)

        game_active = Scollisions(char_rect,villan_rect_list)
    else: 
        score(bullet_rect_list,villan_rect_list)
        screen.blit(lobby, lobby_rect)
        lobby_message = font1.render("PRESS ANY KEY TO START MA NIGGA",False,'white') 
        lobby_message_rect = lobby_message.get_rect(center = (750,400))

        game_name = font2.render("PEW PEW GAME",False,'white') 
        game_name_rect = game_name.get_rect(center = (750, 200))

        lobby_score_surf = font3.render(f"SCORE: {scoree}", False, "white")    
        lobby_score_surf_rect = lobby_score_surf.get_rect(center = (750,1000))
        if scoree == 0:
            screen.blit(game_name,game_name_rect)
        else:
            screen.blit (lobby_score_surf,lobby_score_surf_rect)

        screen.blit(lobby_message, lobby_message_rect)
        screen.blit(char_scaled, char_scaled_rect)
    
    pygame.display.update()
    clock.tick(60)
