# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0 
        ptr1 = head

        while ptr1: # count nodes
            count += 1
            if ptr1.next == None:
                break
            ptr1 = ptr1.next

        node_n = count - n - 1
        if node_n == -1:
            return head.next
            
        ptr2 = head
        for i in range(node_n): 
            ptr2 = ptr2.next

        ptr2.next = ptr2.next.next

        return head

            

        
