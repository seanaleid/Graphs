from util import Stack, Queue

def earliest_ancestor(ancestors, starting_node):
    vertices = {}

    for v1, v2 in ancestors:
        if v1 not in vertices:
            vertices[v1] = set()
        if v2 not in vertices:
            vertices[v2] = set()    
        if v2 in vertices:
            vertices[v2].add(v1)
    
    q = Queue()
    q.enqueue(starting_node)

    visited = list()

    while q.size() > 0:
        v = q.dequeue()

        if v not in visited:
            visited.append(v)

            for next_node in vertices[v]:
                if next_node is None:
                    visited.append(-1)
                else:
                    q.enqueue(next_node)
    
    if len(visited) == 1:
        return -1
    else:
        return visited[-1]

    

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 1))
print(earliest_ancestor(test_ancestors, 2))
print(earliest_ancestor(test_ancestors, 3))
print(earliest_ancestor(test_ancestors, 4))
print(earliest_ancestor(test_ancestors, 5))
print(earliest_ancestor(test_ancestors, 6))
print(earliest_ancestor(test_ancestors, 7))
print(earliest_ancestor(test_ancestors, 8))
print(earliest_ancestor(test_ancestors, 9))
print(earliest_ancestor(test_ancestors, 10))
print(earliest_ancestor(test_ancestors, 11))