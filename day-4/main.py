import re

def run():
    def hgt_val_rule(i):
        grps = re.match('^(?P<how_much>\d+)(?P<unit>cm|in)$', i)
        if not grps:
            return False
        return {
            'in': lambda val: 59 <= int(val) <= 76,
            'cm': lambda val: 150 <= int(val) <= 193,
        }.get(grps['unit'], lambda val: False)(grps['how_much'])

    VALIDATION_RULES = {
        'byr': lambda i: 1920 <= int(i) <= 2002,
        'iyr': lambda i: 2010 <= int(i) <= 2020,
        'eyr': lambda i: 2020 <= int(i) <= 2030,
        'hgt': hgt_val_rule,
        'hcl': lambda i: re.search('^#[0-9a-f]{6}$', i) is not None,
        'ecl': lambda i: i in ['amb','blu','brn','gry', 'grn', 'hzl', 'oth'],
        'pid': lambda i: re.search('^\d{9}$', i) is not None,
    }

    def check_valid(input_dict):
        for key, val in input_dict.items():
            if key not in VALIDATION_RULES.keys():
                continue
            if val is None or not VALIDATION_RULES[key](val):
                return False
        return True

    with open('input.txt', 'r') as f:
        valid = 0
        current = None

        while True:
            line = f.readline()
            if not line:
                break

            if line == "\n":
                valid += int(check_valid(current))
                current = None

            # Example: hgt:172in pid:170cm hcl:17106b iyr:2012 ecl:gry
            grp = re.findall("(\w+):([\d\w#]+)\s?", line.strip())
            if not current:
                current = {key: None for key in VALIDATION_RULES.keys()}

            current.update({key: val for key,val in grp})

        # Flush the while at the end again
        valid += int(check_valid(current))

    print(f">>> Valid passports: {valid}")



if __name__ == '__main__':
    run()
