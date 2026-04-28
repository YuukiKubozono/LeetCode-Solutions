class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        d = []
        
        for i in range(len(s)):
            if s[i] == "[":
               d.append(s[i])
            elif s[i] == "{":
                d.append(s[i])
            elif s[i] == "(":
                d.append(s[i])

            elif s[i] == "]":
                if d and d[-1] == "[":
                    d.pop(-1)
                else:
                    return False
            elif s[i] == "}":
                if d and d[-1] == "{":
                    d.pop(-1)
                else:
                    return False
            elif s[i] == ")":
                if d and d[-1] == "(":
                    d.pop(-1)
                else:
                    return False
        return len(d) == 0
