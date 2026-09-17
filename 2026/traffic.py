from collide2d import *

def setup():
    size(200,600)
    background(220)
    no_stroke()
    fill(255,0,0,125)
    circle(100,100,150)
    no_stroke()
    fill(255,255,0,125)
    circle(100,300,150)
    no_stroke()
    fill(0,255,0,125)
    circle(100,500,150)
    
def draw():
    pass

def mouse_pressed():
    if collidePointCircle(mouse_x,mouse_y,100,100,150):
        fill(255,0,0,255)
    else:
        fill(255,0,0,125)
        circle(100,100,150)
