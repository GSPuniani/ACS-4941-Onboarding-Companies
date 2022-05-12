"""
Problem:
Given an array of numbers sorted in ascending order, find the range of a given number 'key'. 
The range of the 'key' will be the first and last position of the 'key' in the array.
Write a function to return the range of the 'key'. If the 'key' is not present return [-1, -1].
"""

def binary_search_range(nums, key):
    # Declare left and right pointers
    left = 0
    right = len(nums) - 1
    # Declare list to hold index range of key
    key_range = []
    while(left <= right):
        mid = int((right + left) // 2)
        
        if nums[mid] ==  key:
            key_range.append(mid)
            # Check the right and left of the key at mid
            target = mid
            while mid in range(len(nums)):
                if nums[mid + 1] == key:
                    key_range.append(mid + 1)
                    mid += 1
                else:
                    break
            while target in range(len(nums)):
                if nums[target - 1] == key:
                    key_range.append(target - 1)
                    target -= 1
                else:
                    break
            # Reshape key_from list of indices to actual range
            key_range = [min(key_range), max(key_range)]
            return key_range
        elif nums[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
            
    # If key not found, return [-1, -1]
    return [-1, -1]        


print(binary_search_range([4, 6, 6, 6, 9], key = 6)) # Output: [1, 3]
print(binary_search_range([1, 3, 8, 10, 15], key = 10)) # Output: [3, 3]
print(binary_search_range([1, 3, 8, 10, 15], key = 12)) # Output: [-1, -1]
