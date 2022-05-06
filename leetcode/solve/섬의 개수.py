class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [row for row in grid]
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j] == "0":
                    continue
                
                answer += 1
                queue = deque([(i, j)])
                visited[i][j] = "0"
                while queue:
                    x, y = queue.popleft()
                    
                    for k in range(4):
                        nx, ny = x+dx[k], y+dy[k]
                        
                        if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and visited[nx][ny] == "1":
                            visited[nx][ny] = "0"
                            queue.append((nx, ny))
                
        return answer
                            
        
