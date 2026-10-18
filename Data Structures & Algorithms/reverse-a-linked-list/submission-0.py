# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None :
            return None
        if head.next == None : 
            return head
        oldold = head
        old = head.next
        oldold.next = None
        cur = old.next
        old.next = oldold
        while cur != None :
            oldold = old
            old = cur
            cur = cur.next
            old.next = oldold
        return old
            
        