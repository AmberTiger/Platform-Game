import pygame
from Character import Character
from item import Item

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My First Pygame Game")
clock = pygame.time.Clock()
running = True
player = Character(100, 100, "character.png")
item = Item(200, 200, "life.png")
goal = Item(150,200, "goal.png")
trap = Item(0,500,"trap.png")
level = 1
# Create font
font = pygame.font.Font(None, 36)
font_gameover = pygame.font.Font(None, 60)
# Complex map
platform1 = [
    pygame.Rect(0, 520, 250, 80),      # ground
    pygame.Rect(350, 520, 450, 80),    # ground after hole
    pygame.Rect(500, 450, 180, 30),   # higher ground
    pygame.Rect(250, 300, 100, 30),
    pygame.Rect(400, 370, 100, 30)
]
platform2 = [
    pygame.Rect(0, 520, 250, 80),      # ground
    pygame.Rect(350, 520, 450, 80),    # ground after hole
    pygame.Rect(300, 450, 180, 30),   # higher ground
    pygame.Rect(250, 370, 100, 30),
    pygame.Rect(400, 300, 100, 30),
    pygame.Rect(400, 215, 100, 30),
    pygame.Rect(400, 130, 100, 30)
]
platforms=platform1
gravity = 0.8
player_y_velocity = 0
on_ground = False
while running:
    # 1. Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # 2. Keyboard input
    keys = pygame.key.get_pressed()
    player.move(keys)
    # Jump
    if keys[pygame.K_UP] and on_ground:
        player_y_velocity = -13
        on_ground = False
    # Apply gravity
    player_y_velocity += gravity
    player.rect.y += int(player_y_velocity)
    # Platform collision
    on_ground = False
    for platform in platforms:
        if player.rect.colliderect(platform):
            overlap_x = min(player.rect.right - platform.left, platform.right - player.rect.left)
            overlap_y = min(player.rect.bottom - platform.top, platform.bottom - player.rect.top)

            # If horizontal overlap is smaller, it's a SIDE collision (Wall)
            if overlap_x < overlap_y:
                if player.rect.centerx < platform.centerx:
                    player.rect.right = platform.left  # Hit left wall -> push out left
                else:
                    player.rect.left = platform.right  # Hit right wall -> push out right
            elif player.rect.y<platform.top and player.rect.left!=platform.right and player.rect.right!=platform.left and player_y_velocity > 0:
                player.rect.bottom = platform.top
                player_y_velocity = 0
                on_ground = True
            elif player_y_velocity < 0 and player.rect.top >= platform.bottom + int(player_y_velocity) - 1:
                    player.rect.top = platform.bottom  # Snap to the bottom of the platform
                    player_y_velocity = 0 
    
    # Check collision
    if item.is_visible() and player.rect.colliderect(item.rect):
        player.addOneLive()
        item.hide()
    if trap.is_visible() and player.rect.colliderect(trap.rect):
        player.minusOneLive()
        player.reset()
    if goal.is_visible() and player.rect.colliderect(goal.rect):
        player.reset()
        level+=1
        goal.move(400,30)
        trap.move(400,420)
        platforms=platform2

    if player.rect.bottom >= 600:
        player.minusOneLive()
        player.reset()

    
        
    # 3. Draw background
    screen.fill((30, 30, 30))
    # Draw platforms
    for platform in platforms:
        pygame.draw.rect(screen, (80, 160, 80), platform)
    # 4. Draw player
    player.draw(screen)
    if item.is_visible():
        item.draw(screen)
    if goal.is_visible():
        goal.draw(screen)
    if trap.is_visible():
        trap.draw(screen)
    # 5. Draw lives
    lives_text = font.render(f"Lives: {player.getLives()}", True, (255, 255, 255))
    screen.blit(lives_text, (20, 20))
    if player.lives <= 0:
        gameover_text = font_gameover.render("Game Over", True, (255, 0, 0))
        screen.blit(gameover_text, (300,240))
        player.lives = 0
    # 5. Update screen
    pygame.display.flip()
    # 6. Limit FPS
    clock.tick(60)
pygame.quit()