# It is the to do list app list it maintain the list of details that you provide.

todo_list = []


def add_task():
    todo_list.append(input("Enter the task:"))


def view_task():
    for i in range(len(todo_list)):
        print(f"{i + 1}.{todo_list[i]}")


while True:
    print("""Enter 1.Add the task
      2.View the task
      3.To exit""")
    choice = int(input("Enter the choice:"))

    if choice == 1:
        add_task()
    elif choice == 2:
        view_task()
    elif choice == 3:
        print("Good bye!")
        break
    else:
        print("Invalid choice")
