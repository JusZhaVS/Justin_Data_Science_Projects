# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        prev, cur = dummy, head
        while cur:
            temp = prev
            test = cur
            for _ in range(k-1): #test if fewer than k nodes left by looking at next k-1 nodes, if so, break
                test = test.next
                if not test:
                    #break THIS IS WRONG, will still go through for loop below
                    return dummy.next

            for _ in range(k): #reverse current group of k nodes
                tempNxt = cur.next
                cur.next = prev
                prev, cur = cur, tempNxt
            new_prev = temp.next
            temp.next.next = cur
            temp.next = prev
            
            prev = new_prev

        return dummy.next