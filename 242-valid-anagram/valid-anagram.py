class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        ds={}
        dt={}
        for i in range(len(s)):
            if s[i] in ds:
                ds[s[i]]+=1
            elif not s[i] in ds:
                ds[s[i]]=1

        for i in range(len(t)):            
            if t[i] in dt:
                dt[t[i]]+=1            
            elif not t[i] in dt:
                dt[t[i]]=1  

        if ds==dt:
            return True
        else:
            return False

