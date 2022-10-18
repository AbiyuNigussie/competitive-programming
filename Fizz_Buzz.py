from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [i for i in range(1, n+1)]
        for m in range(0, len(answer)):
          if answer[m] % 3 == 0 and answer[m] % 5 == 0:
            answer[m] = "FizzBuzz"
          elif answer[m] % 3 == 0:
            answer[m] = "Fizz"
          elif answer[m] % 5 == 0:
            answer[m] = "Buzz"
        answer = [str(i) for i in answer]
        return answer

obj = Solution()
print(obj.fizzBuzz(15))