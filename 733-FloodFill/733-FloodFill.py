# Last updated: 6/6/2026, 10:25:23 PM
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        curr=image[sr][sc]
        if curr==color:
            return image

        row=len(image)
        col=len(image[0])
        q=deque()
        q.append((sr,sc))
        while q:
            i,j=q.popleft()

            if i<0 or j<0 or i>=row or j>=col:
                continue

            if image[i][j]!=curr:
                continue 

            image[i][j]=color

            q.append((i+1,j))
            q.append((i-1,j))
            q.append((i,j+1))
            q.append((i,j-1))
        return image
        
      

        