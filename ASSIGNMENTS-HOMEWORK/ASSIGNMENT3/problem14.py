def find_duplicate(nums):
    slow = nums[0]
    fast = nums[0]
    
    # Detect cycle
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    slow = nums[0]
    
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow


# Example
nums = [1, 3, 4, 2, 2]
print(find_duplicate(nums))
