from typing import List,Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        hmp = set(nums)

        while head.val in hmp:
            head = head.next

        curr = head
        prev = head
        while curr.next:
            if curr.val in hmp:
                prev.next = curr.next
                curr = curr.next
                continue
            prev = curr
            curr = curr.next
        
        if curr.val in hmp:
            prev.next = None
        return head