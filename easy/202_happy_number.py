
#TODO : 아직못풀었음...
class Solution:
    def isHappy(self, n: int) -> bool:
        number_list = list(map(int, str(n)))

        if len(number_list) == 1: return False

        result = 0

        while result != 1:
            result = 0
            for i in range(len(number_list)):
                result += pow(number_list[i], 2)

            if result == 1:
                return True

            number_list = list(map(int, str(result)))



happy = Solution()

happy.isHappy(19)