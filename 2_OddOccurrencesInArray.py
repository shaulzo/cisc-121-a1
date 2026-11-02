# Problem 2: OddOccurrencesInArray
# Array A has an odd number of elements. Every value can be paired with another element of the same value except one. Return the unpaired value.

def solution(A):
    result = 0

    # XOR of a number with itself is 0, and XOR with 0 is the number.
    # Paired values cancel out, leaving only the unpaired value.
    for value in A:
        result ^= value

    return result
