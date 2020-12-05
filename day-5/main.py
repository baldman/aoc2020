def run():
    def find_position(vector, pos_range):
        for current in vector:
            diff = (pos_range[1] - pos_range[0]) // 2

            if diff == 0:  # We're at the end
                return pos_range[0] if current == 'L' else pos_range[1]

            if current == 'L':
                pos_range = pos_range[0], pos_range[0] + diff
            else:
                pos_range = pos_range[0] + diff + 1, pos_range[1]

    with open('input.txt', 'r') as f:
        highest = 0
        ids = []
        while True:
            line = f.readline()
            if not line:
                break

            row = find_position(line[:7].replace('F', 'L').replace('B', 'R'), (0, 127))
            seat = find_position(line[7:], (0, 7))
            seat_id = row * 8 + seat
            ids.append(seat_id)

            if seat_id > highest:
                highest = seat_id

    print(f">>> Highest seat id {highest}")

    prev = None
    for x in sorted(ids):
        if prev is not None and prev+1 != x:
            print(f">>> My seat is {prev+1}")
            return
        prev = x


if __name__ == '__main__':
    run()
