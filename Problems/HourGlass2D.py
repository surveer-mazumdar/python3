#https://www.hackerrank.com/challenges/2d-array/problem


def hourglassSum(arrVar):
    verMax = horMax = 4
    hourGlassArr = list()
    for i in range(verMax):
        for j in range(horMax):
            hourGlassArr.append(getHourGlass(i, j, arrVar))

    return max(hourGlassArr)

def getHourGlass(i, j, arr):
    return arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]

arr = []
for _ in range(6):
   arr.append(list(map(int, input().rstrip().split())))
result = hourglassSum(arr)