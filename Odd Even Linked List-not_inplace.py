
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        oddhead = head
        newhead =oddhead
        
        evenhead = head.next
        newevenhead = head.next
        curr = head.next.next
        c = 3
        while(curr is not None):
            if(c%2==0):
                print(curr.val)
                evenhead.next = curr
                curr = curr.next
                
             
            else:
                print(curr.val)
                oddhead.next = curr
                curr = curr.next
                
            c=c+1
        evenhead.next = None
        oddhead.next = newevenhead
        
        return newhead


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e


s = Solution()
head = s.oddEvenList(a)

while head:
    print(head.val)
    head = head.next
