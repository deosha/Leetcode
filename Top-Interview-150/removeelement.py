from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j=0
        for num in nums:
            if num != val:
                nums[j] = num
                j += 1
        nums[:] = nums[:j]
        return(j)

#Driver code to test. Update nums and val to test for any list

nums = [3, 2, 2, 3]
val = 3
sol = Solution()
new_length = sol.removeElement(nums,val)
print(nums)
print(new_length)