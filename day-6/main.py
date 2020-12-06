def p1():
    with open('input.txt', 'r') as f:
        curr_set = None
        total = 0
        while True:
            line = f.readline()
            if not line:
                break

            if line == '\n':
                total += len(curr_set)
                curr_set = None
                continue

            if not curr_set:
                curr_set = set()

            curr_set.update([x for x in line.strip()])

        total += len(curr_set)
        print(f">>> Total answers: {total}")


def p2():
    with open('input.txt', 'r') as f:
        curr_set = None
        total = 0
        while True:
            line = f.readline()
            if not line:
                break

            if line == '\n':
                total += len(curr_set)
                curr_set = None
                continue

            line = list(line.strip())
            if curr_set is None:
                curr_set = set(line)
            else:
                for el in curr_set.copy():
                    if el not in line:
                        curr_set.remove(el)

        total += len(curr_set)
        print(f"Total intersections: {total}")


if __name__ == '__main__':
    p2()
