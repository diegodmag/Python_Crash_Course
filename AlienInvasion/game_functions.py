import sys 

import pygame 

from bullet import Bullet

from alien import Alien

def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypressed and mouse events"""
    for event in pygame.event.get(): # pygame.event.get() returns a list of events 
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to KEYDOWN events"""
    if event.key == pygame.K_ESCAPE:
        sys.exit()
    elif event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)

def check_keyup_events(event, ship):
    if event.key == pygame.K_d:
        ship.moving_right = False
    if event.key == pygame.K_a:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, bullets, aliens):
    """Update images on the screen and flip to the new screen"""
    # Redraw the screen during each pass through the loop 
    screen.fill(ai_settings.screen_color)
    
    # the bullets.sprites() returns a list of all the bullets in the group
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme() # blit the ship onto the screen 

    for aliens in aliens:
        aliens.blitme()
    # Draw aliens

    # Make the most recently drawn screen visible.
    # This is the double buffering 
    pygame.display.flip()

def update_bullets(bullets, deltaTime):
    bullets.update()

    # Check for bullets out the screen 
    # Golden rule: Never modifie a list that is being iterated 
    # copy creates a list that point to the same elements 
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0: 
            bullets.remove(bullet) 
    # The group that is being iterated is the copy 
    # but the modified is the original 

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed: 
        # Create a new bullet and add it to the bullets Group
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


# We should have some alien specific system 

# This is homemade a function that determines the space betwwen alines 
def create_fleet(ai_settings, screen, aliens):
    # Determine the spacing
    # Spacing between aliens is one width and height 
    alien_model = Alien(ai_settings,screen) # Just for measurements 
    alien_width, alien_height =  alien_model.rect.size # get dimentions 

    screen_width, screen_height = screen.get_size() 

    current_x, current_y = alien_width, alien_height

    while current_y < screen_height - alien_height*3:
        # Row creation 
        while current_x < screen_width*2:
            create_alien(ai_settings, screen, current_x, current_y, aliens);            
            current_x += alien_width*2
        current_x = alien_width
        current_y+=alien_height*2
        
    # while(cont<screen_width-alien_width):
    #     cont += alien_width
        # create_alien(ai_settings, screen, cont, aliens);            

    # Each space_x we set a new alien 
    # for i in range(ai_settings.aliens_ammount):
    #     alien_starting_x_pos = (i+1) * space_x
    #     if(alien_starting_x_pos < ai_settings.screen_width):
    #         create_alien(ai_settings, screen, alien_starting_x_pos, aliens)

def create_alien(ai_settings, screen, x_pos, y_pos, aliens):
    new_alien = Alien(ai_settings, screen) 
    # new_alien.center = x_pos
    new_alien.x = x_pos 
    new_alien.rect.x = x_pos
    new_alien.rect.y = y_pos
    aliens.append(new_alien)

def update_aliens(aliens, deltaTime):
    for alien in aliens:
        alien.update(deltaTime)