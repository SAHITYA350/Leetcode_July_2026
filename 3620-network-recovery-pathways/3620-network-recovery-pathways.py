from collections import deque

class Solution:
    def check(self, x, adj, topo, k):

        n = len(adj)

        INF = 10 ** 18

        # dp[i] = minimum cost required to reach node i
        dp = [INF] * n
        dp[0] = 0

        # Process nodes in topological order
        for u in topo:

            # Skip unreachable nodes
            if dp[u] == INF:
                continue

            # Relax all outgoing edges
            for v, w in adj[u]:

                # Only consider edges having weight >= current threshold
                if w >= x:
                    dp[v] = min(dp[v], dp[u] + w)

        # Check whether destination can be reached within budget k
        return dp[n - 1] <= k

    def findMaxPathScore(self, edges, online, k):

        n = len(online)

        adj = [[] for _ in range(n)]
        indegree = [0] * n

        mx = 0

        # Build graph using only online nodes
        for u, v, w in edges:

            # Ignore edges connected to offline nodes
            if not online[u] or not online[v]:
                continue

            adj[u].append((v, w))
            indegree[v] += 1

            mx = max(mx, w)

        # Compute topological ordering (only once)
        topo = []
        q = deque()

        for i in range(n):
            if online[i] and indegree[i] == 0:
                q.append(i)

        while q:

            curr = q.popleft()
            topo.append(curr)

            for v, _ in adj[curr]:
                indegree[v] -= 1

                if indegree[v] == 0:
                    q.append(v)

        # Binary Search on the answer
        # We try to maximize the minimum edge weight.
        lo = 0
        hi = mx

        ans = -1

        while lo <= hi:

            mid = (lo + hi) // 2

            if self.check(mid, adj, topo, k):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans