import pygame

pygame.init()

screen_surf = pygame.display.set_mode((1280,720))

ship_img = pygame.image.load('images/ship.bmp')
alien_img = pygame.image.load('images/alien.bmp')

# ship_rect = pygame.rect.Rect(0,0,100,100)
# alien_rect = pygame.rect.Rect(200,200,200,200)

ship_rect = ship_img.get_rect()
ship_rect.midbottom = screen_surf.get_rect().midbottom

alien_rect = alien_img.get_rect()

# bullet_rect = pygame.rect.Rect(0,0,5,30)
# bullet_rect.midbottom = ship_rect.midtop
bullet_rect = None
bullets = []

aliens = []
alien_x_pos = alien_rect.width
alien_y_pos = alien_rect.height
for _ in range(10):
    alien = pygame.rect.Rect(alien_x_pos, alien_y_pos,\
                            alien_rect.width,\
                            alien_rect.height)
    alien_x_pos += alien_rect.width * 2
    aliens.append(alien)
# screen_rect = screen_surf.get_rect()
# while alien_width < (screen_rect.width - 2 * alien_width):
    # alien = pygame.rect.Rect(alien_x_pos,alien_y_pos,alien_width,alien_height)
    # aliens.append(alien)

clock = pygame.time.Clock()

left_pressed = False
right_pressed = False
up_pressed = False
down_pressed = False

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # 총알발사
                if len(bullets) < 5:
                    bullet_rect = pygame.rect.Rect(0, 0, 5, 30)
                    bullet_rect.midbottom = ship_rect.midtop
                    bullets.append(bullet_rect)
            if event.key == pygame.K_RIGHT:    
                right_pressed = True   
            elif event.key == pygame.K_LEFT:
                left_pressed = True
            elif event.key == pygame.K_UP:
                up_pressed = True
            elif event.key == pygame.K_DOWN:   
                down_pressed = True
        elif event.type == pygame.KEYUP:
            # if event.key == pygame.K_SPACE:
            #     bullet_rect = None
            if event.key == pygame.K_RIGHT:
                right_pressed = False
            elif event.key == pygame.K_LEFT:
                left_pressed = False
            elif event.key == pygame.K_UP:
                up_pressed = False
            elif event.key == pygame.K_DOWN:
                down_pressed = False

    # Do logical updates here.

    if right_pressed:
        screen_rect = screen_surf.get_rect()
        if ship_rect.x < screen_rect.width - ship_rect.width:
            ship_rect.x = ship_rect.x + 10
        if alien_rect.x < screen_rect.width - alien_rect.width:
            alien_rect.x = alien_rect.x + 20
   
    if left_pressed:
        if 0< ship_rect.x:
            ship_rect.x = ship_rect.x - 10
        if 0< alien_rect.x:
            alien_rect.x = alien_rect.x - 20
        
    if up_pressed:
        ship_rect.y = ship_rect.y - 10
        alien_rect.y = alien_rect.y - 20
        
    if down_pressed:
        ship_rect.y = ship_rect.y + 10
        alien_rect.y = alien_rect.y + 20

    if bullets:
        screen_rect = screen_surf.get_rect()
       
        for bullet in bullets:
            if bullet.y < 0:
                bullets.remove(bullet) 
        for bullet in bullets:
            bullet.y = bullet.y - 10
    
        


    screen_surf.fill("black")  # Fill the display with a solid color

    # Render the graphics here.
    screen_surf.blit(ship_img, ship_rect)
    # screen_surf.blit(alien_img, alien_rect)
    if aliens:
        screen_rect = screen_surf.get_rect()
        for alien in aliens:
            if screen_rect.width - alien.width < alien.x:
                alien_x_direction = -1
                alien_y_pos =+ 10
                break
            elif alien.x < screen_rect.x:
                alien_x_direction =1
                alien_x_direction_changed = True
                break

        for alien in aliens:
              
            
            
            screen_surf.blit(alien_img, alien)
            
    if bullets:
        for bullet in bullets:
            pygame.draw.rect(screen_surf, 'yellow', bullet)

    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)