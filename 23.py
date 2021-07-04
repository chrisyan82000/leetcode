 Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(-1)
        move = head
        while True:
            curHead = ListNode(float('inf'))
            curIndex = -1
            for i, llist in enumerate(lists):
                if llist and llist.val < curHead.val:
                    curHead = llist
                    curIndex = i
            if curHead.val == float('inf'):
                break
            curNext = curHead.next
            move.next = curHead
            curHead.next = None
            move = curHead
            curHead = curNext
            lists[curIndex] = curHead
        return head.next
