"""This script contains solution for fizzbuzz problem from leetcode"""


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer_list = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                value = "FizzBuzz"
            elif i % 3 == 0:
                value = "Fizz"
            elif i % 5 == 0:
                value = "Buzz"
            else:
                value = str(i)
            answer_list.append(value)
        return answer_list
