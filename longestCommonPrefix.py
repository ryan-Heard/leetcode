from collections import OrderedDict


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        Write a function to find the longest common prefix string
        amongst an array of strings.
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""
        # cycle through each array checking the letter
        # if one letter doesn't match then look isn't true

        # Zip to unpack all the letters at once
        # Enumerate allows you to find the i value
        for i, letter_group in enumerate(zip(*strs)):
            print(letter_group)
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)


if __name__ == '__main__':
    test = ['abc', 'abcd', 'abcde']
    print(Solution().longestCommonPrefix(test))
