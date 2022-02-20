# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        cursor = head

        ## 두 리스트가 비어있다면, head의 next, 즉 설정되어있지 않은 null값을 리턴.
        if list1 == None and list2 == None:
            return head.next

        ## 둘 중 하나라도 비어있지 않으면 무조건 실행.
        while list1 != None and list2 != None:

            # 정렬된 두 리스트를 하나로 합치는 것이므로, list2의 값이 크다면, 작은값인 list1값을 현재 헤드의 다음값으로 넣어줌.
            if list1.val <= list2.val:
                cursor.next = list1
                # 리스트는 그 다음값으로 바꾸어서, 바뀌지 않은 리스트2의 값과 다시 비교할 준비를 함.
                list1 = list1.next
            else:
                cursor.next = list2
                list2 = list2.next

            # 들어간 위치에서 다시 준비
            cursor = cursor.next

        # 위에서도 다 돌고도 남은 노드가 있다면 그냥 넣어줌.
        if list1 != None:
            cursor.next = list1
        else:
            cursor.next = list2

        return head.next
