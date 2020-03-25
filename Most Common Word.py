class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for i in '''!()-[]{};:'"\,<>./?@#$%^&*_~''':
            paragraph=paragraph.replace(i," ")
        wrds = paragraph.lower().split()
        ban = [b.lower() for b in set(banned)]

        print(ban)
        wrd_list = []
        for i in range(len(wrds)):
            if wrds[i] not in ban:
                wrd_list.append(wrds[i])
                
        cnt = collections.Counter(wrd_list)
        print(wrd_list, cnt)
        return sorted(cnt.items(), key=operator.itemgetter(1), reverse=True)[0][0]
            
        
