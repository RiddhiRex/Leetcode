class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dict = {
                2: "abc",
               3: "def",
               4: "ghi",
               5: "jkl",
               6: "mno",
               7: "pqrs",
               8: "tuv",
               9: "wxyz"}
        no = str(digits)
        ans = []
        print(len(no))
        for i in range(len(no)):
            n =dict[int(no[i])]
            li = []
            for j in range(len(n)):
                li.append(n[j])
            print(li)
            if(len(ans)==0):
                ans = li
            else:
                ans = [x + y for x in ans for y in li]

        return ans
