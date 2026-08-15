class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp1 = l1
        temp2 = l2
        dummyNode = ListNode(-1)
        curr = dummyNode
        carry = 0
        while temp1 is not None or temp2 is not None:
            sum = carry
            if temp1:
                sum += temp1.val
            if temp2:
                sum += temp2.val
            
            newNode = ListNode(sum % 10)
            carry = sum // 10

            curr.next = newNode
            curr = curr.next

            if temp1:
                temp1 = temp1.next
            if temp2:
                temp2 = temp2.next

        if carry:
            newNode = ListNode(carry)
            curr.next = newNode
        
        return dummyNode.next