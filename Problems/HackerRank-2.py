#https://www.hackerrank.com/challenges/a-very-big-sum/problem

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    total = 0
    for num in ar:
        total += num

    return total


ar_count = int(input("Enter Count: "))

ar = list(map(int, input().rstrip().split()))

result = aVeryBigSum(ar)

print(result)