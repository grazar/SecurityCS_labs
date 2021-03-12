P = [0.57, 0.52, 0.88, 0.3, 0.68]

graph = {
    1: [2, 3],
    2: [4],
    3: [4, 5],
    4: [5],
    5: []
}

graph_table_size = len(graph)

scheme = {}
for k, v in graph.items():
    scheme[k - 1] = []
    for i in v:
        scheme[k - 1].append(i - 1)
true_pathes = []
f_pr = []


# Depth-first search algorythm
def DFS_all(graph, start, end, path=[]):
    loc_path = path + [start]
    if start == end:
        true_pathes.append(loc_path)
        f_pr.append(loc_path)
    for node in graph[start]:
        if node not in loc_path:
            DFS_all(graph, node, end, loc_path)

DFS_all(graph, 1, 5)
DFS_all(graph, 1, 2)
DFS_all(graph, 1, 4)
for i in f_pr:
    print(*i)

true_pathes.clear()
DFS_all(scheme, 0, 4)
DFS_all(scheme, 0, 1)
DFS_all(scheme, 0, 3)
# making list of all possible variants
possible_var = []
for i in range(2 ** graph_table_size):
    var = []
    tmp = i
    for j in range(graph_table_size, -1, -1):
        if tmp // (2 ** j) == 1:
            tmp = tmp % (2 ** j)
            var.append(j)
    possible_var.append(sorted(var))

# making list of all workable pathes
possible_pathes = []
for i in possible_var:
    for j in true_pathes:
        if set(j).issubset(set(i)):
            possible_pathes.append(i)
            break

# finding P_system
Ptndv = 0
for i in possible_pathes:
    temp = 1
    for j in range(graph_table_size):
        if int(j) in i:
            temp *= P[j]
        else:
            temp *= 1 - P[j]
    Ptndv += temp

print(f'\nProb of infallible work is: {Ptndv}')

