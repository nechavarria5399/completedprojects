#!/usr/bin/env python3
# factor_quadratic.py

J = 2
K = 14
L = 3

print("Given the quadratic:")
print(f" {J}x^2 + {K}x + {L} = 0")
print("The factors are:")

# TODO: Insert your code below
for a in range(1, J + 1):
    if J % a == 0:
        c = J // a
        for b in range(1, L + 1):
            if L % b == 0:
                d = L // b
                if a * d + b * c == K:
                    print(f" ({a}x + {b})"
                          f"({c}x + {d})")
