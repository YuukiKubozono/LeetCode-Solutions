class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        ans = []
        for cur in path:
            if cur == "" or cur == ".":
                continue
            elif cur == "..":
                if ans:
                    ans.pop()
            else:
                ans.append(cur)
        return "/" + "/".join(ans)