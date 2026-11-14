class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}
        sub = strs.copy()
        for i in range(len(sub)):
            sub[i] = "".join(sorted(sub[i]))
        
        for i, x in enumerate(sub):
            if x not in groups:
                groups[x] = [strs[i]]
            else:
                groups[x].append(strs[i])
        
        ans = list(groups.values())
        return ans