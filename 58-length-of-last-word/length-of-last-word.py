class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        candidate=0
        for i in range(len(s)-1,-1,-1):
            if s[i]==' ' and candidate==0:
                continue
            elif s[i]!=' ':
                candidate+=1
            elif s[i]==' ' and candidate!=0:
                break
        return candidate