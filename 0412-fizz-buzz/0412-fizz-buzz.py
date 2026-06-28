class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []
        for i in range(0, n, 1):
            s = i + 1
            if s % 3 == 0 and s % 5 == 0:
                answer.append("FizzBuzz")
            elif s % 3 == 0:
                answer.append("Fizz")
            elif s % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(s)) # Converted to string to match standard FizzBuzz return type
        return answer