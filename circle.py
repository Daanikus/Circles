from graphics import *
from time import sleep
from math import sin, cos
import random


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
    list_length = len(circles)
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


# --------- Begin ----------

# Global colour values
colours = ["red", "blue", "green", "yellow", "orange", "cyan"]

# Defaults
ratio = 3
r = 500
screen_size = r * 2
layers = 4

# Display window
win = GraphWin("Circles", screen_size, screen_size)

# Create initial circle in list
circles = [Circle(Point(r, r), r)]

for i in range(0, layers):
    col = rand_colour()
    for j in range(len(circles) - (7**i), len(circles)):
        circles.extend(generate(circles[j], col))

run_time = time.time()
draw_circles(circles)
run_time = time.time() - run_time
print(f"Completed in {run_time} seconds")
win.getMouse()
win.close()
