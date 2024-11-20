import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((1700, 1000))
pygame.display.set_caption("Memory Card Game")

card_width = 145
card_height = 170
card_margin = 20
cols = 10
rows = 5
num_cards = rows * cols
cards = list(range(1, num_cards // 2 + 1)) * 2
random.shuffle(cards)
flipped_cards = []
matched_cards = []
font = pygame.font.SysFont(None, 48)
running = True
clock = pygame.time.Clock()

def draw_board():
    for row in range(rows):
        for col in range(cols):
            card_index = row * cols + col
            x = col * (card_width + card_margin) + card_margin
            y = row * (card_height + card_margin) + card_margin
            card_value = cards[card_index]
            if card_index in matched_cards:
                pygame.draw.rect(screen, (0, 0, 0), (x, y, card_width, card_height))
            else:
                pygame.draw.rect(screen, (169, 169, 169), (x, y, card_width, card_height))
                if card_index in flipped_cards:
                    text = font.render(str(card_value), True, (255, 255, 255)) #text color
                    screen.blit(text, (x + card_width / 2 - text.get_width() / 2, y + card_height / 2 - text.get_height() / 2))
                pygame.draw.rect(screen, (0, 0, 0), (x, y, card_width, card_height), 3) #border

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
        pygame.display.update()
        time.sleep(0.5)
        flipped_cards = []

while running:
    screen.fill((0,100,0))
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
    clock.tick(60)
pygame.quit()
