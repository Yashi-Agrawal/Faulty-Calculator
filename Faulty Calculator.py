# Faulty-Calculator

print("+ for Addition\n- for Substraction\n* for Multiplication \n/ for float Division \n** for exponentiation \n// for integer division\n% for Modulo operation \n")

# Input two numbers :

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

# Select any operation which you want to do ...

operation = input("Select any operation... :")

if (operation == '+'):
    if (num1 == 56 and num2 == 9):
        print("56 + 9 = 77")
    else:
        print("Addition of these two numbers is :  ", num1 + num2)

elif (operation == '-'):
    print("Substraction of these two numbers is :  ", num1 - num2)

elif (operation == '*'):
    if (num1 == 45 and num2 == 3):
        print("45 * 3 = 555")
    else:
        print("Multiplication of these two numbers is :  ", num1 * num2)

elif (operation == '/'):
    if (num1 == 56 and num2 == 6):
        print(" 56/6 = 4")
    else:
        print("Float Division of these two numbers is :  ", num1 / num2)

elif (operation == '**'):
    print("Exponentiation of these two numbers is :  ", num1 ** num2)

elif (operation == '//'):
    print("Integer Division of these two numbers is :  ", num1 // num2)

elif (operation == '%'):
    print("Modulus of these two numbers is :  ", num1 % num2)