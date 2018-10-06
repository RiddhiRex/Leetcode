class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit() is True:
            return [int(input)]
        ans = []
        for i, no in enumerate(input):
            if input[i] in ['+', '-', '*']:
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for l in left:
                    for r in right:
                        ans.append(eval(str(l)+no+str(r)))
        return ans
