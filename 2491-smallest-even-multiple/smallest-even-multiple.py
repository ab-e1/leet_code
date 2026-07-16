class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2 != 0:
            result = n*2
        else:
            result = n
        return result

        