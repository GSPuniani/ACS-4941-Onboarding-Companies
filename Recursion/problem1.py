"""
Problem:
Given a sorted array of strings, write a recursive function 
to find the index of the first and last occurrence of a target string. 
If the target string is not found in the array, report that.
"""

def binary_search_range(strings, target, left=0, right=0):
    # Declare left and right pointers
    if right == 0:
        right = len(strings) - 1
    # Declare list to hold index range of target
    target_range = []
        
    mid = int((right + left) // 2)
    
    if strings[mid] == target:
        target_range.append(mid)
        # Check the right and left of the target at mid
        other_mid = mid
        while mid in range(len(strings)):
            if strings[mid + 1] == target:
                target_range.append(mid + 1)
                mid += 1
            else:
                break
        while other_mid in range(len(strings)):
            if strings[other_mid - 1] == target:
                target_range.append(other_mid - 1)
                other_mid -= 1
            else:
                break
        # Reshape target_from list of indices to actual range
        target_range = [min(target_range), max(target_range)]
        return target_range
    # Use recursive calls
    elif strings[mid] < target:
        binary_search_range(strings, target, mid + 1, right)
    else:
        binary_search_range(strings, target, left, mid - 1)
            
    # If target not found, return -1
    return -1

# Output: [7, 10]
print(binary_search_range(["Adriana", "Adriana", "Alan", "Alan", "Alan", "Alan", "Alan", "Braus", "Braus", "Braus", "Braus", "Dan", "Dan", "Dan", "Dan", "Dan", "Dani", "Dani", "Jess", "Meredith", "Milad", "Milad", "Mitchell", "Mitchell", "Mitchell", "Mitchell"], "Braus"))