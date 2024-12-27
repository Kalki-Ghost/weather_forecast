from logo_game import logo
import random


def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(owner):
    if sum(owner) == 21 and len(owner) == 2:
        return 0
    if 11 in owner and sum(owner) > 21:
        owner.remove(11)
        owner.append(1)
    return sum(owner)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "Your score went over.You lose😤."
    if user_score == computer_score:
        return "Match draw😊."
    elif computer_score == 0:
        return "Loss,opponent has Blackjack🙀"
    elif user_score == 0:
        return "Win with Blackjack😎."
    elif user_score > 21:
        return "You went over.You lose😭."
    elif computer_score > 21:
        return "Opponent went over. You win😁."
    elif user_score > computer_score:
        return "You win😊."
    else:
        return "You lose😤."


def play():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cards:{user_cards}, current score={user_score}")
        print(f" computer's first card:{computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True

        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal.lower() == 'y':
                user_cards.append(deal_cards())
            else:
                is_game_over = True
    computer_score = calculate_score(computer_cards)
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f" Your final hand:{user_cards}, final score:{calculate_score(user_cards)}")
    print(f" Computer's final hand:{computer_cards}, final score:{computer_score}")
    print(compare(calculate_score(user_cards), calculate_score(computer_cards)))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    play()
