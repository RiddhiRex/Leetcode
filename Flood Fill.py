class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(r, c,  clr, newColor):

            if self.image[r][c]==clr:
                self.image[r][c]=newColor
                if r>0:
                    dfs(r-1, c,  clr, newColor)
                if c>0:
                    dfs(r, c-1,  clr, newColor)
                if r+1<self.r:
                    dfs(r+1, c,  clr, newColor)
                if c+1<(self.c):
                    dfs(r, c+1,  clr, newColor)
            else:
                return     
            return

        self.image = image
        self.r = len(image)
        self.c = len(image[0])
        clr = image[sr][sc]
        if clr!=newColor:
            dfs(sr, sc, clr, newColor)
        return self.image
        
