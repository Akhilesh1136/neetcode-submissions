class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        mp = {}
        for i in range(0,n,1):
            if nums[i] in mp:
                mp[nums[i]] += 1
            else:
                mp[nums[i]] = 1
        sorted_items = sorted(mp.items(), key=lambda x: x[1], reverse=True)
        ans = []
        for i in range(0,k,1):
            ans.append(sorted_items[i][0])
        return ans