# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev, curr = None, head


        while curr: #while curr not null
            nxt = curr.next #save the forward link to slide forward
            curr.next = prev # point backwards
            prev = curr # move prev forward
            curr = nxt #curr moves forward
        return prev