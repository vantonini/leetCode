# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
    
        # find the middle node using fast and slow pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second half of the linked list
        prev = None
        curr = slow
        while curr:
            # temporary get the next value
            nxt = curr.next
            # invert the direction of the current next pointer
            curr.next = prev
            # the current node becomes the prev
            prev = curr
            # and the next node becomes de current
            curr = nxt
            # repeat until we reach the end of the linked list
        
        # compare the first and second halves of the linked list
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True