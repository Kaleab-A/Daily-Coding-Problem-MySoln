def maxNonAdjSum(arr):
    length = len(arr)

    summs = [0, 0]

    for i in range(0, length):
        summs.append(max(summs[i + 1], summs[i] + arr[i]))

    return summs[-1]


# Test cases
print(maxNonAdjSum([3, 4, 1, 1]))  # 5
print(maxNonAdjSum([2, 4, 6, 2, 5]))  # 13
print(maxNonAdjSum([5, 1, 1, 5]))  # 10
