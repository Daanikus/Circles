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


def rand_colour():

    return color_rgb(random.randint(0, 255),
                     random.randint(0, 255),
                     random.randint(0, 255))

def run_default():
    # Create initial circle in list
    initial_circle = Circle(Point(r, r), r)
    initial_circle.setFill(rand_colour())
    circles = [initial_circle]
    currCircles = circles

    for i in range(0, layers):
        col = rand_colour()
        print(f"Generation {i}:")
        draw_circles(currCircles)
        sleep(2)
        currCircles = []
        for j in range(len(circles) - (NUM_CIRCLES**i), len(circles)):
            currCircles.extend(generate(circles[j], col))
        circles.extend(currCircles)


# --------- Begin ----------

# Welcome message and usage info
print("Welcome to Circles")

parser = argparse.ArgumentParser()
parser.add_argument("-g", "--generation", default="3", help="set number of generations", type=int)
args = parser.parse_args()
layers = args.generation
print(f"Running {args.generation} generations")
ratios = []
colours = []
for line in sys.stdin:
    line = line.strip().split(" ")
    ratios.append(line[0]);
    colours.append(color_rgb(int(line[1]), int(line[2]), int(line[3])))

print(ratios)
print(colours)

sleep(2)
# exit()

# Display window
win = GraphWin("Circles", screen_size, screen_size)

run_time = time.time()

run_default()

run_time = time.time() - run_time
print(f"Completed in {run_time} seconds")
win.getMouse()
win.close()
