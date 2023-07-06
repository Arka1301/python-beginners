from art import calc_logo


def add(n1,n2):
    return n1 + n2


def subtract(n1,n2):
    return n1 - n2


def multiply(n1,n2):
    return n1 * n2


def divide(n1,n2):
    return n1 / n2



operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

condition1 = True


# while condition1:
#     num1 = int(input("What's the first number?: "))
#
#     condition2 = True
#
#     for key in operations:
#         print(key)
#
#     while condition2:
#
#         choice = input("Choose an operation from above: ")
#
#         num2 = int(input("What's the next number?: "))
#
#         ans = operations[choice](num1,num2)
#
#         print(f"{num1} {choice} {num2} = {ans}")
#
#         num1 = ans
#
#         cont = input("Do you want to continue? Type 'yes' or 'no'. ").lower()
#
#         if cont == 'no':
#             condition2 = False
#             count1 = input("Do you want to start a new calculation? Type 'yes' or no. ").lower()
#
#     if count1 == 'no':
#         condition1 = False


# ____USING RECURSION___
def calculator():

    num1 = float(input("What's the first number?: "))

    condition2 = True

    for key in operations:
        print(key)

    while condition2:

        choice = input("Choose an operation from above: ")

        num2 = float(input("What's the next number?: "))

        ans = operations[choice](num1, num2)

        print(f"{num1} {choice} {num2} = {ans}")

        cont = input(f"Type 'yes' to continue with {ans} or 'no' to stop the current calculation ").lower()

        if cont == 'yes':
            num1 = ans
        else:
            condition2 = False
            choice1 = input("Do you want to start a new calculation? Type yes or no. ").lower()
            if choice1 == 'yes':
                calculator()
            else:
                print('Thank you for using our calculator. ')


print(calc_logo)
calculator()