class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans=[]
        kb = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        for each in words:
            for i in kb:
                if set(each.lower()).issubset(set(i)):
                    ans.append(each)
        return ans
