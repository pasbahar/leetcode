def solve(board):
    """
    Do not return anything, modify board in-place instead.
    """
    def dfs(mat, i,j):
        if i<0 or i>=len(mat) or j<0 or j>=len(mat[0]) or mat[i][j]=="X" or mat[i][j]=="_":
            return # return if reached the boundary or is X or already visited
        mat[i][j]='_'
        dfs(mat,i-1,j)
        dfs(mat,i+1,j)
        dfs(mat,i,j+1)
        dfs(mat,i,j-1)
    
    for i in range(len(board)):
        dfs(board,i,0)
    for i in range(len(board)):
        dfs(board,i,len(board[0])-1)
    for j in range(len(board[0])):
        dfs(board,0,j)
    for j in range(len(board[0])):
        dfs(board,len(board)-1,j)
        
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]=="O":
                board[i][j]="X"
            if board[i][j]=="_":
                board[i][j]="O"
arr=[["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]
solve(arr)
print(arr)