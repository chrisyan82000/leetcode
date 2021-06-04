

# def romanToInt(s):
#     dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     num = 0
#     for i in range(len(s)):
#         if i > 0 and dict[s[i]] > dict[s[i - 1]]:
#             num += dict[s[i]] - 2 * dict[s[i - 1]]
#         else:
#             num += dict[s[i]]
#     return num
