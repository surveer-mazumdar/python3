#https://www.hackerrank.com/challenges/plus-minus/problem

def plusMinus(arr):
    positive = negative = zero = 0

    for num in arr:
        if num == 0:
            zero += 1
        elif num < 0:
            negative += 1
        elif num > 0:
            positive += 1
    arrLen = len(arr)
    positiveFrac = (positive / arrLen)
    negativeFrac = (negative / arrLen)
    zeroFrac = (zero / arrLen)

    print(positiveFrac)
    print(negativeFrac)
    print(zeroFrac)


n = int(input("Enter Count: "))

arr = list(map(int, input().rstrip().split()))

plusMinus(arr)