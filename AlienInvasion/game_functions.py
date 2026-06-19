import sys 

import pygame 

from bullet import Bullet

from alien import Alien

def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypressed and mouse events"""
    for event in pygame.event.get():
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

    ship.blitme()

    for aliens in aliens:
        aliens.blitme()
    # Draw aliens

    # Make the most recently drawn screen visible.
    # This is the double buffering 
    pygame.display.flip()

def update_bullets(bullets):
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


# This is homemade a function that determines the space betwwen alines 
def set_aliens(ai_settings, screen, aliens):
    # alien = Alien(ai_settings,screen)

    # Determine the spacing
    space_x = float(ai_settings.screen_width)/ai_settings.aliens_ammount

    # Each space_x we set a new alien 
    for i in range(ai_settings.aliens_ammount):
        alien_starting_x_pos = (i+1) * space_x
        if(alien_starting_x_pos < ai_settings.screen_width):
            new_alien = Alien(ai_settings, screen) # create a new alien
            new_alien.center = alien_starting_x_pos
            print(f"The alien should be set at {alien_starting_x_pos}")
            aliens.append(new_alien)

def update_aliens(aliens):
    for alien in aliens:
        alien.update()