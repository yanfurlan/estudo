import random

def draw_card():
    """Draw a card from the deck."""
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    return random.choice(cards)

def card_value(card):
    """Return the value of the drawn card."""
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 11
    else:
        return int(card)

def calculate_hand_value(hand):
    """Calculate the total value of the hand."""
    value = sum(card_value(card) for card in hand)
    ace_count = hand.count('A')
    while value > 21 and ace_count:
        value -= 10
        ace_count -= 1
    return value

def display_hand(player, hand, hide_second_card=False):
    """Display the player's hand."""
    if hide_second_card:
        print(f"{player} hand: {hand[0]}, X")
    else:
        print(f"{player} hand: {', '.join(hand)} (Value: {calculate_hand_value(hand)})")

def game():
    """Play a simple game of 21."""
    print("Welcome to the game of 21!")
    
    player_hand = [draw_card(), draw_card()]
    dealer_hand = [draw_card(), draw_card()]

    while True:
        display_hand("Player", player_hand)
        display_hand("Dealer", dealer_hand, hide_second_card=True)

        if calculate_hand_value(player_hand) == 21:
            print("Congratulations! You hit 21! You win!")
            return

        move = input("Do you want to 'hit' or 'stand'? ").lower()
        if move == 'hit':
            player_hand.append(draw_card())
            if calculate_hand_value(player_hand) > 21:
                display_hand("Player", player_hand)
                print("You busted! Dealer wins.")
                return
        elif move == 'stand':
            break
        else:
            print("Invalid input. Please enter 'hit' or 'stand'.")

    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(draw_card())

    display_hand("Player", player_hand)
    display_hand("Dealer", dealer_hand)

    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if dealer_value > 21 or player_value > dealer_value:
        print("Congratulations! You win!")
    elif player_value < dealer_value:
        print("Dealer wins.")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    game()
