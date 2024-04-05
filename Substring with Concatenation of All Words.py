class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        l =len(words[0])
        total_len = l*len(words)
        wrd_cnt = collections.Counter(words)
        print(wrd_cnt)
        ans = []
        for i in range(0, len(s)-total_len+1):
            substr = s[i:i+total_len]
            substr_wrds = []
            for j in range(0, len(substr), l):
                substr_wrds.append(substr[j:j+l])
            if collections.Counter(substr_wrds)==wrd_cnt:
                ans.append(i)
        return ans
