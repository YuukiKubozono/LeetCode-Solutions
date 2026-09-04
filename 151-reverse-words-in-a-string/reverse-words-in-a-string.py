class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        start = 0
        end = 0
        i = 0

        while i < len(s):
            if s[i] != " ":
                start = end = i
                while i < len(s) and s[i] != " ":
                    end += 1
                    i = end
                ans.append(s[start:end])

            i += 1

        ans.reverse()

        return " ".join(ans)