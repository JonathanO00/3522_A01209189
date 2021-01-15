import math

"""
Using functions to perform math.
"""


def CalculateHypotenuse(a, b):
    """
    Calculates hypotenuse of two inputs.
    :param a: Input 1
    :param b: Input 2
    :return: Hypotenuse
    """
    return math.sqrt(math.pow(float(a), 2) + math.pow(float(b), 2))


def main():
    """
    Main function.
    :return: None
    """
    print("Enter 2 values: ")
    a = input("Value 1: ")
    b = input("Value 2: ")
    print(CalculateHypotenuse(a, b))


if __name__ == "__main__":
    main()
