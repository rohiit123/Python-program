"""
Write function that ask a number from user and prints if that number is odd or even
"""


def odd_even():
    num=int(input("Enter your number:"))
    if num % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")


odd_even()
odd_even()