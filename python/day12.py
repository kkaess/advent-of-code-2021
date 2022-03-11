from igraph import Graph, plot

with open('input/input_day12.txt') as f:
    formula = ', '.join(f.read().splitlines())

g = Graph.Formula(formula)

start = g.vs.find(name="start")
end = g.vs.find(name="end")

majors = []

for vertex in g.vs:
    name = vertex.attributes()['name']
    if len(name) == 2:
        if not name.lower() == name:
            majors += [vertex.index]

path_queue = [[start.index]]
valid_paths = []

while len(path_queue) > 0:
    current_path = path_queue.pop()
    for vertex in g.vs[current_path[-1]].neighbors():
        if vertex.index == end.index:
            valid_paths.append(current_path+[vertex.index])
        elif vertex.index in majors or vertex.index not in current_path:
            path_queue.append(current_path+[vertex.index])

print(len(valid_paths))

path_queue = [[[start.index], False]]
valid_paths = []

while len(path_queue) > 0:
    current_path = path_queue.pop()
    for vertex in g.vs[current_path[0][-1]].neighbors():
        if vertex.index == start.index:
            continue
        if vertex.index == end.index:
            valid_paths.append(current_path[0]+[vertex.index])
        else:
            if vertex.index in majors or vertex.index not in current_path[0]:
                path_queue.append([current_path[0]+[vertex.index],current_path[1]])
            elif not current_path[1]:
                path_queue.append([current_path[0] + [vertex.index], True])

print(len(valid_paths))
