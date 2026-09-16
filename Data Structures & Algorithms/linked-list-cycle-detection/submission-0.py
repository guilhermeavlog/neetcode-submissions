# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ptr = head

        while ptr:
            if ptr.val == 10000:
                return True
            else:
                ptr.val = 10000
            ptr = ptr.next
        
        return False