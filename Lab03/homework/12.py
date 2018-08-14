from inside import is_inside

# case 1:
point1 = [100, 120]
rect1 = [140, 60, 100, 200]
case1 = is_inside(point1, rect1)

# case 2:
point2 = [200, 120]
rect2 = [140, 60, 100, 200]
case2 = is_inside(point2, rect2)

if case1 == False and case2 == True:
    print("Your function is correct")
else:
    print("Ooops, bugs detected")