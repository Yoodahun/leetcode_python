# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head == None or head.next == None: return False

        root = ListNode(-1)
        root.next = head

        cursor = root
        val_list = []
        val_list.append(cursor)

        while cursor.next != None:
            if cursor.next in val_list:
                return True
            else:
                val_list.append(cursor.next)

            cursor = cursor.next
        return False



