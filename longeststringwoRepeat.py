class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        window = ''
        endpoint = 0
        longest = 0
        startpoint = 1

        # count the number of unique to get base endpoint
        # Move the slider over one to see if the the window endpoint increases
        # Make sure that the  slider never moves past len(s) + max size
        for i in range(len(s)):
            if s[i] not in window:
                window += s[i]
                if longest < len(window):
                    longest = len(window)
            else:
                window = window[window.index(s[i]) + 1:] + s[i]

            print(window)

        return longest

if __name__ == '__main__':
    test = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(test))
