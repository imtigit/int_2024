def half_pyramid(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("* ", end="")
        print()


# Example: Print a half pyramid with 5 rows
n = 5
half_pyramid(n)
N = 5
# Outer loop runs N times, once for each row
for i in range(1, N + 1):
    # Inner loop prints 'i - 1' spaces
    for j in range(1, i):
        print("  ", end="")
    # Inner loop prints '2 * (N - i) + 1' stars
    for j in range(1, 2 * (N - i) + 2):
        print("*", end="")
    # Move to the next line
    print()

