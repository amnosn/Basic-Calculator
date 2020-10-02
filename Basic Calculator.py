def add(num1, num2):
    return num1 + num2

def divide(num1, num2):
    return num1 / num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def remainder(num1, num2):
    return num1 % num2

print("Please select one of the following options:\n")
print("1.Add\n2.Subtract\n3.Divide\n4.Multiply\n5.Remainder\n")
choice = int(input())
num1 = float(input("Enter number 1:"))
num2 = float(input("Enter number 2:"))

if choice == 1:
    print(add(num1, num2))
elif choice == 2:
    print(subtract(num1, num2))
elif choice == 3:
    print(divide(num1, num2))
elif choice == 4:
    print(multiply(num1, num2))
elif choice == 5:
    print(remainder(num1, num2))
else:
    print("Not a valid option")
