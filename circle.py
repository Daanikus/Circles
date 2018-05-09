import types
from graphics import *
from time import sleep
from math import sin, cos
import argparse
import random
import sys

# Defaults
ratio = 3
r = 300
screen_size = r * 2
NUM_CIRCLES = 7


def generate(circle, colour):
    circles = []
    r_small = circle.radius / ratio
    r2 = r_small * 2
    # 60 degrees in radians for math functions
    angles = [1.0472, -1.0472]
    center = circle.getCenter()
    Cx = center.getX()
    Cy = center.getY()

    # Generate 3 horizontal circles
    for i in range(0, 3):
        temp = Circle(Point((Cx + ((i-1) * r2)), Cy), r_small)
        temp.setFill(colour)
        circles.append(temp)

    # Generate the 4 "corner" circles
    for i in range(0, 2):
        for angle in angles:
            if i == 0:
                X = Cx - (r2 * cos(angle))
                Y = Cy - (r2 * sin(angle))
            else:
                X = Cx + (r2 * cos(angle))
                Y = Cy + (r2 * sin(angle))
            center = Point(X, Y)
            temp = Circle(center, r_small)
            temp.setFill(colour)
            circles.append(temp)
    return circles


# Print all circles in resultant list of circles
def draw_circles(circles):

    count = 0
    for c in circles:
        c.draw(win)
        #sleep(.3)
        count = count + 1
    print(f"{count} circles drawn")


def generate_colours():
    colours = []

    for i in range(0, layers):
        c = color_rgb(random.randint(0, 255),
                      random.randint(0, 255),
                      random.randint(0, 255))
        colours.append(c)
    return colours

def run(colours):
    if not colours:
        colours = generate_colours()

    # Create initial circle in list
    initial_circle = Circle(Point(r, r), r)
    initial_circle.setFill(colours[0])
    circles = [initial_circle]
    curr_circles = circles
    for i in range(0, layers):
        print(f"Generation {i}:")
        draw_circles(curr_circles)
        if i == layers - 1:
            break
        curr_circles = []

        # sleep(1)
        for j in range(len(circles) - (NUM_CIRCLES**i), len(circles)):
            curr_circles.extend(generate(circles[j], colours[i+1]))
        circles.extend(curr_circles)




def has_stdin():
    return not sys.stdin.isatty()


# --------- Begin ----------


print("Welcome to Circles")

# Set up command line args
parser = argparse.ArgumentParser()
parser.add_argument("-g", "--generation", default="3", help="set number of generations", type=int)
args = parser.parse_args()
layers = args.generation


ratios = []
colours = []
if has_stdin():
    count = 0
    print("Running with input file. -g flag will be ignored, if specified")
    for line in sys.stdin:
        line = line.strip().split(" ")
        ratios.append(line[0])
        colours.append(color_rgb(int(line[1]), int(line[2]), int(line[3])))
        count = count + 1
    layers = count
else:
    print("Running with defaults")

print(f"Running {layers} generations")
print(ratios)

# Display window
win = GraphWin("Circles", screen_size, screen_size)

run_time = time.time()

run(colours)

run_time = time.time() - run_time
print(f"Completed in {run_time} seconds")
win.getMouse()
win.close()
