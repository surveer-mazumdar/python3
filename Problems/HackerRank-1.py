#https://www.hackerrank.com/challenges/compare-the-triplets/problem


# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alen = bob = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            alen += 1
        elif a[i] < b[i]:
            bob += 1
    return [alen, bob]


a = list(map(int, input().rstrip().split()))

b = list(map(int, input().rstrip().split()))

result = compareTriplets(a, b)

print(' '.join(map(str, result)))

