class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            return self.is_integer(int(str(x)[::-1]))
        else:
            temp = str(x)
            temp = temp[1::]
            temp = temp[::-1]
            return self.is_integer(-1 * int(temp))

    def is_integer(self, test):
        if abs(test) > 2**32 or abs(test) >= 2147483651:
            return 0
        else:
            return test


if __name__ == '__main__':
    a = 1534236469
    print(Solution().reverse(a))
