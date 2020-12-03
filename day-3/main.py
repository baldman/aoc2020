from functools import partial, reduce


def count_tree_encounters(input="input.txt", right=3, down=1):
    """
    Simple one-pass iteration over the input. Nothing fancy.

    Complexities:
        - time: O(n) where n is number of lines
        - space: O(1) - or if you want to be diligent, O(s) where s is the length of one input line
    """
    with open(input, 'r') as f:
        # Counters
        down_ctr = tree_ctr = right_ctr = line_len = 0

        while True:
            line = f.readline().strip()
            if not line:
                break

            down_ctr += 1
            # Skip down as needed and initial positioning
            if down_ctr <= down or ((down_ctr+1) % down) != 0:
                line_len = len(line)
                continue

            # Skip right
            right_ctr += right
            char_at_pos = line[right_ctr % line_len]

            if char_at_pos == '#':
                tree_ctr += 1

        return tree_ctr


def run():
    count_over_same_input = partial(count_tree_encounters, 'input.txt')
    pairs = [
        (1, 1),
        (3, 1),  # Part 1
        (5, 1),
        (7, 1),
        (1, 2)
    ]

    total = reduce(lambda a, b: a*count_over_same_input(*b), pairs, 1)
    print(f"Total trees >>> {total}")


if __name__ == '__main__':
    run()
