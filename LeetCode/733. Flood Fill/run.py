class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        target=image[sr][sc]
        # print(target)
        if target==color:
            return image
        def neighbor(x,y,conti):
            # print (x,y,conti)
            if not conti:return False
            if x<0 or x>=len(image): return False
            if y<0 or y>=len(image[0]): return False
            # print (x,y,image[x][y],target,conti and image[x][y]==target)
            if image[x][y]==target:
                conti=conti and image[x][y]==target
                image[x][y]=color
                neighbor(x-1,y,conti)
                neighbor(x,y-1,conti)
                neighbor(x+1,y,conti)
                neighbor(x,y+1,conti)
            else:return neighbor(0,0,False)
            
        change=neighbor(sr,sc,True)
        return image


       