class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        streak = 0
        for i in range(len(nums)-k-1):
            if nums[i+1] > nums[i] and nums[i+k+1] > nums[i+k]:
                streak += 1
            else:
                streak = 0
            if streak == k-1:
                return True
        return False