
import sys
import pygame

from alien import Alien
from bullet import Bullet
from ship import Ship


class Game:
    def __init__(self,title):
        self.title = title
        pygame.init()
        self.creat_screen()
        self.creat_ship()
        self.creat_alien()
        self.creat_score()
        self.bullets=[]
        self.clock = pygame.time.Clock()

   
    def creat_score(self):
        score_font = pygame.font.SysFont(None, 64)
        self.score_font_surf = score_font.render(str(5643), True, 'black')

    def creat_alien(self):
        self.aliens = []
        # alien = Alien(self.screen_surf)
        # alien.move(50,50)
        # self.aliens.append(alien)
        for i in range(1,5):
            for j in range(10):
                alien = Alien(self.screen_surf)
                x_pos = 80+(80*2)*j
                y_pos = 50+(50*2)*i
                alien.move(x_pos, y_pos)
                self.aliens.append(alien)

    def creat_ship(self):
        self.ship = Ship(self.screen_surf)
        self.ship.move_midbottom()

    def creat_screen(self):
        self.screen_surf = pygame.display.set_mode(size=(800,640))
    
    def start(self):
        while True:
            events = pygame.event.get()
            for e in events:
                print(e.type, type(e.type))
                if e.type == pygame.QUIT:
                    sys.exit()
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_LEFT:
                        self.left_pressed = True
                    elif e.key == pygame.K_RIGHT:
                        self.right_pressed = True
                        
                elif e.type == pygame.KEYUP:
                    if e.key == pygame.K_LEFT:
                        self.left_pressed = False
                    elif e.key == pygame.K_RIGHT:
                        self.right_pressed = False
                    elif e.key == pygame.K_SPACE:
                        bullet = Bullet(self.screen_surf)
                        bullet.move_front_ship(self.ship.get_rect())
                        self.bullets.append(bullet)
            
            self.ship.update()
        
            self.ship.render()     
            pygame.display.flip()
            self.clock.tick(60)
            
            # 여기 밑은 이동예정
            self.screen_surf.fill('white')
            for alien in self.aliens:
                alien.render()
            for bullet in self.bullets:
                bullet.render()
            self.screen_surf.blit(self.font_surf,(100,100,self.font_surf.get_rect().height,50))
    def __str__(self):
        return self.title




