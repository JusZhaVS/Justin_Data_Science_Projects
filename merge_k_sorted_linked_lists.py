# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import List, Optional

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        while len(lists) > 1:
            tempMergedLists = [] #temporary list variable to the merged lists, will reset to main lists variable at end of loop

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i + 1) < len(lists) else None
                tempMergedLists.append(self.mergeList(l1, l2))
            lists = tempMergedLists

        return lists[0] #there should be just one list in lists at this point

    def mergeList(self, l1, l2):
        dummy = ListNode()
        temp = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next

        while l1:
            temp.next = l1
            l1 = l1.next
            temp = temp.next

        while l2:
            temp.next = l2
            l2 = l2.next
            temp = temp.next

        return dummy.next