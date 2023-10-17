def add(a,b):
    print(f"\n {a} + {b} = {a+b}\n")

def subtract(a,b):
    print(f"\n {a} - {b} = {a-b}\n")
    
def multiply(a,b):
    print(f"\n {a} * {b} = {a*b}\n")
    
def divide(a,b):
    print(f"\n {a} / {b} = {a/b}\n")
    
while True:
    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("5: Quit")
    choice = int(input("Enter an option (1/2/3/4/5): "))
    if 0 < choice < 5:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        if choice == 1:
            add(a,b)
        elif choice == 2:
            subtract(a,b)
        elif choice == 3:
            multiply(a,b)
        elif choice == 4:
            divide(a,b)
    elif choice == 5:
        print("\nThank you for using simple calculator.\n")
    else:
        print("\nInvalid input, try again later.\n")
        