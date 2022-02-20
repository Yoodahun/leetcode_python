from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums)==0: return 0

        count = 0


        for i in range(0, len(nums)):
            # 삭제해야하는 숫자와 같지 않다면, 새로운 요소가 나왔다는 것.
            if nums[i] != val:
                # 이제껏은 그럼 삭제해야할 숫자였다는 말이므로, 그 위로 덮어씌워줌.
                nums[count] = nums[i]
                count += 1

        return count
