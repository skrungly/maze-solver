import colorsys as coloursys

from PIL import Image
from time import time

# Oof, this is painful.
Image._decompression_bomb_check = lambda _: _


def load(filepath):
    image = Image.open(filepath).convert("1")
    pixels = image.load()

    grid = []
    for i in range(image.width):
        grid.append([])
        for j in range(image.height):
            grid[i].append(pixels[j, i])

    return grid


def navigate(maze, start=None, end=None):
    width = len(maze[0])
    height = len(maze)

    # Set the start position
    if start is None:
        start = (0, 0)

    start_x = start[0] % width
    start_y = start[1] % height
    start = (start_x, start_y)

    # Set the end position
    if end is None:
        end = (-1, -1)

    end_x = end[0] % width
    end_y = end[1] % height
    end = (end_x, end_y)

    # Initialise our path and start navigation
    path = [start]
    while path[-1] != end:
        x, y = path[-1]

        north = (x, y - 1)
        south = (x, y + 1)
        east = (x + 1, y)
        west = (x - 1, y)

        # Attempt to move in all directions
        for direction in north, south, east, west:
            x, y = direction
            
            # Skip the current direction if we've gone out of bounds
            if x not in range(width) or y not in range(height):
                continue

            # If it isn't a wall here, make it one.
            if maze[y][x]:
                maze[y][x] = False
                path.append(direction)
                break
        # If we can't move, go back
        else:
            path.pop()

    return path


def save(maze, file: str):
    print("Drawing path...")
    image = Image.open(file).convert("RGB")
    pixels = image.load()

    # Draw each point of the path onto the image
    for i, point in enumerate(path):
        pixels[point] = (255, 0, 0)

    print("Saving to file...")
    image.save("solution.png")


if __name__ == "__main__":
    file = input("Please enter maze file >> ")
    print(">------<")

    start_loading = time()
    print("Loading image...")
    maze = load(file)
    print("Loaded in {:.02f} seconds".format(time() - start_loading))
    print(">------<")

    start_navigate = time()
    print("Searching for path...")
    path = navigate(
        maze = maze,
        start = (0, 1),
        end = (-1, -1)
    )

    print("Found in {:.02f} seconds".format(time() - start_navigate))
    print(">------<")

    start_saving = time()
    save(maze, file)
    print("Saved in {:.02f} seconds".format(time() - start_saving))
    print(">------<")

    input("Finished in {:.02f} seconds total! Press <ENTER> to exit. ".format(time() - start_loading))
