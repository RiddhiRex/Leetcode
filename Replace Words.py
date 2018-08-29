class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        d = set(dict)
        w = sentence.split(" ")
        for j in range(len(w)):
            for i in range(1, len(w[j])):
                if w[j][:i] in d:
                    w[j]= w[j][:i]
        return " ".join(w)
