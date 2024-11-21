import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Card Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)

# Card class to represent each card on the board
class Card:
    def __init__(self, x, y, number):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 100
        self.number = number
        self.flipped = False
        self.matched = False

    def draw(self, surface):
        if self.flipped or self.matched:
            pygame.draw.rect(surface, WHITE, (self.x, self.y, self.width, self.height))
            font = pygame.font.SysFont(None, 48)
            text = font.render(str(self.number), True, BLACK)
            text_rect = text.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
            surface.blit(text, text_rect)
        else:
            pygame.draw.rect(surface, GREY, (self.x, self.y, self.width, self.height))

    def check_click(self, pos):
        if self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height:
            return True
        return False

# Set up the cards
def create_deck():
    numbers = list(range(1, 9)) * 2  # Create pairs of 1-8
    random.shuffle(numbers)
    cards = []
    for i in range(4):  # 4 rows
        for j in range(4):  # 4 columns
            card = Card(j * 120 + 50, i * 120 + 50, numbers.pop())
            cards.append(card)
    return cards

def main():
    cards = create_deck()
    flipped_cards = []  # List to hold flipped cards
    matched_pairs = 0
    game_over = False
    clock = pygame.time.Clock()

    while not game_over:
        screen.fill(BLACK)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.MOUSEBUTTONDOWN and len(flipped_cards) < 2:
                # Check if a card is clicked
                for card in cards:
                    if card.check_click(event.pos) and not card.flipped and not card.matched:
                        card.flipped = True
                        flipped_cards.append(card)

                # Check if two cards are flipped
                if len(flipped_cards) == 2:
                    if flipped_cards[0].number == flipped_cards[1].number:
                        flipped_cards[0].matched = True
                        flipped_cards[1].matched = True
                        matched_pairs += 1
                    # Pause for a moment to let the player see the result
                    pygame.time.delay(50)
                    # Flip back unmatched cards
                    for card in flipped_cards:
                        if not card.matched:
                            card.flipped = False
                    flipped_cards = []

        # Draw all cards
        for card in cards:
            card.draw(screen)

        # Check if all pairs are matched
        if matched_pairs == len(cards) // 2:
            font = pygame.font.SysFont(None, 48)
            text = font.render("You Win!", True, WHITE)
            screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
