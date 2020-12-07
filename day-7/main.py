import re


class Node:

    def __init__(self, name):
        self.name = name
        self.visited = False
        self.children = []
        self.parents = []


def get_node(name, lut):
    if name not in lut:
        lut[name] = Node(name)

    return lut[name]


def run(which_one):
    # 1. construct graph from file
    with open('input.txt', 'r') as f:
        lut = {}
        while True:
            line = f.readline()
            if not line:
                break

            parsed = re.findall('(\w+\s\w+)\sbags\scontain\s(.*)', line.strip())
            root_node = get_node(parsed[0][0], lut)

            child_nodes = re.findall('((\d+)\s(\w+\s\w+))\sbags?[,|\.]\s?', parsed[0][1])

            for child in child_nodes:
                n = get_node(child[2], lut)
                root_node.children.append(
                    (n, int(child[1]))  # Node, <count>
                )
                n.parents.append(root_node)

    # 2. Perform a BFS (or some other search) target->parents to find all (P1)
    inclusions = []
    search_stack = [lut[which_one]]
    while len(search_stack):
        node = search_stack.pop()

        # Special case the target
        if node.name != which_one:
            inclusions.append(node)

        for parent in node.parents:
            if parent.visited is True:
                continue

            parent.visited = True
            search_stack.append(parent)

    print(f'>>> {which_one} is included by proxy in {len(inclusions)}: {[n.name for n in inclusions]}')

    # 3. Perform a DFS target->children to find and count all using dynamic
    # programming for speed (P2)
    cache = {}

    def solve_for_node(curr):
        my_total = 1
        for chld, cnt in curr.children:
            if chld.name not in cache:
                cache[chld.name] = solve_for_node(chld)

            my_total += cnt * cache[chld.name]

        return my_total

    tot_bags = solve_for_node(lut[which_one]) - 1  # -1 for the starting nodes
    print(f'>>> {which_one} needs {tot_bags} bags in it')


if __name__ == '__main__':
    run('shiny gold')
