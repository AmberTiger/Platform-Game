import pygame

class Character:
    def __init__(self, x, y, image_path, lives=3):
        self.lives = lives
        self.width = 40
        self.height = 40
        self.speed = 3
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = pygame.Rect(x, y, self.width, self.height)
    def move(self, keys):
        if self.game_over() == True:
            return
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def getLives(self):
        return self.lives
    def addOneLive(self):
        self.lives += 1
    def minusOneLive(self):
        self.lives -= 1
    def reset(self):
        self.rect.x = self.x
        self.rect.y = self.y
    def game_over(self):
        if self.lives == 0:
            return True
        else:
            return False