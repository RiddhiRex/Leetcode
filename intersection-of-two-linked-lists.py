# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA==None or headB==None:
            return None
        currA=headA
        currB=headB
        cntA=0
        cntB=0
        while(currA!=None):
            cntA+=1
            currA=currA.next
        while(currB!=None):
            cntB+=1
            currB=currB.next  
        
        difcnt=abs(cntA-cntB)
        if(cntA>cntB):
            while(difcnt>0):
                headA=headA.next
                difcnt-=1
        elif(cntB>cntA):
            while(difcnt>0):
                headB=headB.next
                difcnt-=1        
        currA=headA
        currB=headB
        intersect=None
        while(currA!=None and currB!=None):
            if currA==currB:
                if intersect==None:
                    intersect = currA
            else:
                intersect=None
            currA=currA.next
            currB=currB.next
        return intersect
        
        
