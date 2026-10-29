class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmaps = {}
        hashmapt = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in hashmaps:
                hashmaps[s[i]] = 1
            else:
                hashmaps[s[i]] += 1
            if t[i] not in hashmapt:
                hashmapt[t[i]] = 1
            else:
                hashmapt[t[i]] += 1
        if hashmapt != hashmaps:
            return False
        return True