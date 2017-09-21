import pprint as pp


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        final = ""
        increment, step = 0, 0

        if numRows == 1:
            return s
        # Create the correct number of rows
        rows = ['' for x in range(numRows)]
        # Cycle through the string and add it to rows based on position
        for i in range(len(s)):
            if increment == 0:
                step = 1
            elif increment == numRows - 1:
                step = -1

            rows[increment] += s[i]
            increment += step

        return ''.join(rows)

if __name__ == '__main__':
    print(Solution().convert("ABC", 2))
