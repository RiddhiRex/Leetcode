class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans = []
        products = sorted(products)
        for idx, l in enumerate(searchWord):
            i=0
            suggested_wrds = []
            while(i<len(products) and len(suggested_wrds)<3):
                if products[i].startswith(searchWord[0:idx+1]):
                    suggested_wrds.append(products[i])
                i+=1
            ans.append(suggested_wrds)
        return ans
        
