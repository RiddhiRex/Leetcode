class ListNode(object):
    def __init__(self, val):
        self.val=val
        self.next =None

class MyLinkedList(object):

    def __init__(self):
        self.head = None

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        curr = self.head
        idx=0
        while(curr and idx<index):
            print(curr.val, idx)
            curr = curr.next
            idx+=1
        if(curr!=None):
            return curr.val
        else:
            return -1
        

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        newHead = ListNode(val)
        newHead.next = self.head
        self.head = newHead
        print("prnting headdd", self.head.val)


    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.head==None:
            self.head = ListNode(val)
            return
        curr = self.head
        while(curr.next!=None):
            curr=curr.next
        curr.next = ListNode(val)
        return
        

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index==0:
            self.addAtHead(val)
            return
        curr = self.head
        idx=0
        while(curr and idx<index-1):
            curr = curr.next    
            idx+=1
        if(curr):
            newNode = ListNode(val)
            newNode.next = curr.next
            curr.next = newNode
        

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index==0:
            self.head=self.head.next
            return
        curr = self.head
        idx=0
        while(curr and idx<index-1):
            curr = curr.next    
            idx+=1
        if(curr!=None and curr.next!=None):
            curr.next =curr.next.next
            
        return


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
