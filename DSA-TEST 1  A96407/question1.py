lst = [14, 8, -23, 4, 6, 10, -18, 5, 5, 11]
maxSum =lst[0]
sumz = 0

for i in range(0, len(lst)):
    sumz += lst[i]

    if sumz < 0:
        sumz = 0
    elif maxSum < sumz:
        maxSum = sumz

print("Maximum Sub array sum =",maxSum)        