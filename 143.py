class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head):

        if not head: return

        ltmp = []
        cur = head

        while cur:  #  into a list
            ltmp.append(cur)
            cur = cur.next

        n = len(ltmp)  # 
        for i in range(n // 2):  # deal with
            ltmp[i].next = ltmp[n - 1 - i]
            ltmp[n - 1 - i].next = ltmp[i + 1]

        ltmp[n // 2].next = None  #  
