list1 = []
list2 = []

with open("day1/input.txt", "r") as input:
    for line in input:
        parts = line.strip().split()
        list1.append(int(parts[0]))
        list2.append(int(parts[1]))

list1.sort()
list2.sort()
distance = 0

for left, right in zip(list1, list2):
    distance += abs(left - right)

print("Distance", distance)