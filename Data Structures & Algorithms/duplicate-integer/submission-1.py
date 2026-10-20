class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # n = len(nums)
        # if n==0:
        #     return False
        # mp = set()
        # for i in range(0,n,1):
        #     if nums[i] in mp:
        #         return True
        #     mp.add(nums[i])
        # return False

        return len(set(nums)) != len(nums)