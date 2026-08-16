class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        ans = 0
        for i, c in enumerate(citations):
            if c < i + 1:
                return i
        return len(citations)