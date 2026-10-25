class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp = 26*[0]
        n = len(s)
        m = len(t)
        if n != m: return False
        for i in range(0,n,1):
            temp[ord(s[i]) - ord('a')] += 1
            temp[ord(t[i]) - ord('a')] -= 1
        for i in range (0,26,1):
            if temp[i]!=0: return False
        return True