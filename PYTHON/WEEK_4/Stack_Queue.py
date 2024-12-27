class Stack:
    def __init__(self):
        self.arr = []
        self.top = -1

    def push(self, element):
        self.arr.append(element)
        self.top = self.top + 1

    def pop(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            self.top -= 1
            print(self.arr.pop())

    def display(self):
        print(f"Stack:{self.arr}")


class Queue:
    def __init__(self):
        self.arr = []
        self.rear = -1
        self.front = -1

    def enqueue(self, element):
        if self.front == -1 and self.rear == -1:
            self.arr.append(element)
            self.front += 1
            self.rear += 1
        else:
            self.arr.append(element)
            self.rear += 1

    def dequeue(self):
        if self.rear == -1:
            print("Queue is empty")
        elif self.rear == self.front:
            self.rear -= 1
            self.front -= 1
            ele = self.arr[0]
            del self.arr[0]
            print(ele)
        else:
            self.rear -= 1
            ele = self.arr[0]
            del self.arr[0]
            print(ele)

    def display(self):
        print(f"Queue:{self.arr}")


print("Stack operations:")
print("Push")
stack = Stack()
for i in range(3):
    stack.push(i)
stack.display()
print("pop")
for i in range(4):
    stack.pop()

print("Queue operations:")
print("Enqueue")
queue = Queue()
for i in range(3):
    queue.enqueue(i)
queue.display()
for i in range(4):
    queue.dequeue()
