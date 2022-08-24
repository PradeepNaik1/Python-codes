# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head
        
        pres = head
        
        while pres!= None and pres.next != None:
            if pres.val == pres.next.val:
                pres.next = pres.next.next
                continue
            pres = pres.next
                
        return head
