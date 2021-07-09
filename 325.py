def solution(nums, k):
    if not nums or len(nums) == 0:
        return 0
    max_l, sum_ = 0, 0
    # start, end = 0, 0
    dic=  {0:-1}
    for i in range(len(nums)):
        sum_ += nums[i]
        if sum_-k in dic:
            max_l = max(max_l, i - dic[sum_-k])
            # if i - dic[sum_-k] > max_l:
            #     start, end = dic[sum_-k] + 1, i
        if sum_ not in dic:
            dic[sum_] = i
    return max_l
