import re

mul_pattern = r'\b\w*mul\((\d+),\s*(\d+)\)'
do_pattern = r'\w*do\(\)'
dont_pattern = r'\bdon\'t\(\)'

multiply = True
total = 0

with open("day3/input.txt", "r") as input:
    content = input.read()

parts = re.split(r'(\bmul\(\d+,\s*\d+\)|\bdo\(\)|\bdon\'t\(\))', content)

for part in parts:
    part = part.strip()
    print(part)

    if re.match(do_pattern, part):
        multiply = True
    elif re.match(dont_pattern, part):
        multiply = False
    elif multiply and (match := re.match(mul_pattern, part)):
        total += int(match.group(1)) * int(match.group(2))

print("Total", total)