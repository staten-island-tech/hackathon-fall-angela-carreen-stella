import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Card Game")

# Colors (optional, for background)
BLACK = (0, 0, 0)

# Card class to represent each card on the board
class Card:
    def __init__(self, x, y, number, img_dict):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 100
        self.number = number
        self.flipped = False
        self.matched = False
        self.img_dict = img_dict  # Dictionary of card images
        self.card_image = self.img_dict[number]  # Select the image for this card

    def draw(self, surface):
        if self.flipped or self.matched:
            # If flipped or matched, display the card's image
            surface.blit(self.card_image, (self.x, self.y))
        else:
            # Display the back of the card
            surface.blit(self.img_dict["back"], (self.x, self.y))

    def check_click(self, pos):
        if self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height:
            return True
        return False

# Set up the card images
def load_images():
    img_dict = {}
    # Load the back card image
    image = pygame.image.load("card_back.png").convert_alpha()


    # Load images for the card faces
    for i in range(1, 9):
        image = pygame.image.load("card1.png")

    return img_dict

# Set up the cards
def create_deck(img_dict):
    numbers = list(range(1, 9)) * 2  # Create pairs of 1-8
    random.shuffle(numbers)
    cards = []
    for i in range(4):  # 4 rows
        for j in range(4):  # 4 columns
            card = Card(j * 120 + 50, i * 120 + 50, numbers.pop(), img_dict)
            cards.append(card)
    return cards

def main():
    img_dict = load_images()  # Load all images
    cards = create_deck(img_dict)  # Create the deck of cards
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
                    pygame.time.delay(500)
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
            text = font.render("You Win!", True, (255, 255, 255))
            screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()