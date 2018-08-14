def is_inside(point, rect):
    end_x = rect[0] + rect[2]
    end_y = rect[1] + rect[3] 

    if rect [0] <= point [0] <= end_x and rect[1] <= point [1] <= end_y:
        return True
    else:
        return False


