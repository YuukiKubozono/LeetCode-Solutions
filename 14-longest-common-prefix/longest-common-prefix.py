class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        candidate=strs[0]
        for x in strs:
            if x.startswith(candidate):
                continue
            while not x.startswith(candidate):
                candidate=candidate[:-1]
        return candidate

