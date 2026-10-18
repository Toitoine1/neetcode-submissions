# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0 :
            return
        if len(lists) == 1 :
            return lists[0]
        a = self.mergeKLists(lists[:len(lists)//2])
        b = self.mergeKLists(lists[len(lists)//2:])
        if a == None :
            return b
        if b == None :
            return a
        if a.val < b.val :
            first = a
            a=a.next
        else :
            first = b
            b=b.next
        cur = first 
        while cur != None :
            if a == None :
                cur.next = b
                cur = None
            elif b == None :
                cur.next = a
                cur = None
            elif a.val < b.val :
                cur.next = a
                a=a.next
                cur=cur.next
            else :
                cur.next = b
                b=b.next
                cur=cur.next
        return first



