from collections import deque

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # every letter that appears gets a node
        adj = {c: set() for w in words for c in w}
        indegree = {c: 0 for c in adj}

        # compare each adjacent pair of words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            # invalid: longer word comes before its own prefix ("abc" before "ab")
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break    # only the first difference matters

        # Kahn's algorithm: start with letters nothing must come before
        q = deque(c for c in indegree if indegree[c] == 0)
        res = []

        while q:
            c = q.popleft()
            res.append(c)
            for nxt in adj[c]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        # if not all letters were placed, there's a cycle
        if len(res) < len(indegree):
            return ""
        return "".join(res)