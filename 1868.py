class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        s1, s2 = len(encoded1), len(encoded2)

        # 将数组中长度坐标改为截止下标
        for i1 in range(1, s1):
            encoded1[i1][1] += encoded1[i1 - 1][1]
        for i2 in range(1, s2):
            encoded2[i2][1] += encoded2[i2 - 1][1]

        # print(encoded1)
        # print(encoded2)

        ans1 = []

        now = 0
        i1, i2 = 0, 0
        while i1 < s1 and i2 < s2:
            v = encoded1[i1][0] * encoded2[i2][0]
            if encoded1[i1][1] < encoded2[i2][1]:
                ans1.append([v, encoded1[i1][1] - now])
                now = encoded1[i1][1]
                i1 += 1
            elif encoded1[i1][1] > encoded2[i2][1]:
                ans1.append([v, encoded2[i2][1] - now])
                now = encoded2[i2][1]
                i2 += 1
            else:  # encoded1[i1][1] == encoded2[i2][1]
                ans1.append([v, encoded1[i1][1] - now])
                now = encoded1[i1][1]
                i1 += 1
                i2 += 1

        ans2 = []
        for v, l in ans1:
            if ans2 and v == ans2[-1][0]:
                ans2[-1][1] += l
            else:
                ans2.append([v, l])

        return ans2
