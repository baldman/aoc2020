import re


def part1_checker(parsed):
    """
    Check that the range of occurrences of a letter is valid.

    Ex: 1-3 x means "at least one and at most 3 occurrences of x"
    """
    counter = parsed['pwd'].count(parsed['letter'])
    return int(parsed['start']) <= counter <= int(parsed['end'])


def part2_checker(parsed):
    """
    Check that the letter is at most at given positions. Note the indexing is
    shifted by 1, aka we count from 1, not 0

    Ex: 1-3 x means "x has to be either the first letter or the third letter"
    """
    position_checks = [False, False]

    for idx, char in enumerate(parsed['pwd'], 1):
        if idx == int(parsed['start']):
            position_checks[0] = char == parsed['letter']
        if idx == int(parsed['end']):
            position_checks[1] = char == parsed['letter']

    return position_checks[0] != position_checks[1]

def run():
    p1_valid_passwords = 0
    p2_valid_passwords = 0
    # ctr = 0

    with open('input.txt', 'r') as f:
        while True:
            # ctr +=1
            raw_pwd = f.readline()
            if not raw_pwd:
                break

            # Parse out this format into named groups: "1-2 x: xpxc"
            parsed = re.match("^(?P<start>\d+)\-(?P<end>\d+)\s(?P<letter>\w+):\s(?P<pwd>\w+)$", raw_pwd)

            if part1_checker(parsed):
                p1_valid_passwords += 1

            if part2_checker(parsed):
                p2_valid_passwords += 1

            # break

    print(f">>> Valid passwords (Part I): {p1_valid_passwords}")
    print(f">>> Valid passwords (Part II): {p2_valid_passwords}")


if __name__ == '__main__':
    run()
