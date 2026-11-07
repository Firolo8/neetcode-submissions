# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # output = []
        # count1 = 0
        # count2 = 0 

        # while list1 and list2:
        #     if list1[count1] < list2[count2]:
        #         output[count1] = list1[count1]
        #         count1 += 1
        #     else:
        #         output[count2] = list2[count2]
        #         count2 += 1
            
        # return output

        dummy = ListNode() # no edge case of inserting in empty list
        tail = dummy
        
        #if both not empty
        while list1 and list2:
            if list1.val < list2.val: 
                tail.next = list1 #take l1 val and put it in tail
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next #update regardless
        # what if 1 is empy but other isn't...
        #find non-empty and insert at end of list
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next
            
