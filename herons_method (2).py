#!/usr/bin/env python3
# herons_method.py

import random


def heron(s):
    x = s / 2
    # TODO: Implement your code here
    epsilon = 1e-8
    while x**2 - s > epsilon:
        x = (s / x + x) / 2
    return x


def main():
    s = random.randint(int(1e6), int(2e6))
    r = round(heron(s), 8)
    print(f"The square root of {s:,} is {r:,}")


if __name__ == "__main__":
    main()
