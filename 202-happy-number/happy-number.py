class Solution:
    def isHappy(self, n: int) -> bool:
        d = set()
        total = n
        
        while total != 1:
            currect_sum = 0
            for x in str(total):
                digit = int(x)
                currect_sum += digit**2

            total = currect_sum

            if total in d:
                return False
            else:
             d.add(total)  
        return True