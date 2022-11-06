with open('graf-2txt.txt') as f:
    nodes = int(f.readline().split()[0])    # first line
    print('nodes - ', nodes)
    tablica = {x: [] for x in range(nodes)}

    for x in f:
        line = x.split()
        tablica[int(line[0])].append(int(line[1]))
print(tablica)

for starting_node in range(nodes):
    stop_var = 0
    visited = [starting_node]
    graph_queue = tablica[starting_node]
    while len(visited) != nodes and stop_var <= nodes ** 2 and len(graph_queue) > 0:
        print(f'current node - {graph_queue[0]}')
        print(f'queue - {graph_queue}')
        print(f'visited - {visited}')
        if not (graph_queue[0] in visited):
            visited.append(graph_queue[0])
        graph_queue += tablica[graph_queue[0]]
        graph_queue.pop(0)
        stop_var += 1
    if len(visited) == nodes:
        break


if len(visited) == nodes:
    print('graf jest spójny')
else: print('graf NIE jest spójny')