#https://www.hackerrank.com/challenges/diagonal-difference/problem

# Complete the diagonalDifference function below.


def diagonalDifference(arr):
    ltrTotal = rtlTotal = 0
    ltrIndex = 0
    rtlIndex = len(arr) - 1

    for i in arr:
        ltrTotal += i[ltrIndex]
        rtlTotal += i[rtlIndex]
        ltrIndex += 1
        rtlIndex -= 1
    return abs(ltrTotal - rtlTotal)


n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)
print(result)