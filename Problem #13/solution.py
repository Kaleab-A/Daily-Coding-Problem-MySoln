# Assuming s is all lowercase and k > 0
def longestSubstring(s, k):
    # Two pointer
    i = 0
    j = 0
    maxx = 0
    letterFreq = [0] * 26
    uniqueLetter = 0

    while j < len(s) and i < len(s):
        if uniqueLetter < k or (uniqueLetter == k and letterFreq[letterIdx(s[j])] != 0):
            letterFreq[letterIdx(s[j])] += 1
            if letterFreq[letterIdx(s[j])] == 1:
                uniqueLetter += 1
            j += 1
        else:
            letterFreq[letterIdx(s[i])] -= 1
            if letterFreq[letterIdx(s[i])] == 0:
                uniqueLetter -= 1
            i += 1

        maxx = max(maxx, j - i)

    return maxx


def letterIdx(ch):
    return ord(ch) - ord("a")


# Testing
print(longestSubstring("abcba", 2))  # 3
print(longestSubstring("aaabb", 2))  # 5
print(longestSubstring("ababbc", 2))  # 5

print(longestSubstring("aabcdbbdbcdacadcb", 3))  # 9
print(longestSubstring("aabcdbbdbcdacadcdac", 3))  # 10
