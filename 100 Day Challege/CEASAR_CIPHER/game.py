letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, caesar_position, caesar_direction):
    answer = ""
    if caesar_direction.lower() == "decode":
        caesar_position *= -1

    for letter in text:
        if letter in letters:
            ind = letters.index(letter)
            position = (caesar_position + ind) % 26
            answer += letters[position]
        else:
            answer += letter
    return answer


while True:
    choice = input("Enter 'encode' for encryption and 'decode' for decryption:").lower()
    position_skip = int(input("Enter the number of letter to skip:"))
    code = input("Enter the text:").lower()
    result = caesar(code, position_skip, choice)
    print(f"The {choice}d is {result}")
    choice2 = input('Enter yes or no for continue:').lower()
    if choice2 == 'no':
        break
