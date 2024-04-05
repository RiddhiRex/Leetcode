class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wrdset = set(wordDict)

        def checkwrd(s):
            if s in wrdset:
                return True
            for i in range(len(s)):
                if s[0:i] in wrdset and checkwrd(s[i:]) == True:
                    return True
            return False
        
        return checkwrd(s)
