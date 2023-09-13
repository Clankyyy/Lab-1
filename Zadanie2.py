import math


def Add(x, y):
    return x + y

def Subtract(x, y):
    return x - y

def Multiply(x, y):
    return x * y

def Divide(x, y):
    return x / y

def Power(x, y):
    return pow(x,y)

def Log(x,y):
    if y <= 0 or y == 1:
        print("Operation is non defined\n")
        return 0
    return math.log(x,y)

def round_ceil(x,y):
    y = int(y)
    x = str(x)
    number_list = list(x)
    round_ch = int(number_list[int(number_list.index('.')) + y]) + 1
    number_list[int(number_list.index('.')) + y] = str(round_ch)
    return ''.join(number_list)[:number_list.index('.') + y + 1]

def round_floor(x,y):
    y = int(y)
    x = str(x)
    number_list = list(x)
    round_ch = int(number_list[int(number_list.index('.')) + y]) - 1
    number_list[int(number_list.index('.')) + y] = str(round_ch)
    return ''.join(number_list)[:number_list.index('.') + y + 1]

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power")
print("6.Log")
print("7.Round ceil")
print("8.Round floor")

while True:
    choice = input("Enter choice(1/2/3/4/5/6/7/8): ")

    if choice in ('1', '2', '3', '4', '5', '6', '7', '8'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", Add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", Subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", Multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", Divide(num1, num2))
            
        elif choice == '5':
            print(num1, "**", num2, "=", Power(num1, num2))

        elif choice == '6':
            print("log", num2, "to", num1,  "=", Log(num1, num2))

        elif choice == '7':
            print(num1, "rounded to", round_ceil(num1, num2))

        elif choice == '8':
            print(num1, "rounded" , round_floor(num1, num2))
            
        
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")
