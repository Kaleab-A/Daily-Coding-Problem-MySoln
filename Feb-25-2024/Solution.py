# Recurive Idea


# So decode("2345") can be treated as "b" + decode("345") or "w" + decode("45")
# Also need to check that 23 is less that 26.
# Letter are from 1 to 26, so no need to consider treating 3 digit number as one letter.
# decode("2345") = (1 + decode("345")) + (1 + decode("45"))
# Time complexity: O(2^n) where n is len of string
def decode(string):
    if len(string) == 0:
        return 1

    option1 = decode(string[1:])  # Treating the first number as a letter

    option2 = 0
    if (
        len(string) > 1 and int(string[:2]) <= 26
    ):  # Checking if we can consider the 2 digits as a letter
        option2 = decode(string[2:])

    return option1 + option2


# The above code will call the decode on the same arguement multiple time so we can create
# a map to apply memoize the values
# Updated Time Complexity will be O(n) where n is length of string

knownValue = {}


def decode2(string):
    if len(string) == 0:
        return 1
    if knownValue.get(string) != None:
        return knownValue[string]

    option1 = decode2(string[1:])  # Treating the first number as a letter

    option2 = 0
    if (
        len(string) > 1 and int(string[:2]) <= 26
    ):  # Checking if we can consider the 2 digits as a letter
        option2 = decode2(string[2:])

    knownValue[string] = option1 + option2
    return knownValue[string]


# Testing
print(decode2("111"))  # 3 because 'aaa', 'ka', and 'ak'

# Runs faster no decode2() than decode()
print(decode2("1111111111111111111111111111111"))
