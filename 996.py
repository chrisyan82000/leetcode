import collections


class Solution():
    def numSquarefulPerms(self, A):
        count = collections.Counter(A)

        graph = {x: [] for x in count}
        for x in count:  # Find those numbers and x can form a square
            for y in count:
                if int((x+y)**.5 + 0.5) ** 2 == x+y:  # ,0.5 plus and without adding does not affect the result
                    graph[x].append(y)

        def dfs(x, todo):
            count[x] -= 1
            if todo == 0:
                ans = 1
            else:
                ans = 0
                for y in graph[x]:  # Select a number in turn for depth-first recursive judgment
                    if count[y]:
                        ans += dfs(y, todo - 1)
            count[x] += 1
            return ans

        return sum(dfs(x, len(A) - 1) for x in count)


if __name__ == '__main__':
    solu = Solution()
    print(solu.numSquarefulPerms([1, 17, 8]))
