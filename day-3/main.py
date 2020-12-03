from functools import reduce


def run():
    pairs = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    def count_encounters(input_f, right=3, down=1):
        with open(input_f, 'r') as f:
            tree_ctr = right_ctr = line_len = 0  # Counters

            for down_ctr, line in enumerate(f.readlines(), 1):
                # Skip down as needed and initial positioning
                if down_ctr <= down or ((down_ctr + 1) % down) != 0:
                    line_len = len(line) - 1
                    continue

                right_ctr += right  # Skip right
                tree_ctr = tree_ctr + int(line[right_ctr % line_len] == '#')

            return tree_ctr

    total = reduce(lambda a, b: a*count_encounters('input.txt', *b), pairs, 1)
    print(f"Total trees >>> {total}")


if __name__ == '__main__':
    run()
