"""
Problem:
Find the maximum value in a given Bitonic array. 
An array is considered bitonic if it is monotonically increasing and then monotonically decreasing. 
Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].
"""

def bitonic_max(nums):
    # Declare left and right pointers
    left = 0
    right = len(nums) - 1

    # Use similar logic as binary search
    while(left <= right):
        mid = int((right + left) // 2)
        
        # The max will be greater than both of its neighbors
        if nums[mid] >= nums[mid + 1] and nums[mid] >= nums[mid - 1]:
            return nums[mid]
        # Reassign left pointer if values are increasing
        elif nums[mid + 1] >= nums[mid]:
            left = mid + 1
        # Reassign right pointer if values are increasing
        else:
            right = mid - 1
                    


print(bitonic_max([1, 3, 8, 12, 4, 2])) # Output: 12
