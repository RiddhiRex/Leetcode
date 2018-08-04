class Codec:
    def __init__(self):
        self.dic = {}
        self.i = 0
        self.url = "http://tinyurl.com/"
        
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        self.i=self.i+1
        self.dic[self.i]=longUrl
        shortUrl = self.url+str(self.i)

        return shortUrl
        
        

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        key = shortUrl.replace(self.url, "")
        return self.dic[int(key)]
        
        

# Your Codec object will be instantiated and called as such:
url = "https://leetcode.com/problems/design-tinyurl"
codec = Codec()
codec.decode(codec.encode(url))
