# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        l = 0
        r=len(lists)-1
        if(len(lists)==0 or (len(lists)==1 and lists[0] is None)):
            return []
        while(r>0):
            lists[l] = self.mergeTwoList(lists[l], lists[r])
            r=r-1
        return lists[0]
        
    def mergeTwoList(self, l1, l2):
        if l1 is None and l2 is None:
            return l1
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            dummy=ListNode(-1)
            curr=dummy
            cur1 = l1
            cur2= l2
            while(cur1 is not None and cur2 is not None):
                if cur1.val<=cur2.val:
                    curr.next = cur1
                    cur1=cur1.next
                else:
                    curr.next = cur2
                    cur2=cur2.next
                curr=curr.next
            if cur2 is not None:
                curr.next = cur2
            elif cur1 is not None:
                curr.next = cur1
        return dummy.next
            
            
            
