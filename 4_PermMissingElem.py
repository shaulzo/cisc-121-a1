# Problem 4: PermMissingElem
# Array A contains N different integers from the range 1 to N + 1, so exactly one value is missing. Return the missing value.

def solution(A):
    n = len(A)

    # Sum of 1 to N + 1 using the arithmetic series formula
    expected_sum = (n + 1) * (n + 2) // 2

    # The difference between the two sums is the missing number
    actual_sum = sum(A)

    return expected_sum - actual_sum
