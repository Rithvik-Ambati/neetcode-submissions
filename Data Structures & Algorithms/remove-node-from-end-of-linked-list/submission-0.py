# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        current = head

        while current:
            count += 1
            current = current.next

        position = count - n + 1

        if position == 1:
            return head.next

        current = head

        for _ in range(position - 2):
            current = current.next

        current.next = current.next.next

        return head
        