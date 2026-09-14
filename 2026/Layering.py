def setup():
    size(400, 400)  # canvas similar proportions to the image (taller than wide)
    print("width =", width, "\nheight =", height)
    
def draw():
    background(220)
    fill(255)
    stroke(0)
    circle(120,120,200)
    fill(220)
    no_stroke()
    rect(10,100,220,150)
    stroke(0)
    line(20,100,220,100)
