def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        if not restrictions:
            return n - 1
        ans = 0
        def leftward(prev, next):
            return [next[0], min(next[1], prev[1] + next[0] - prev[0])]
        def rightward(prev, next):
            nonlocal ans
            next = [next[0], min(next[1], prev[1] + prev[0] - next[0])]
            high, low = sorted([prev[1], next[1]])
            ans = max(ans, high + (prev[0] - next[0] - high + low) // 2)
            return next
        restrictions = list(accumulate(sorted(restrictions), leftward, initial=[1,0]))
        for _ in accumulate(restrictions[::-1], rightward, initial=[n + 1, n - restrictions[-1][0] + restrictions[-1][1]]):
            pass
        return ans 
                
