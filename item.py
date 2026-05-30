import pygame
class Item:
    def __init__(self, x, y, image_path):
        self.x = x
        self.y = y
        self.width = 32
        self.height = 32
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        self.visible=True
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def is_visible(self):
        return self.visible
    def hide(self):
        self.visible=False
    def move(self,x,y):
        self.rect.x=x
        self.rect.y=y
    