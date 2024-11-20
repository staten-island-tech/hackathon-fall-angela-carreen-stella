import pygame

pygame.init()
screen = pygame.display.set_mode((1700, 1000))
player_pos = pygame.Vector2(850, 500)
player_size = 10
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    dt = clock.get_time() / 1000
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    screen.fill((0,100,0))
    
    pygame.draw.rect(screen, (245, 245, 220), (player_pos.x - player_size / 2, player_pos.y - player_size / 2, player_size, player_size))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()