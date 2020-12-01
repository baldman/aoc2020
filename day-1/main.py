
def part1(fn='input.txt', target=2020, skip=None):
    """
    Find a solution using one pass and complements.

    Complexities:
    - time: O(n)
    - space: O(n)
    """
    print("Day 1 of Advent of Code - Part 1")

    with open(fn, 'r') as input_stream:
        complements = set()
        while True:
            number = input_stream.readline()
            if not number:
                break

            number = int(number)

            # Look whether we already seen a number that is a complement to this one to the target sum of `target`.
            # If so, we have a solution.
            if number in complements:
                print(f"Found a solution >>> numbers are {number} and {target - number}. Multiple is: {number * (target - number)}")
                return number, target - number

            complements.add(target - number)


def part2(fn='input.txt'):
    """
    
    """
    ...

if __name__ == '__main__':
    part1()
