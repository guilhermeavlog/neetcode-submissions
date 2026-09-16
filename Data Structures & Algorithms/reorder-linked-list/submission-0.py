class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find middle with slow/fast pointers
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        curr, prev = slow.next, None
        slow.next = None  # Split: slow is end of first half
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Merge
        left, right = head, prev
        while left and right:
            tmp1 = left.next
            tmp2 = right.next
            left.next = right
            right.next = tmp1
            left = tmp1
            right = tmp2