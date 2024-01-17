class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        left = nums[:len(nums)//2]
        right = nums[len(nums)//2:]
        removals = 0

        while left and right:
            if left[-1] == right[-1]:
                left.pop()
                right.pop()
            elif left[-1] < right[-1]:
                left.pop()
                right.pop()
                removals += 2

        return len(nums) - removals