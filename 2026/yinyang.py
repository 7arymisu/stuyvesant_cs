def setup():
    size(500,500)

def draw():
    background(220)
    fill(255)
    stroke(0)
    stroke_weight(5)
    circle(250,250,400)
    fill(0)
    arc(250,250,400,400,radians(90),radians(270))
    circle(250,150,200)
    fill(255)
    no_stroke()
    circle(250,350,200)
