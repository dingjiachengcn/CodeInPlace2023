import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
TRIANGLE_WIDTH = 100
TRIANGLE_HEIGHT = 100


def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Point 1: Bottom Left
    x1 = (CANVAS_WIDTH - TRIANGLE_WIDTH) / 2
    y1 = (CANVAS_HEIGHT + TRIANGLE_HEIGHT) / 2

    # Point 2: Bottom Right
    x2 = (CANVAS_WIDTH + TRIANGLE_WIDTH) / 2
    y2 = (CANVAS_HEIGHT + TRIANGLE_HEIGHT) / 2

    # Point 3: Middle
    x3 = CANVAS_WIDTH / 2
    y3 = (CANVAS_HEIGHT - TRIANGLE_HEIGHT) / 2

    canvas.create_polygon(x1, y1, x2, y2, x3, y3)

if __name__ == '__main__':
    main()