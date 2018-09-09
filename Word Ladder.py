class Solution(object):    
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        cur = [beginWord]
        visited = set([beginWord])
        lookup = set(wordList)
        dist=0
        while(cur):
            next_cur = []
            for word in cur:
                if word==endWord:
                    return dist+1
                for i in range(len(word)):
                    for j in "abcdefghijklmnopqrstuvwxyz":
                        w = word[:i]+j+word[i+1:]
                        if w not in visited and w in lookup:
                            next_cur.append(w)
                            visited.add(w)
            cur=next_cur
            dist+=1
        return 0
                
            

        
