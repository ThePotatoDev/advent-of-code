grid = []

with open("day4/input.txt", "r") as input:
     for line in input:
        grid.append(line.strip().split())

count = 0

def count_word_occurrences(grid, word):
    rows, cols = len(grid), len(grid[0][0])
    word_len = len(word)
    directions = [
        (0, 1),  # Horizontal right
        (0, -1),  # Horizontal left
        (1, 0),  # Vertical down
        (-1, 0),  # Vertical up
        (1, 1),  # Diagonal down-right
        (-1, -1),  # Diagonal up-left
        (1, -1),  # Diagonal down-left
        (-1, 1)  # Diagonal up-right
    ]

    def is_valid(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][0][ny] != word[i]:
                return False
        return True

    count = 0  # Counter for occurrences
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if is_valid(x, y, dx, dy):
                    count += 1

    return count



print(count_word_occurrences(grid, "XMAS"))
