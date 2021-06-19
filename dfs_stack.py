graph= {'1':['2','3'],
        '2': ['4','5','6'],
        '3': ['6'],
        '4': [],
        '5':[],
        '6':[],
        '7':['8','9'],
        '8':['10'],
        '9':[],
        '10':[]
}


def present(list,node):
    for i in list :
        if i == node :
            return True
    return False


def dfs(graph,visited,start_node):
    stack = [] 
    top = -1
    stack.append(start_node)
    top += 1
    while not (len(stack)==0):
        if not present(visited,stack[top]):
            visited.append(stack[top])
            node = stack[top]
            print(stack[top])
            stack.pop()
            top -=1
            for neighbour in graph[node]:
                if not present(stack,neighbour):
                    stack.append(neighbour) 
                    top += 1
            
        else:
            stack.pop()
            top -= 1


visited = []

start_node = '1'
dfs(graph,visited,start_node) 
for node in graph.keys():
    visited_set = set(visited)
    if node not in visited_set:
        print("For disconnected graph")
        dfs(graph,visited,node)
print(visited)