class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=[]
        for x in s:
            if x.isalnum():
                t.append(x.lower())

        return t==t[::-1]