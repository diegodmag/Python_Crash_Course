import sys 

import pygame 

from bullet import Bullet

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
    if event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add it to the bullets Group
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        print(f"FIRE!\n")
        print(f"Starting posiiton bullet: {new_bullet.rect.centery}\n")
        print(f"Ship Y position: {ship.rect.centery}\n")

def check_keyup_events(event, ship):
    if event.key == pygame.K_d:
        ship.moving_right = False
    if event.key == pygame.K_a:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, bullets):
    """Update images on the screen and flip to the new screen"""
    # Redraw the screen during each pass through the loop 
    screen.fill(ai_settings.screen_color)
    
    # the bullets.sprites() returns a list of all the bullets in the group
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    # Make the most recently drawn screen visible.
    # This is the double buffering 
    pygame.display.flip()