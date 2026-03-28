class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=[x.lower() for x in s if x.isalnum()]
        return t==t[::-1]