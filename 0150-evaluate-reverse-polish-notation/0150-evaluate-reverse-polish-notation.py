class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        dummy = []
        prefix = 0
        suffix = 0
        for x in tokens:
            if x == "+":
                suffix = dummy[-1]
                dummy.pop()
                prefix = dummy[-1]
                dummy.pop()
                dummy.append(prefix + suffix)
            elif x == "-":
                suffix = dummy[-1]
                dummy.pop()
                prefix = dummy[-1]
                dummy.pop()
                dummy.append(prefix - suffix)
            elif x == "*":
                suffix = dummy[-1]
                dummy.pop()
                prefix = dummy[-1]
                dummy.pop()
                dummy.append(prefix * suffix)
            elif x == "/":
                suffix = dummy[-1]
                dummy.pop()
                prefix = dummy[-1]
                dummy.pop()
                dummy.append(int(prefix / suffix))
            else:
                dummy.append(int(x))
        return dummy[-1]