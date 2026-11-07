# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0,head) # val =0, next ptr set to head
        left = dummy
        right = head

        while n > 0 and right: #and right not null
            right = right.next
            n -= 1 #when n=0 we shifted as much as wanted

        while right: #until right reaches end of list
            left = left.next
            right = right.next

        #delete
        left.next = left.next.next
        #l
        # 1 -> 2 -> 3 |  1 -> 3

        return dummy.next

        