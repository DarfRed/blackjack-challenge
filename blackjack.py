from art import logo
import os
import random


def clear():
    """
    Clears the Console.
    """
    os.system("cls" if os.name == "nt" else "clear")


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def cpu_turn(cpu_hand, player_hand):
    cpu_score = sum(cpu_hand)
    player_score = sum(player_hand)
    while cpu_score < 17 and (cpu_score < player_score or cpu_score < 21):
        cpu_hand.append(deal_card())
        cpu_score = sum(cpu_hand)
    return cpu_hand


# Initialize Game
def game():
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if play == "y":
        player_hand = []
        cpu_hand = []
        players_turn = True

        clear()
        print(logo)

        player_hand.append(deal_card())
        cpu_hand.append(deal_card())
        cpu_hand.append(deal_card())

        while players_turn:
            player_hand.append(deal_card())
            # Aces count as 1 if Score is over 21
            if 11 in player_hand and sum(player_hand) > 21:
                for i in range(len(player_hand)):
                    if player_hand[i] == 11:
                        player_hand[i] = 1
            print(f"Your cards: {player_hand}, current score: {sum(player_hand)}")
            print(f"Computer's first card: {cpu_hand[0]}")

            # Implement Blackjack
            if len(cpu_hand) == 2 and sum(cpu_hand) == 21:
                players_turn = False
                print(f"Your final hand: {player_hand}, final score: {sum(player_hand)}")
                print(f"Computer's final hand: {cpu_hand}, final score: {sum(cpu_hand)}")
                print("Computer wins with a Blackjack!")
                game()
            elif len(player_hand) == 2 and sum(player_hand) == 21:
                players_turn = False
                cpu_hand = cpu_turn(cpu_hand, player_hand)
                print(f"Your final hand: {player_hand}, final score: {sum(player_hand)}")
                print(f"Computer's final hand: {cpu_hand}, final score: {sum(cpu_hand)}")
                print("You win with a Blackjack!")
                game()

            # Implement Player over
            elif sum(player_hand) > 21:
                players_turn = False
                cpu_hand = cpu_turn(cpu_hand, player_hand)
                print(f"Your final hand: {player_hand}, final score: {sum(player_hand)}")
                print(f"Computer's final hand: {cpu_hand}, final score: {sum(cpu_hand)}")
                print("You went over. You lose!")
                game()

            else:
                take_card = input("Type 'y' to get another card, type 'n' to pass: ")
                if take_card == "n":
                    players_turn = False
                    cpu_hand = cpu_turn(cpu_hand, player_hand)
                    print(f"Your final hand: {player_hand}, final score: {sum(player_hand)}")
                    print(f"Computer's final hand: {cpu_hand}, final score: {sum(cpu_hand)}")
                    if sum(player_hand) == sum(cpu_hand):
                        print("It's a draw.")
                        game()
                    elif sum(player_hand) <= 21 and sum(cpu_hand) > 21:
                        print("Computer went over, you win!")
                        game()
                    elif sum(player_hand) > sum(cpu_hand):
                        print("You win!")
                        game()
                    elif sum(player_hand) < sum(cpu_hand):
                        print("Computer wins!")
                        game()


game()
