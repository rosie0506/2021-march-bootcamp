# Assignment 1
# This assignment is for exercising Python fundamental I and getting familiar with Python syntax.

# 注意 - Copy this file and rename as assignment1-{first_name}.py then complete code with a PR.
# 注意 - Copy this file and rename as assignment1-{first_name}.py then complete code with a PR.
# 注意 - Copy this file and rename as assignment1-{first_name}.py then complete code with a PR.

# Q1. Write a program which can compute the factorial of a given numbers.

def factorial(x: int) -> int:
    fac = 1
    for i in range(1,x+1):
       fac *= i
    return fac


# Q2. Write a program which take a num and print a str as the sum of all numbers from 1 to this number
# [1 + 2 + ... + x] and x is always >= 1.

def print_sum(x: int) -> str:
    sum = 0
    for i in range(1, x+1):
        sum += i
    return str(sum)


# Q3. Write a program to check is a year is leap year (x is always > 0)

def is_leap_year(year: int) -> bool:
    if year % 400 ==0 or (year % 4 ==0 and year % 100 !=0):
        return True
    else:
        return False


# Q4. Write a program to convert a list of lowercase words to uppercase words.

def to_upper_case(words: [str]) -> [str]:
    WORDS=[]
    for c in words:
        WORDS.append(c.upper())
    return WORDS


# Q5. Write a program to use only 'and' and 'or' to implement 'xor'
# https://baike.baidu.com/item/%E5%BC%82%E6%88%96/10993677?fromtitle=xor&fromid=64178

def xor(a: bool, b: bool) -> bool:
    if a and b:
        return False
    elif a or b:
        return True
    else:
        return False
