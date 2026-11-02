# Problem 5: TapeEquilibrium
# Split a non-empty array A at a point P (0 < P < N) into a left part and a right part. Return the minimum possible absolute difference between the sum of the left part and the sum of the right part.

def solution(A):
    total = sum(A)

    left_sum = 0
    min_diff = float("inf")

    # Try every split point. P must leave at least one element on each side,
    # so we stop before the last element.
    for i in range(len(A) - 1):
        left_sum += A[i]               # left part now ends at index i
        right_sum = total - left_sum   # everything else is on the right
        diff = abs(left_sum - right_sum)

        # Keep the smallest difference seen so far
        if diff < min_diff:
            min_diff = diff

    return min_diff
