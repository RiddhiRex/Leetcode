class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0  # Maximum index that can be reached
        last_index = len(nums) - 1
        
        # Iterate through the list
        for i in range(len(nums)):
            # Update the maximum index that can be reached
            max_reach = max(max_reach, i + nums[i])
            
            # If the maximum index that can be reached is beyond or at the last index,
            # then it's possible to reach the last index
            if max_reach >= last_index:
                return True
        
            # If the current index cannot be reached (i.e., it's a dead end)
            # and there is no way to continue further, return False
            if max_reach <= i:
                return False
        
        # If the loop completes without returning True, it means the last index cannot be reached
        return False
