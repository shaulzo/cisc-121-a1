# Problem 3: FrogJmp
# A frog starts at position X and wants to reach a position greater than or equal to Y. Each jump covers a fixed distance D. Return the minimum number of jumps.

def solution(X, Y, D):
    distance = Y - X

    # Ceiling division without floats: (a + b - 1) // b
    # This rounds up so the frog reaches or passes Y.
    return (distance + D - 1) // D
