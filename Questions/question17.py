"""
Write a function fizzbuzz(n) that takes a single number and prints "fizz"
if it's divisible by 3, "buzz" if it's divisible by 5 "FizzBuzz",
if it's divisible by both , otherwise print the number itself.
"""


def fizzbuzz(num):
    if num % 3==0 and num%5==0:
        print("FizzBuzz")  
    elif num%3==0:
        print("Fizz")
    elif num % 5==0: 
        print("Buzz")    
    else:
        print("It is not divisiable by any ",num)

fizzbuzz(20)
fizzbuzz(9)
fizzbuzz(15)
fizzbuzz(7)               