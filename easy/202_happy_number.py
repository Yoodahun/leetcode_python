
class Solution:
    def isHappy(self, n: int) -> bool:

       def get_next(n):
           total_sum = 0
           while n > 0:
               #n을 10으로 계속해서 나누어 각 자리수를 분리시켜나감. 나머지 수는 다시 나누어 나감
               n, digit = divmod(n, 10)
               total_sum += digit ** 2
           return total_sum

       seen = set()
       while n != 1 and n not in seen:
           seen.add(n)
           n = get_next(n)

       return n == 1