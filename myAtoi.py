class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        # conver the blank case
        if str == '' or str is None:
            return 0

        # find all the symbols in the function. (+, -, /, *)
        # stripping those creates the numbers
        # read string until I find a number
        # Once you hit a non numner add the converted string to array
        '''
            run through the array. if ther a is a symbol, preform the
            action on the left and right members of the  array.
            Slice the the first two elements of the array and set the third
            to the value.   
        '''
if __name__ == '__main__':
    print(Solution().myAtoi(''))
