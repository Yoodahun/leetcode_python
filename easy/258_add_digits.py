class Solution:
    def addDigits(self, num: int) -> int:
        digit = 0

        while num > 0:
            # 몫은 더하고, 나머지만 다시 취함
            digit += num%10
            num = num // 10

            if num == 0 and digit > 9: #자리가 두자리 수 이상이라면
                num = digit ##다시 계산대상값으로 이동시켜주고
                digit = 0 #바구니를 비워

        return digit


