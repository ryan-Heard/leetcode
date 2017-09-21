

class ListNode(object):
    def __init__(self, x, next):
        self.val = x
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        a_list = []
        b_list = []
        carry = 0
        returnData = []

        while True:
            a_list.append(l1.val)

            if l1.next is None:
                break

            l1 = l1.next

        while True:
            b_list.append(l2.val)

            if l2.next is None:
                break

            l2 = l2.next

        list_dif = len(a_list) - len(b_list)

        if list_dif > 0:
            for i in range(list_dif):
                b_list.append(0)
        elif list_dif < 0:
            for i in range(abs(list_dif)):
                a_list.append(0)

        zippped = zip(a_list, b_list)

        for pair in zippped:

            temp = pair[0] + pair[1] + carry

            carry = 0

            if temp >= 10:
                carry = 1
                returnData.append(temp % 10)
            else:
                returnData.append(temp)

        if carry == 1:
            returnDataa.append(1)

        return returnData


if __name__ == '__main__':
    test1 = ListNode(0, None)
    a_node = ListNode(4, test1)  # rename to to test2
    # a_node = ListNode(2, test2)

    test1 = ListNode(4, None)
    test2 = ListNode(6, test1)
    b_node = ListNode(5, test2)

    here = Solution().addTwoNumbers(a_node, b_node)

    pp.pprint(here)
