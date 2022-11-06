# download this file 
# https://api.dlanauczyciela.pl/api/v1/files/229447/download
# https://informatyka.edu.pl/zasoby/szkola-ponadpodstawowa,informatyka-na-czasie,zakres-rozszerzony,czesc-3

with open('graf-2txt.txt') as f:
    nodes_num = int(f.readline().split()[0])
    print('nodes - ', nodes_num)
    
    tablica: dict = {x: [] for x in range(nodes_num)}

    for x in f:  # inserting variables into "tablica"
        line = x.split()
        tablica[int(line[0])].append(int(line[1]))
print(tablica)

# checking routes from all starting nodes
for starting_node in range(nodes_num):

    stop_var = 0 
    visited = [starting_node]
    graph_queue = tablica[starting_node]


    while len(visited) != nodes_num \
        and stop_var <= nodes_num **2 \
        and len(graph_queue) > 0:
        # visiting all nodes until we have visited them all
        current_node = graph_queue[0]
        print(f'current node - {current_node}')
        print(f'queue - {graph_queue}')
        print(f'visited - {visited}')

        # unless this node wasnt already visited
        # we add them to queue
        if not (current_node in visited):
            visited.append(current_node)

        # connections from this node
        current_edges = tablica[current_node]
        print(f'connections - {current_edges}')

        # adding all connection from this node to the queue
        for x in current_edges:
            if x not in visited and x not in graph_queue:
                graph_queue.append(x)

        graph_queue.pop(0)  #removing current node from the queue

        stop_var += 1

    # when we already have visited all nodes then there is no need to start from other nodes
    if len(visited) == nodes_num:
        break

# printing out answer
if len(visited) == nodes_num:
    print('graf jest spójny')
else:
    print('graf NIE jest spójny')
