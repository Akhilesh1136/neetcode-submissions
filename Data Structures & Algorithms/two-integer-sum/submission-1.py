# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         n=len(nums)
#         i=0
#         j=n-1
#         while i<j:
#             if nums[i]+nums[j]>target: j=j-1
#             elif nums[i]+nums[j]<target: i=i+1
#             else: return[i,j]
#         return []

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(0,n-1,1):
            for j in range(i+1,n,1):
                if nums[i]+nums[j]==target: return [i,j]
        return []