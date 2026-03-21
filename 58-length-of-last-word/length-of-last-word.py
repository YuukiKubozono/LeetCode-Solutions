class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        condidate=0
        for i in range(len(s)-1,-1,-1):
            if s[i]==' ' and condidate==0:
                continue
            elif s[i]!=' ':
                condidate+=1
            elif s[i]==' ' and condidate!=0:
                break
        return condidate