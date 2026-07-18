class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a,2)
        b = int(b,2)
        c = a + b
        
        if c == 0:
            return str(0)

        k = []
        while c > 0:
            if c % 2 == 1:
                k.append(1)
            else:
                k.append(0)
            c = c // 2
        k.reverse()
        ans = ""
        for x in k:
            ans += str(x)
        return ans