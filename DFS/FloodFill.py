class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        col = image[sr][sc]
        image_res = self.dfs(image, sr, sc, newColor, col)
        return image_res
        
        
    def dfs(self, image, sr, sc, newColor, col):
        m = len(image)
        n = len(image[0])
        if sr >= m or sc >= n or image[sr][sc] == newColor or sr < 0 or sc < 0:
            return image
            
        if col == image[sr][sc]:
            image[sr][sc] = newColor                
            self.dfs(image, sr+1, sc, newColor, col)
            self.dfs(image, sr-1, sc, newColor, col)
            self.dfs(image, sr, sc+1, newColor, col)
            self.dfs(image, sr, sc-1, newColor, col)
            
        return image
