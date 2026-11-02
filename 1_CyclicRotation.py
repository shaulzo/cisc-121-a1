# Problem 1: CyclicRotation
# Rotate an array A to the right K times. Each rotation moves the last element to the front.

def solution(A, K):
    n = len(A)

    # An empty array has nothing to rotate
    if n == 0:
        return A

    # Rotating n times returns the original array, so only K mod n matters
    k = K % n

    # The last k elements move to the front, the rest shift right
    return A[n - k:] + A[:n - k]
