from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

    
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        leftPrev, cur = dummy, head
        for i in range(left-1):
            leftPrev, cur = cur, cur.next

        prev = None
        for i in range(right-left+1):
            tmpNext = cur.next
            cur.next = prev
            prev, cur = cur, tmpNext

        leftPrev.next.next = cur #cur will not be the one right after the right pointer
        leftPrev.next = prev #prev is now at the right node
        return dummy.next