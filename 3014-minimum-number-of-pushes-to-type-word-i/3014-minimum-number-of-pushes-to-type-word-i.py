class Solution:
    def minimumPushes(self, word: str) -> int:
        q, r = divmod(len(word), 8)
        return ((q << 2) + r) * (q + 1)