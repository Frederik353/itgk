import random

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
deck = cards*4

def draw_card():
    if len(deck) == 0:
        print("No more cards in the deck.")
        return None
    card = random.choice(deck)
    deck.remove(card)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Ekte Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def play_blackjack():
    player_cards = []
    dealer_cards = []

    for _ in range(2):
        player_cards.append(draw_card())
        dealer_cards.append(draw_card())

    game_over = False

    while not game_over:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"Dealers cards are {dealer_cards[0]}, and Your score is: {player_score}" )

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            another_card = input("Do you want another card? (Y/N): ").lower()
            if another_card == "y":
                player_cards.append(draw_card())
            else:
                game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(draw_card())
        dealer_score = calculate_score(dealer_cards)

    print(f"Dealers cards are {dealer_cards[0]} and {dealer_cards[1]}")
    print(f"Dealers score is: {dealer_score}")

    if player_score > 21:
        print("You lost")
    elif dealer_score > 21 or player_score > dealer_score:
        print("You won!")
    elif player_score == dealer_score:
        print("It's a draw")
    else:
        print("You lost")

play_blackjack()
