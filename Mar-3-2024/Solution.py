# Idea is let have a circle with a radius of 1 unit center at (0, 0)
# And let have a square centered at (0, 0) with side length of 2.
# The area of circle is equal to pi(1^2) = pi.
# The area of the square is equal to 2^2 = 4.
# If generated random point within square (x: [-1, 1], y: [-1, 1]) the probability that it is
# in the circle is equal to the ratio of their areas, which is equal to pi/4.
# So the goal it to generate a lot of point and estimate pi from the equation
# (probabilty of being in square) * 4 = PI

from random import random


def estimatePI(samples=100000):
    inCircle = 0

    for i in range(samples):
        x = random() * 2 - 1  # From -1 to 1
        y = random() * 2 - 1

        # Within the circle?
        if (x**2 + y**2) <= 1:  # I am not sure about checking for equality here
            inCircle += 1

    return (inCircle / samples) * 4  # Based on the explaination above


print(estimatePI())
