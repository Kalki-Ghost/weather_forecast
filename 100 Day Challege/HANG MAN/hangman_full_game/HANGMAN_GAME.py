import random
from hangman_art import stages, logo
from Hangman_game_words import word_list


print("Welcome to HANGMAN game.")
print(logo)
end_game = False
random_word = random.choice(word_list)
answer = ['_'] * len(random_word)
lives = 6
random_word = random_word.upper()
while not end_game:
    guess_letter = input("Enter letter in the word:").upper()
    if guess_letter in answer:
        print("You already guessed this letter.")
    if guess_letter in random_word:
        print(f"You guessed letter '{guess_letter}' in word.")
        for i in range(len(random_word)):
            if random_word[i] == guess_letter:
                answer[i] = guess_letter
        print(f"{''.join(answer)}")
        if '_' not in answer:
            print("You won.")
            end_game = True
        continue
    else:
        print(f"You guessed wrong letter '{guess_letter}'.")
        print(f"{''.join(answer)}")
        lives -= 1

    print(stages[lives])
    if lives == 0:
        print(f"Correct word is '{random_word}'")
        end_game = True
        print("Game over.")
