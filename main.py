# Quadrilaterals Project by Peyton Goodlett
# Start: 1/8/25
# Finish: 2/12/25
import math
quadrils = ["Square", "Rectangle", "Parallelogram", "Kite", "Rhombus", "Trapezoid"]


def generateGrid(length, height):
    # Generate a grid based on the length and height of our shape.
    rows, col = height, length
    return [[" "] * col for _ in range(rows)]

def normalPrint(grid):
    for row in grid:
        print(row)

def prettyPrint(grid):
    # Print our shape prettily, showing only its outline
    for row in grid:
        print(" ".join(row))

# Quadrilateral Functions

def square(grid, length):
    # Using our grid, generate a square of a given length
    for i in range(length):
        for z in range(length):
            grid[z][i] = "#"
    return prettyPrint(grid)

# While we could've merged these functions together,
# I decided to seperate them to keep it simple.

def rectangle(grid, length, width):
    # Using our grid, generate a rectangle of a given length and width
    for i in range(length):
        for z in range(width):
            grid[z][i] = "#"
    return prettyPrint(grid)

def rhombus(grid, length, width):
    # Using our grid, generate a rhombus (diamond-shaped) of a given length and width
    # a**2 + b**2 = c**2
    radius = round(length/2)
    height = round(width/2)
    leg = math.sqrt((radius**2)+(height**2))
    points = []
    for z in range(height):
        i = height-1
        # print(f"Z: {z} | I: {i-z}")
        points.append((z,i-z))
    for z in range(height):
        i = height-1
        # print(f"Z: {z} | I: {i+z}")
        points.append((z,i+z))
    for z in range(height):
        i = height-1
        # print(f"Z: {z+height-1} | I: {i-z+height-1}")
        points.append((z+height-1,i-z+height-1))
    for z in range(height):
        i = height-1
        # print(f"Z: {z-height-1} | I: {i+z-height+1}")
        points.append((z-height-1,i+z-height+1))
    for item in points:
        grid[item[0]][item[1]] = "#"
    return prettyPrint(grid)

def parallelogram(grid, length, width):
    # Using our grid, create a parallelogram
    points = []
    for z in range(width):
        i = width-1
        # print(f"Z: {z} | I: {i-z}")
        points.append((z,i-z))
    for i in range(round(length/2)):
        z = 0
        points.append((z, round(i+width)))
    for z in range(width):
        i = width-1
        # print(f"Z: {z} | I: {i-z}")
        points.append((z,round(i-z+length/2)))
    for i in range(round(length/2)):
        z = width-1
        points.append((z, i))
    print(points)
    for item in points:
        grid[item[0]][item[1]] = "#"
    return prettyPrint(grid)

print(parallelogram(generateGrid(12,6), 12, 6))
