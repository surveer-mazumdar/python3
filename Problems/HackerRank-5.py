#https://www.hackerrank.com/challenges/staircase/problem


def staircase(n):
    for i in range(1, n+1):
        spaces = n - i
        print(" " *spaces + "#" *i)


n = int(input("Enter a number: "))

staircase(n)