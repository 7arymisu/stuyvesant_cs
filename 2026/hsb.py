def setup():
    size(400,400)

def draw():
    background(220)
    fill(0)
    #text(str(mouse_x) + ", " + str(mouse_y), 20, 20)

    color_mode(HSB,360,100,100)
    
    fill(240,100,100)

    d = 60
    dp5 = d + 5

    text_size(20)
    text("Saturation",50,25)
    text("Brightness",240,25) 
