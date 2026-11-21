import pygame

print('Setup Start')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print('Setup End')

print('Setup Loop')
while True:
    # Check for all events
    for event in pygame.event.get():
        print('Quitting')
        if event.type == pygame.QUIT:
            pygame.quit() # Close window
            quit() # End pygame
