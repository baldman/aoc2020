
def part1(fn='input.txt', target=2020, skip=0):
    """
    Find a solution using one pass and complements.

    Complexities:
    - time: O(n)
    - space: O(n)
    """
    skip == 0 and print("Day 1 of Advent of Code - Part 1")

    with open(fn, 'r') as input_stream:
        complements = set()
        skipped = 0
        while True:
            number = input_stream.readline()
            if not number:
                break

            number = int(number)

            # Skip in the input if instructed
            if skip > skipped:
                skipped +=1
                continue

            # Look whether we already seen a number that is a complement to this
            # one to the target sum of `target`. If so, we have a solution.
            if number in complements:
                if skip == 0:
                    print(">>> Found a solution <<<")
                    print(f"Numbers: {number} and {target - number}")
                    print(f"Multiple is: {number * (target - number)}")
                return number, target - number

            complements.add(target - number)

    return None


def part2(fn='input.txt', target=2020):
    """
    Reuse P1 because of my laziness.

    This definitely could be done in a a single function and one hashmap instead
    of complement set without the additional overhead of stack call and
    (re)allocating of the set in memory.

    Complexities:
        - time: O(n^2)
        - space: O(n)
    """
    print("Day 1 of Advent of Code - Part 2")

    with open(fn, 'r') as input_stream:
        ctr = 0
        while True:
            ctr +=1
            number = input_stream.readline()
            if not number:
                break

            number = int(number)

            # Just use P1
            sub_target = target - number
            sumof2 = part1(target=sub_target, skip=ctr)
            if sumof2:
                print(">>> Found a solution <<<")
                print(f"Numbers: {number} and {sumof2[0]} and {sumof2[1]}")
                print(f"Multiple is: {number * sumof2[0] * sumof2[1]}")


if __name__ == '__main__':
    part2()
