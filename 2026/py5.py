import py5

def setup():
    py5.size(400, 500)  # canvas similar proportions to the image (taller than wide)
    py5.print("width =", py5.width, "\nheight =", py5.height)

def draw():
    py5.background(220)  # light grey background like the slide image
    py5.fill(255)        # white squares
    py5.stroke(0)        # black outline on squares

    square_size = 50
    margin = 20

    # top-left square
    py5.square(margin, margin, square_size)

    # top-right square
    py5.square(py5.width - margin - square_size, margin, square_size)

    # bottom-left square
    py5.square(margin, py5.height - margin - square_size, square_size)

    # bottom-right square
    py5.square(py5.width - margin - square_size, py5.height - margin - square_size, square_size)

py5.run_sketch()