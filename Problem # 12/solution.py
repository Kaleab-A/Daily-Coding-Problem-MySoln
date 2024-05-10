# Condition: Can jump one or two stairs
def nWaysStairsEasy(n):
    # Base Cases: One way to get to no staircase. One way to get to first staircase
    ans = [1, 1]

    # To get to the nth staircase
    for i in range(n - 1):
        ans.append(ans[-1] + ans[-2])

    return ans[n]


# Testing
print(nWaysStairsEasy(2))  # 1
print(nWaysStairsEasy(4))  # 5


# --------------------------------------------------------------------------------
# Challenge: The frog can jump any number of stairs. It is given as {1, 3, 5}
def nWayStairs(n, steps):
    # Setting Base Cases
    ans = [1]  # One way to get no staircase

    for i in range(1, n + 1):
        nWays = 0
        for j in steps:
            if i - j >= 0:
                nWays += ans[i - j]
        ans.append(nWays)

    return ans[n]


# Testing
print("\nChallenge")
print(nWayStairs(4, [1, 2]))  # 5
print(nWayStairs(4, [1, 3, 5]))  # 3
