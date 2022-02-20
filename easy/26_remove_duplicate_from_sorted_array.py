from typing import List


## in-place, 즉 어떠한 추가적인 배열을 사용하지 않고 한번에 체크하면서 중복을 체크하고 자리를 바꾸어야함.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        number = 0

        # 전체 배열만큼 이동하는데, 1부터 시작하는 이유는 첫번째와 두번째 요소를 비교해보기 위함임.
        for i in range(1, len(nums)):
            # 만약, 요소가 같지않다면, 중복이 끝났다는 뜻이므로
            if nums[number] != nums[i]:
                # 고유한 요소의 개수를 증가시키고
                number += 1
                # 중복이 끝나기 전 자리에 새 요소를 집어넣음.
                nums[number] = nums[i]

        return number
