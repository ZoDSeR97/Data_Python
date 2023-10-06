# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
# The order of the elements may be changed. 
# Then return the number of elements in nums which are not equal to val.

# Constraints:
# 0 <= nums.length <= 100
# 0 <= nums[i] <= 50
# 0 <= val <= 100

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index
    
if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]
    expectedNums = [0,0,1,3,4]
    solution = Solution()
    k = solution.removeElement(nums, 2)
    print("Fail counting" if k != len(expectedNums) else "Pass counting")
    # No joke this is how they test array
    # Since most strong type programming languages cannot shrink array at will
    # Hence, they technically cannot do in-line, but they can swap
    k_sorted = sorted(nums[:k])
    nums = k_sorted+nums[k:]
    for i in range(k):
        if expectedNums[i] != nums[i]:
            print("Fail removal")
            break