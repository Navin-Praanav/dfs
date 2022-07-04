def dfs_ouptut(matrix,start=0,visited=[]):
    output=[]
    def ret_dfs(matrix, start, visited):
            output.append(start)
            visited.append(start)
            for i in range(len(matrix)):
                if (matrix[start][i] == 1 and
                        (i not in visited)):
                    ret_dfs(matrix,i,visited)
    ret_dfs(matrix,start,visited)
    s=''
    l=0
    for i in output:
        s+=str(i)
        s+="(("
        s+=str(i)
        s+='))'
        if l!=len(output)-1:
            s+='-->'
        l+=1
    return [output,s]


def bfs_ouptut(matrix,start=0,visited=[]):
    output=[]
    def ret_bfs(start):
        visited = []
        q = [start]
        visited.append(start)
        while q:
            vis = q[0]
            output.append(vis)
            q.pop(0)
            for i in range(len(matrix)):
                if (matrix[vis][i] == 1 and
                      (i not in visited)):
                    q.append(i)
                    visited.append(i)
    ret_bfs(start)
    print(output)
    s=''
    l=0
    for i in output:
        s+=str(i)
        s+="(("
        s+=str(i)
        s+='))'
        if l!=len(output)-1:
            s+='-->'
        l+=1
    return [output,s]