def dfs(board,ncol,nrow,word,pos,i,j):
    if pos==len(word)-1: return True
    char=board[i][j]
    board[i][j]="*"
    next_char=word[pos+1]

    if j+1<ncol and board[i][j+1]==next_char:
        if dfs(board,ncol,nrow,word,pos+1,i,j+1):
            return True
    if i+1<nrow and board[i+1][j]==next_char:
        if dfs(board,ncol,nrow,word,pos+1,i+1,j):
            return True
    if i-1>-1 and board[i-1][j]==next_char:
        if dfs(board,ncol,nrow,word,pos+1,i-1,j):
            return True
    if j-1>-1 and board[i][j-1]==next_char:
        if dfs(board,ncol,nrow,word,pos+1,i,j-1):
            return True
    board[i][j]=char
    return False

def exist(board,word):
    nrow=len(board)
    ncol=len(board[0])

    for i in range(nrow):
        for j in range(ncol):
            if board[i][j]==word[0]:
                if dfs(board,ncol,nrow,word,0,i,j):
                    return True
    return False

print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE"))



