class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        h_index = 0
        for i in range(len(citations)):
            if i + 1 <= citations[i]:
                h_index += 1
            else:
                break
        return h_index