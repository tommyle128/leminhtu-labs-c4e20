
def draw_star (x, y, length):
    import turtle
    
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
        
    
    for k in range (5):
        turtle.forward(length)
        turtle.right(144)
        
    turtle.mainloop()
    
# test2 = draw_star(100, 100, 100)