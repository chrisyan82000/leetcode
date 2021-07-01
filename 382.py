class Solution:
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self._len = 0
        self.head = head
        while head.next:
            head = head.next
            self._len += 1
    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        chose = random.randint(0,self._len)
        head = self.head
        while chose:
            head = head.next
            chose -= 1
        return head.val
