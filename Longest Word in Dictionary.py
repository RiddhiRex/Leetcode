class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort()
        r = set([''])
        longestword = ""
        for word in words:
            if word[:-1] in r:
                r.add(word)
                if(len(word)>len(longestword)):
                    longestword = word
        return longestword
        
