graph= {'1':['2','3'],
        '2': ['4','5','6'],
        '3': ['6'],
        '4': [],
        '5':[],
        '6':[]
}

visited = []

def present(list,node):
    for i in list :
        if i == node :
            return True
    return False


def dfs(graph,start_node,visited):
    if not present(visited,start_node):
        print(start_node,'-->')
        visited.append(start_node) 
        for neighbour in graph[start_node]:
            dfs(graph,neighbour,visited)
    
start_node = '1'
dfs(graph,start_node,visited)    
for node in graph.keys():
    visited_set = set(visited)
    if node not in visited_set:
        print("For disconnected graph")
        dfs(graph,node,visited)  