class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        i = 0
        index = 0
        while i < len(s):
            if s[i] == " ":
                i += 1
            else:
                ans.append([])
                while i < len(s) and s[i] != " ":
                    ans[index].append(s[i])
                    i += 1
                index += 1
        ans.reverse()
        for j in range(len(ans)):
            ans[j] = "".join(ans[j])
        
        ans = " ".join(ans)
        return ans