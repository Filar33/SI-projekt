import random
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def solve_maze(maze):
    start_pos = find_start(maze)
    if start_pos is None:
        return None

    visited = set()
    path = []
    best_path = []
    best_points = [float('inf')]  # Initialize with infinity

    dfs(maze, start_pos, visited, path, best_path, best_points)
    return best_path

def dfs(maze, pos, visited, path, best_path, best_points):
    x, y = pos
    rows, cols = len(maze), len(maze[0])

    if x == 0:
        points = calculate_points(path, maze)
        if points < best_points[0]:  # Check if current path has fewer points
            best_points[0] = points
            best_path[:] = path  # Update best_path

    visited.add(pos)

    neighbors = get_neighbors(maze, pos)
    for neighbor in neighbors:
        if neighbor not in visited:
            dfs(maze, neighbor, visited, path + [neighbor], best_path, best_points)

    visited.remove(pos)

def calculate_points(path, maze):
    points = 0
    for pos in path:
        x, y = pos
        if maze[x][y] == '+':
            points -= 3
        elif maze[x][y] == '-':
            points += 3
        elif maze[x][y] == ' ':
            points += 1
    return points

def get_neighbors(maze, pos):
    x, y = pos
    rows, cols = len(maze), len(maze[0])
    neighbors = []

    if x > 0 and maze[x - 1][y] != '#':  # Up
        neighbors.append((x - 1, y))
    if x < rows - 1 and maze[x + 1][y] != '#':  # Down
        neighbors.append((x + 1, y))
    if y > 0 and maze[x][y - 1] != '#':  # Left
        neighbors.append((x, y - 1))
    if y < cols - 1 and maze[x][y + 1] != '#':  # Right
        neighbors.append((x, y + 1))

    return neighbors

def find_start(maze):
    start_positions = []
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == 'e':
                start_positions.append((i, j))
    if start_positions:
        return start_positions[0]
    return None

def print_maze(maze):
    for row in maze:
        print(' '.join(row))

def generate_random_points(maze):
    rows, cols = len(maze), len(maze[0])
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] not in ['#', 'e', 'x']:
                if random.random() < 0.4:  # 40% chance for generating a point
                    if random.random() < 0.5:  # 50% chance for + or -
                        maze[i][j] = '+'
                    else:
                        maze[i][j] = '-'
    return maze

# Example usage:
maze = [
    ['#', 'x', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', ' ', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', ' ', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', '#', '#'],
    ['#', ' ', '#', '#', ' ', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', 'e', '#', '#', '#', '#', '#'],
]

maze = generate_random_points(maze)
print("Original Maze:")
print_maze(maze)

path = solve_maze(maze)
if path:
    print("\nPath found:")
    print("Maze with path:")
    maze_copy = [row[:] for row in maze]  # Create a copy of the maze

    for row in maze_copy:
        for i in range(len(row)):
            if row[i] == '+' or row[i] == '-':
                row[i] = ' '  # Replace '+' or '-' with empty space

    for pos in path:
        x, y = pos
        maze_copy[x][y] = 'P'  # Mark path with 'P'

    print_maze(maze_copy)
else:
    print("\nNo path found.")

if path:
    path_length = len(path)
    points = calculate_points(path, maze)
    ratio = points / path_length if path_length > 0 else 0.0

    print("\nPath length:", path_length)
    print("Cost:", points)
    print("Cost to Path ratio:", round(ratio,2))

# Generate GIF frames
frames = []

fig, ax = plt.subplots()

maze_rows = len(maze)
maze_cols = len(maze[0])
maze_size = max(maze_rows, maze_cols)
fig.set_size_inches(maze_size, maze_size)

def update_frame(i):
    ax.cla()
    ax.set_title(f"Step {i+1}")
    ax.set_xticks([])
    ax.set_yticks([])
    for x in range(maze_rows):
        for y in range(maze_cols):
            if maze[x][y] == '#':
                ax.fill([y, y+1, y+1, y, y], [maze_rows-x, maze_rows-x, maze_rows-x-1, maze_rows-x-1, maze_rows-x], color='black')
            elif maze[x][y] == 'e':
                ax.fill([y, y+1, y+1, y, y], [maze_rows-x, maze_rows-x, maze_rows-x-1, maze_rows-x-1, maze_rows-x], color='green')
            elif maze[x][y] == 'x':
                ax.fill([y, y+1, y+1, y, y], [maze_rows-x, maze_rows-x, maze_rows-x-1, maze_rows-x-1, maze_rows-x], color='red')
            elif (x, y) in path[:i]:
                ax.fill([y, y+1, y+1, y, y], [maze_rows-x, maze_rows-x, maze_rows-x-1, maze_rows-x-1, maze_rows-x], color='blue')
    if i == len(path) - 1:
        ax.text(0.5, 0.5, "Goal reached!", ha='center', va='center', transform=ax.transAxes, fontsize=16)

for i in range(len(path) + 1):
    update_frame(i)
    fig.canvas.draw()
    width, height = fig.canvas.get_width_height()
    buffer = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
    buffer = buffer.reshape((height, width, 3))
    image = Image.fromarray(buffer)
    frames.append(image)

# Generate GIF
frames[0].save('maze_solution.gif', format='GIF', append_images=frames[1:], save_all=True, duration=1000, loop=0)
