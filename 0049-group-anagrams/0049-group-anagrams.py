class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        ans = {}
        dummy = strs.copy()

        for i in range(len(dummy)):
            dummy[i] = "".join(sorted(dummy[i]))

        for i in range(len(dummy)):
            if dummy[i] in ans:
                ans[dummy[i]].append(strs[i])
            else:
                ans[dummy[i]] = [strs[i]]
        return list(ans.values())
        
