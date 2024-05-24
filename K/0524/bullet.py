import pygame


class Bullet:
    def __init__(self,screen_surf):
        self.bullet_rect = pygame.Rect(0,0,10,30)
        self.screen_surf = screen_surf

    def render(self):
        pygame.draw.rect(self.screen_surf, 'red', self.bullet_rect)

    def move_front_ship(self,ship_rect):
        self.bullet_rect.midbottom = ship_rect.midtop

