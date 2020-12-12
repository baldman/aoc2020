
def p1(sorted_input, device_joltage):
    prev = None
    diffs = {1: 0, 2: 0, 3:0}
    for current in [0] + sorted_input + [device_joltage]:
        if prev is None:
            prev = current
            continue

        diffs[current-prev] += 1
        prev = current

    print(f">>> Multiplied joltage diffs: {diffs[1]*diffs[3]}")


def p2(sorted_input, joltage):
    possible_combinations = {0: 1}
    for val in sorted_input + [joltage]:
        possible_combinations[val] =  possible_combinations.get(val-1, 0) + possible_combinations.get(val-2, 0) + possible_combinations.get(val-3, 0)
    print(f">>> Found {possible_combinations[joltage]} solutions for input length of {len(sorted_input)}")

def run():
    with open('input.txt', 'r') as f:
        raw_input = [int(x) for x in f.readlines()]

    sorted_input = [x for x in sorted(raw_input)]
    device_joltage = sorted_input[-1] + 3

    p1(sorted_input, device_joltage)
    p2(sorted_input, device_joltage)

if __name__ == '__main__':
    run()
