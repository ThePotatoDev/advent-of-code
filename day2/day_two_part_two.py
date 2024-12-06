reports = []

with open("day2/input.txt", "r") as input:
    for line in input:
        reports.append(list(map(int, line.strip().split())))

def is_valid_row(lst):
    for i in range(len(lst) - 1):
        diff = abs(lst[i] - lst[i + 1])
        if diff < 1 or diff > 3:
            return False
        
    is_increasing = all(lst[i] < lst[i + 1] for i in range(len(lst) - 1))
    is_decreasing = all(lst[i] > lst[i + 1] for i in range(len(lst) - 1))
    return is_decreasing or is_increasing

def check_with_dampener(lst):
    if is_valid_row(lst):
        return True
  
    for i in range(len(lst)):
        new_lst = lst[:i] + lst[i+1:]
        if is_valid_row(new_lst):
            return True
    
    return False

result = 0

for report in reports:
    if check_with_dampener(report):
        result += 1

print("Valid reports:", result)