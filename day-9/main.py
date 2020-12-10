
def p1():
    """
    This is basically O(n*b) where n is the number of lines and b is the buffer
    size. Technically, that's a constant, so in the end, you end up in O(n)
    """
    PREAMBLE_SIZE = 25
    with open('input.txt', 'r') as f:
        cntr = 0
        stream = []
        while True:
            line = f.readline()
            if not line:
                break

            cntr += 1
            number = int(line.strip())
            # Read into the stream first
            if cntr <= PREAMBLE_SIZE:
                stream.append(number)
                continue

            # Ok, I am at the number that I need to sum up to?
            complements = set()
            for n in stream:
                if n in complements:
                    break
                complements.add(number-n)
            else:
                print(f">>> Number {number} is not sum of the previous ones")
                return number

            # Append 1, drop first element
            stream.append(number)
            stream.pop(0)


def p2(target):
    print(f">>> Looking for largest range targeting: {target}")

    def read_data():
        with open('input.txt', 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                yield int(line.strip())

    consume_number = read_data()
    max_consecutive = []
    stream = []
    curr_sum = 0

    # Find the sum in O(n) time
    while True:
        # We have a solution, great. Potentially save it, pop off of the
        # beginning of the stream (FIFO like) and continue
        if curr_sum == target:
            if len(stream) > len(max_consecutive):
                max_consecutive = stream.copy()
            curr_sum -= stream.pop(0)
            continue

        # Okay, overflown, so, pop off of the end of the stream and continue
        if curr_sum > target:
            curr_sum -= stream.pop(0)
            continue

        # Now
        if curr_sum < target:
            try:
                number = next(consume_number)
            except StopIteration:
                break
            curr_sum += number
            stream.append(number)

    # Find low and high in a O(n) fashion (probs not worth it)
    low = high = None
    for num in max_consecutive:
        if high is None or num > high:
            high = num

        if low is None or num < low:
            low = num

    print(f">>> Sum of the numbers on the rage {low} and {high} is {low+high}")


if __name__ == '__main__':
    p2(p1())
