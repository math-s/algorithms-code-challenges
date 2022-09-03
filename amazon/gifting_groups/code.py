"""Amazon challenge"""

related0 = [
    '1100',
    '1110',
    '0110',
    '0001'
] # 2
related1 = [
    '10000',
    '01000',
    '00100',
    '00010',
    '00001'
] # 5
related2 = [
    '11001',
    '11000',
    '00100',
    '00010',
    '10001'
] # 3
related3 = [
    '11111',
    '11111',
    '11111',
    '11111',
    '11111'
] # 1
related4 = [
    '111111',
    '111111',
    '111111',
    '111111',
    '111111',
    '111111',
] # 1


def count_groups(related: list) -> int:
    """Counts the number of groups"""

    dimension = len(related)
    indexes = range(dimension)

    connected_nodes = {}

    for i in indexes:
        connected_nodes[i] = {i}

    for i in indexes:
        for j in indexes:

            same_person = i == j
            has_relationship = related[i][j] == '1'

            if same_person:
                continue

            if has_relationship:
                connected_nodes[i].add(j)

    for node, connections in connected_nodes.items():
        for connection in connections:
            connected_nodes[node] = connected_nodes[node].union(connected_nodes[connection])

    groups = []
    for node, connections in connected_nodes.items():
        if connections not in groups:
            groups.append(connections)

    return len(groups)

assert count_groups(related0) == 2
assert count_groups(related1) == 5
assert count_groups(related2) == 3
assert count_groups(related3) == 1
assert count_groups(related4) == 1
