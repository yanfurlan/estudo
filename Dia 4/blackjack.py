import tkinter as tk
from tkinter import messagebox
import random

# Configuração das cartas
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

# Função para criar um baralho
def create_deck():
    return [(value, suit) for suit in suits for value in values]

# Função para distribuir uma carta
def draw_card(deck):
    return deck.pop(random.randint(0, len(deck) - 1))

# Função para calcular a pontuação
def calculate_score(hand):
    score = sum(card_values[card[0]] for card in hand)
    aces = sum(1 for card in hand if card[0] == 'A')
    while score > 21 and aces:
        score -= 10
        aces -= 1
    return score

# Função para atualizar o display
def update_display():
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    player_cards_label.config(text=f"Player Cards: {', '.join(f'{v} of {s}' for v, s in player_hand)}")
    player_score_label.config(text=f"Player Score: {player_score}")
    dealer_cards_label.config(text=f"Dealer Cards: {', '.join(f'{v} of {s}' for v, s in dealer_hand)}")
    dealer_score_label.config(text=f"Dealer Score: {dealer_score}")

    if player_score > 21:
        messagebox.showinfo("Game Over", "Player Busted! Dealer Wins!")
        return
    if dealer_score > 21:
        messagebox.showinfo("Game Over", "Dealer Busted! Player Wins!")
        return
    if len(player_hand) == 2 and len(dealer_hand) == 2:
        if player_score == 21:
            messagebox.showinfo("Game Over", "Blackjack! Player Wins!")
            return
        if dealer_score == 21:
            messagebox.showinfo("Game Over", "Blackjack! Dealer Wins!")
            return

def hit():
    player_hand.append(draw_card(deck))
    update_display()

def stand():
    while calculate_score(dealer_hand) < 17:
        dealer_hand.append(draw_card(deck))
    update_display()
    dealer_score = calculate_score(dealer_hand)
    player_score = calculate_score(player_hand)
    if dealer_score > 21:
        messagebox.showinfo("Game Over", "Dealer Busted! Player Wins!")
    elif player_score > dealer_score:
        messagebox.showinfo("Game Over", "Player Wins!")
    elif player_score < dealer_score:
        messagebox.showinfo("Game Over", "Dealer Wins!")
    else:
        messagebox.showinfo("Game Over", "It's a Tie!")

def start_game():
    global deck, player_hand, dealer_hand
    deck = create_deck()
    player_hand = [draw_card(deck), draw_card(deck)]
    dealer_hand = [draw_card(deck), draw_card(deck)]
    update_display()

# Configuração da interface gráfica
root = tk.Tk()
root.title("Blackjack")

start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack()

hit_button = tk.Button(root, text="Hit", command=hit)
hit_button.pack()

stand_button = tk.Button(root, text="Stand", command=stand)
stand_button.pack()

player_cards_label = tk.Label(root, text="Player Cards: ")
player_cards_label.pack()

player_score_label = tk.Label(root, text="Player Score: ")
player_score_label.pack()

dealer_cards_label = tk.Label(root, text="Dealer Cards: ")
dealer_cards_label.pack()

dealer_score_label = tk.Label(root, text="Dealer Score: ")
dealer_score_label.pack()

root.mainloop()
