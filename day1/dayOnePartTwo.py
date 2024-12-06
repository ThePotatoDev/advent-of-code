from collections import Counter

list1 = []
list2 = []

with open("day1/input.txt", "r") as input:
    for line in input:
        parts = line.strip().split()
        list1.append(int(parts[0]))
        list2.append(int(parts[1]))

result = 0

# Loop through each number in list1
for number in list1:
    result += list2.count(number) * number

print("Result", result)