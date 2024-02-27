# Idea
# sum([2, 4, 6, 2, 5]) = max(2 + sum([6, 2, 5])) + max(4 + sum([2, 5]))
# The above equation works if 2 and 4 are non-negative. If they are negative, then not picking sum
# better for the total sum.
# Time complexity: T(n) = 1 + T(n-2) + T(n-3) | O(2^n) # Some kind of exponential


def nonAdjSum(lst):
    if len(lst) == 0:
        return 0

    option1 = max(lst[0], 0) + nonAdjSum(lst[2:])  # Take the first digit if positive
    option2 = 0

    if len(lst) > 1:
        option2 = max(lst[1], 0) + nonAdjSum(
            lst[3:]
        )  # Taking the second digit if positive

    return max(option1, option2)


# Memoize to make it faster, I can just use the length of array as a key.
# Time: O(n)
# Space: O(n)


def nonAdjSumMemo(lst):  # To reset the known value everytime function called
    knownVal = {}

    def nonAdjSum2(lst):
        if len(lst) == 0:
            return 0
        if (knownVal.get(len(lst))) != None:
            return knownVal[len(lst)]

        option1 = max(lst[0], 0) + nonAdjSum2(
            lst[2:]
        )  # Take the first digit if positive
        option2 = 0

        if len(lst) > 1:
            option2 = max(lst[1], 0) + nonAdjSum2(
                lst[3:]
            )  # Taking the second digit if positive

        knownVal[len(lst)] = max(option1, option2)
        return knownVal[len(lst)]

    return nonAdjSum2(lst)


# Possible to improve the space complexity by only storing the last 3 values [n-1, n-2, n-3].
# Will get us O(1) space complexity

# Slower
print("Without memoization | O(2^n)")
print(nonAdjSum([2, 4, 6, 2, 5]))  # 13 taking [2, 6, 5]
print(nonAdjSum([5, 1, 1, 5]))  # 10 taking [5, 5]
print(nonAdjSum([5, 1, 1, 5] * 13))  # Time check

# Faster
print("\nWith memoization | O(n)")
print(nonAdjSumMemo([2, 4, 6, 2, 5]))  # 13 taking [2, 6, 5]
print(nonAdjSumMemo([5, 1, 1, 5]))  # 10 taking [5, 5]
print(nonAdjSumMemo([5, 1, 1, 5] * 13))  # Time check
