# This the simple notepad application

def write_note():
    """The function to write the content to the required file."""
    file_name = input("Enter the file name:")
    note = ""
    print("Enter the note here(Write save to save the text):")
    while True:
        text = input()
        if text.lower() == 'save':
            break
        note += text + '\n'

    mode = input("Enter the mode: 'a' for append the text and 'w' for write the new content: ")
    if mode.lower() in ['a', 'w']:
        with open(f"{file_name}.txt", mode) as file:
            file.write(note)
        print(f"Content is saved to {file_name}.txt")
    else:
        print("You enter the wrong mode.")


def read_note():
    """The function is to view the content in the required file."""
    file_name = input("Enter the file name:")
    try:
        with open(f"{file_name}.txt", 'r') as file:
            print("Note in file:\n\n")
            print(file.read())
    except FileNotFoundError:
        print("Required file is not found.")


while True:
    choice = int(input("Enter the choice 1.write 2.Read 3.Exit\n"))
    if choice == 1:
        write_note()
    elif choice == 2:
        read_note()
    elif choice == 3:
        print("Good bye!")
        break
    else:
        print("Invalid choice")
