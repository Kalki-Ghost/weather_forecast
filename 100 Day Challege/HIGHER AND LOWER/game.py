import random
from replit import clear
from game_art import logo, vs
from game_data import data

# List to keep track of used random numbers
number = []


def random_number_generator():
    """Generates a random number that hasn't been used before."""
    while True:
        random_number = random.randint(0, len(data) - 1)
        if random_number not in number:
            number.append(random_number)
            return random_number


def value(val):
    """Formats the value for display."""
    return f"{val['name']}, a {val['description']}, from {val['country']}."


# Print the game logo

game_over = False
score = 0

# Generate the first random number
current_num = random_number_generator()

while not game_over:
    print(logo)
    current_value = data[current_num]
    A = value(current_value)

    if score > 0:
        print(f"You're right! Current score: {score}")

    next_num = random_number_generator()
    next_value = data[next_num]
    B = value(next_value)

    print(f"Compare A: {A}")
    print(vs)
    print(f"Against B: {B}")

    flag = input("Who has more followers? Type 'A' or 'B': ").upper()
    clear()
    if (flag == 'A' and current_value['follower_count'] >= next_value['follower_count']) or \
            (flag == 'B' and current_value['follower_count'] <= next_value['follower_count']):
        score += 1
        current_num = next_num  # Update current_num with next_num for the next round
    else:
        print(f"A followers: {current_value['follower_count']}")
        print(f"B followers: {next_value['follower_count']}")
        print(f"Sorry, that's wrong. Final score: {score}")

        game_over = True
