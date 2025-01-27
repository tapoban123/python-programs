### Write a interactive program to performs all operations of stack using list.

def push(stk, item):
    stk.append(item)


def pop(stk):
    if len(stk) == 0:
        print("Underflow! No items present in stack.")
    else:
        popped = stk.pop()
        print(f"Item popped -> {popped}")


def display(stk):
    if len(stk) == 0:
        print("Empty stack!")
    else:
        print("Items in Stack:")
        for i in range(len(stk) - 1, -1, -1):
            print(stk[i])


def peek(stk):
    if len(stk) == 0:
        print("Empty stack!")
    else:
        print(f"Top -> {stk[-1]}")


def menu():
    print("STACK OPERATIONS:")
    print("Enter 0 to view operations.")
    print("Enter 1 to push.")
    print("Enter 2 to pop.")
    print("Enter 3 to peek.")
    print("Enter 4 to display.")
    print("Enter 5 to quit.")


stack = []
menu()

while True:
    user_input = int(input("Enter your choice: "))

    if user_input == 0:
        menu()

    elif user_input == 1:
        item = input("Enter new item: ")
        push(stk=stack, item=item)

    elif user_input == 2:
        pop(stack)

    elif user_input == 3:
        peek(stack)

    elif user_input == 4:
        display(stack)

    elif user_input == 5:
        print("Program executed successfully.")
        break

    else:
        print("Invalid choice. Please try again.")
        continue
