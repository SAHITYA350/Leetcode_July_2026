class Solution:
    def pathExistenceQueries(self, n: int, nums: list[int], maxDiff: int, queries: list[list[int]]) -> list[int]:
        order = sorted(range(n), key=lambda i: nums[i])
        pos = [0] * n
        for i, o in enumerate(order):
            pos[o] = i
        val = [nums[o] for o in order]

        # reach[i]: farthest j with val[j]-val[i] <= maxDiff
        reach = [0] * n
        j = 0
        for i in range(n):
            if j < i:
                j = i
            while j + 1 < n and val[j + 1] - val[i] <= maxDiff:
                j += 1
            reach[i] = j

        # component ids
        comp = [0] * n
        for i in range(1, n):
            comp[i] = comp[i - 1] + (1 if val[i] - val[i - 1] > maxDiff else 0)

        # binary lifting
        LOG = max(1, n.bit_length())
        jump = [reach[:]]
        for k in range(1, LOG):
            prev = jump[-1]
            jump.append([prev[prev[i]] for i in range(n)])

        ans = []
        for u, v in queries:
            pu, pv = pos[u], pos[v]
            if comp[pu] != comp[pv]:
                ans.append(-1)
                continue
            if pu == pv:
                ans.append(0)
                continue
            if pu > pv:
                pu, pv = pv, pu
            dist = 0
            cur = pu
            for k in range(LOG - 1, -1, -1):
                if jump[k][cur] < pv:
                    cur = jump[k][cur]
                    dist += 1 << k
            if cur < pv:
                dist += 1
            ans.append(dist)
        return ans