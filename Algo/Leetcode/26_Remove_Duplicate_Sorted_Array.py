# Given an integer array nums sorted in non-decreasing order
# Remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same. 
# Then return the number of unique elements in nums.

# Constraints:
# 1 <= nums.length <= 3 * 10^4 This only means we are guaranteed to have 1 unique
# -100 <= nums[i] <= 100

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        lastUnique = 1
        for i in range(len(nums)):
            if i != 0 and nums[i]!=nums[i-1]:
                nums[lastUnique] = nums[i]
                lastUnique+=1
        return lastUnique
        
if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    expectedNums = [0,1,2,3,4]
    solution = Solution()
    k = solution.removeDuplicates(nums)
    print("Fail counting" if k != len(expectedNums) else "Pass counting")
    # No joke this is how they test array
    # Since most strong type programming languages cannot shrink array at will
    # Hence, they technically cannot do in-line, but they can swap
    for i in range(k):
        if expectedNums[i] != nums[i]:
            print("Fail removal")
            break