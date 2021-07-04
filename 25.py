class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        #实现一个group内的变换
        def reverse(head, k):
            #判断长度是否小于k，小于则不反转
            p = head
            for i in range(k):
                if(p):
                    p = p.next
                else:
                    return head

            pre, now = head, head.next
            pre.next = None
            i = 1
            while(now != None and i < k):
                nex = now.next
                now.next = pre
                pre, now = now, nex
                i += 1

            if(now != None):
                head.next = reverse(now, k)

            return pre

        if(head):
            return reverse(head, k)
        else:
            return None
