import pygame
import random
import time
pygame.init()
screen_width, screen_height = 1700, 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Card Game")

card_width = 310
card_height = 245
card_margin = 20
cols = 5
rows = 4
num_cards = rows * cols
cards = list(range(1, num_cards // 2 + 1)) * 2
random.shuffle(cards)
flipped_cards = []
matched_cards = []
card_images = []
for i in range(1, num_cards // 2 + 1):
    card_images.append(pygame.image.load(f'card_images/card{i}.png'))
font = pygame.font.SysFont('comic sans', 48)
running = True
def draw_board():
    for row in range(rows):
        for col in range(cols):
            card_index = row * cols + col
            x = col * (card_width + card_margin) + card_margin
            y = row * (card_height + card_margin) + card_margin
            card_value = cards[card_index]
            if card_index in matched_cards:
                pygame.draw.rect(screen, (0, 225, 0), (x, y, card_width, card_height))
            else:
                pygame.draw.rect(screen, (169, 169, 169), (x, y, card_width, card_height))
                if card_index in flipped_cards:
                    card_image = card_images[card_value - 1]
                    card_image = pygame.transform.scale(card_image, (card_width, card_height))
                    screen.blit(card_image, (x, y))
                pygame.draw.rect(screen, (0, 100, 0), (x, y, card_width, card_height), 3)
def flip_card(pos):
    global flipped_cards
    col = pos[0] // (card_width + card_margin)
    row = pos[1] // (card_height + card_margin)
    card_index = row * cols + col
    if card_index not in flipped_cards and card_index not in matched_cards:
        flipped_cards.append(card_index)
def check_for_match():
    global flipped_cards
    if len(flipped_cards) == 2:
        index1 = flipped_cards[0]
        index2 = flipped_cards[1]
        if cards[index1] == cards[index2]:
            matched_cards.extend([index1, index2])
        flipped_cards = []
while running:
    screen.fill((0, 100, 0))  # Background color (green)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            flip_card(mouse_pos)
    check_for_match()
    draw_board()
    if len(matched_cards) == num_cards:
        text = font.render("You Win!", True, (0, 0, 0))
        screen.blit(text, (screen_width / 2 - text.get_width() / 2, screen_height / 2 - text.get_height() / 2))
    pygame.display.flip()
pygame.quit()