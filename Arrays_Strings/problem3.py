"""Problem 3:
Given an array a of n numbers and a count k find the k largest values in the array a.
Example: a=[5, 1, 3, 6, 8, 2, 4, 7], k=3  ⇒  [6, 8, 7]
"""

def find_k_largest(a, k):
    k_largest_nums = []
    for _ in range(k):
        largest_value = max(a)
        k_largest_nums.append(largest_value)
        a.remove(largest_value)
    return k_largest_nums

print(find_k_largest([5, 1, 3, 6, 8, 2, 4, 7], 3))
