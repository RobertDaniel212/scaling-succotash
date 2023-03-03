import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, window_width, window_height):
        super().__init__()
        self.image = pygame.image.load("kisspng-video-game-2d-computer-graphics-platform-game-clip-ground-5abba3931c8d80.979780851522246547117.png")
        self.rect = self.image.get_rect()
        self.rect.x = window_width
        self.rect.y = window_height
        

# create a group for platforms
platforms = pygame.sprite.Group()

# create some platforms and add them to the group
platforms.add(Platform(2, 200))

pygame.display.update(window_width, window_height)