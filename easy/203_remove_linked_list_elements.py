# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        # 입력값이 아예 빈 값일때는 빈값으로 리턴
        if head == None:
            return head

        root = ListNode(-1)
        root.next = head

        cursor = root

        #첫번째 입력값부터 확인해주게 됨.
        while cursor.next != None:
            #root node의 다음값, 즉 입력값의 첫번째val부터 중복값이라면,
            if cursor.next.val == val:
                #그 첫번째 node를, 첫번째 node의 다음값으로 대체
                cursor.next = cursor.next.next
            else:
                #그렇지 않다면, 즉 중복이 아니기 때문에 커서를 커서의 다음값으로 이동.
                cursor = cursor.next


        return root.next