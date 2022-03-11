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


def calculate_score(player_cards):
    if len(player_cards) == 2 and sum(player_cards) == 21:
        score = 0
        return score
    elif 11 in player_cards and sum(player_cards) > 21:
        player_cards.remove(11)
        player_cards.append(1)
        score = sum(player_cards)
        return score
    else:
        score = sum(player_cards)
    return score


def compare(player_score, cpu_score):
    if player_score == cpu_score:
        print("It's a draw.")
    elif cpu_score == 0:
        print("Computer wins with a Blackjack!")
    elif player_score == 0:
        print("You win with a Blackjack!")
    elif player_score > 21:
        print("You went over, you lose!")
    elif cpu_score > 21:
        print("Computer went over, you win!")
    elif cpu_score > player_score:
        print("Computer wins!")
    elif player_score > cpu_score:
        print("You win!")


def blackjack():
    clear()
    print(logo)

    game_continues = True
    user_cards = []
    computer_cards = []

    user_cards.append(deal_card())
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())

    while game_continues:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards are {user_cards}, total score: {user_score}")
        print(f"Computers first card is {computer_cards[0]}")

        if computer_score == 0:
            game_continues = False
            print(f"Computers final hand is {computer_cards}, total score: {computer_score}")
            compare(user_score, computer_score)
        elif user_score == 0:
            game_continues = False
            print(f"Computers final hand is {computer_cards}, total score: {computer_score}")
            compare(user_score, computer_score)
        elif user_score > 21:
            game_continues = False
            print(f"Computers final hand is {computer_cards}, total score: {computer_score}")
            compare(user_score, computer_score)
        else:
            new_card = input("Do you want to draw another card? y/n: ")
            if new_card == "y":
                user_cards.append(deal_card())
            else:
                game_continues = False
                while computer_score < 17:
                    computer_cards.append(deal_card())
                    computer_score = calculate_score(computer_cards)
                print(f"Computers final hand is {computer_cards}, total score: {computer_score}")
                compare(user_score, computer_score)

    new_game = input("Do you want to play again? y/n: ")
    if new_game == "y":
        blackjack()


play = input("Do you want to play Blackjack? y/n: ")
if play == "y":
    blackjack()
