# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        startIndex = (len(nums) - k) % len(nums)
        # print(id(nums)) 
        nums[:] = nums[startIndex:] + nums[0:startIndex]
        # print(id(nums))
    
if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3
    solution = Solution()
    solution.rotate(nums, k)
    print(nums)