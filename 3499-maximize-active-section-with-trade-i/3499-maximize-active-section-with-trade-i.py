class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        # counts of zeros in blocks
        zeros = map(len, filter(None, s.split("1")))

        # max zeros in two consecutive blocks
        maxzeros = max(map(sum, pairwise(zeros)), default=0)

        return s.count("1") + maxzeros