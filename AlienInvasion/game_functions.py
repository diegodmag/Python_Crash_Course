import sys 

import pygame 

def check_events(ship):
    """Respond to keypressed and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                ship.moving_right = True
            elif event.key == pygame.K_a:
                ship.moving_left = True
            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                ship.moving_right = False
            if event.key == pygame.K_a:
                ship.moving_left = False

def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen"""
    # Redraw the screen during each pass through the loop 
    screen.fill(ai_settings.screen_color)
    
    ship.update()

    ship.blitme()
    # Make the most recently drawn screen visible.
    # This is the double buffering 
    pygame.display.flip()