"""Problem 4:
Given two arrays a and b of numbers and a target value t, find a number from each array whose sum is closest to t.
Example: a=[9, 13, 1, 8, 12, 4, 0, 5],  b=[3, 17, 4, 14, 6],  t=20  ⇒  [13, 6] or [4, 17] or [5, 14]
"""

def find_closest_sum_pair(a, b, t):
    a_sorted = sorted(a)
    b_sorted = sorted(b)
    a_index = 0
    b_index = len(b_sorted) - 1
    closest_sum = None
    closest_sum_a = None
    closest_sum_b = None
    while a_index < len(a_sorted) and b_index >= 0:
        a_value = a_sorted[a_index]
        b_value = b_sorted[b_index]
        sum_value = a_value + b_value
        if closest_sum is None or abs(sum_value - t) < abs(closest_sum - t):
            closest_sum = sum_value
            closest_sum_a = a_value
            closest_sum_b = b_value
        if sum_value > t:
            b_index -= 1
        elif sum_value < t:
            a_index += 1
        else:
            return [a_value, b_value]
    return [closest_sum_a, closest_sum_b]

print(find_closest_sum_pair([9, 13, 1, 8, 12, 4, 0, 5], [3, 17, 4, 14, 6], 20))