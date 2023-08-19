class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        length = len(piles)
        sec_round = h - length
        number = max(0, length - sec_round)

        l = sum(piles) // h
        if l < 1:
            return 1
        r = max(piles)
        m = (l + r) // 2
        eat = [i // m + 1 if i % m != 0 else int(i / m) for i in piles]
        m_total_days = sum(eat)
        # print (l,m,r, m_total_days)
        if l == r:
            return m
        while (l >= 0 and l < r and l != r and l != m and r != m):

            if m_total_days > h:
                l = m + 1
            elif m_total_days < h:
                r = m
            else:
                r = m
            m = (l + r) // 2
            # print (l,m,r)
            eat = [i // m + 1 if i % m != 0 else int(i / m) for i in piles]
            m_total_days = sum(eat)
        if m_total_days > h:
            return r
        else:
            return m
