import re

pattern = r'\bmul\((\d+(\.\d+)?),\s*(\d+(\.\d+)?)\)'

with open("day3/input.txt", "r") as input:
    content = input.read()

matches = re.findall(pattern, content)
total = 0

for match in matches:
    total += int(match[0]) * int(match[2])

print("Total", total)