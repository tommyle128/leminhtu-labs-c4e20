
def draw_square (length, square_color):
    from turtle import color, forward, right, mainloop
    color(square_color)
    
    for j in range (4):
        forward(length)
        right(90)
    
    mainloop()
    
# test = draw_square(100, 'red')

