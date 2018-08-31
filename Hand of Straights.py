class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        handd = {}
        for each in hand:
            if each not in handd:
                handd[each]=1
            else:
                handd[each]+=1
        hand=sorted(hand)
        while(len(hand)>0):
            no = hand[0]
            for i in range(W):
                if(no+i not in handd or handd[no+i]==0):
                    return False
                handd[no+i]-=1
                hand.remove(no+i)
        return True
                
            
