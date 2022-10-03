def compute(side_of_cube,painted_sides):
    if painted_sides==1:
        return 6 * ((side_of_cube-2)**2)
    elif painted_sides==2:
        return 12 * (side_of_cube-2)
    elif painted_sides==3:
        return 8
    else:
        return (side_of_cube-2)**3
print(compute(5,3))