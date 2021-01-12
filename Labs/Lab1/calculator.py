import math

"""
Using functions and if statements to build a calculator.
"""


def CalculateHypotenuse(a, b):
    """
    Calculates hypotenuse of two inputs.
    :param a: Input 1
    :param b: Input 2
    :return: Hypotenuse
    """
    return math.sqrt(math.pow(float(a), 2) + math.pow(float(b), 2))


def Sum(a, b):
    """
    Calculates sum of two inputs.
    :param a: Input 1
    :param b: Input 2
    :return: Sum of inputs
    """
    return float(a) + float(b)


def Subtract(a, b):
    """
    Calculates difference of two inputs.
    :param a: Input 1
    :param b: Input 2
    :return: Difference of inputs
    """
    return float(a) - float(b)


def Multiply(a, b):
    """
    Returns product of two inputs.
    :param a: Input 1
    :param b: Input 2
    :return: Product of inputs
    """
    return float(a) * float(b)


def Divide(a, b):
    """
    Returns quotient of two inputs.
    :param a: Input 1
    :param b: Input 2
    :return: Quotient of inputs
    """
    return float(a) / float(b)


def main():
    """
    Main function
    :return: None
    """
    print("1 to calculate hypotenuse")
    print("2 to add")
    print("3 to subtract")
    print("4 to multiply")
    print("5 to divide")
    choice = input("Choose an operator: ")
    a = input("enter first number: ")
    b = input("enter second number: ")

    if int(choice) == 1:
        print(CalculateHypotenuse(a, b))
    elif int(choice) == 2:
        print(Sum(a, b))
    elif int(choice) == 3:
        print(Subtract(a, b))
    elif int(choice) == 4:
        print(Multiply(a, b))
    elif int(choice) == 5:
        print(Divide(a, b))


main()
