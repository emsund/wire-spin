# wire-spin: simple animated 3d objects in Python

def tetrahedron():
    '''
    Return a hashed set containing the line segments of a tetrahedron.

    Form: {[(x,y,z),(x,y,z)], [(x,y,z),(x,y,z)], ...}
    i.e., {[(point), (vector)], ... }

    Each element of the set is a list containing six numerical elements.
    The first three of these elements represent a point in 3d space.
    The next three elements represent a vector that indicates the direction
    and length of the line originating at the given point.
    '''
    
    lines = [
        [0,0,0, 1,1,0],
        [0,0,0, 1,0,1],
        [0,0,0, 0,1,1],
        [0,1,1, 1,-1,0],
        [0,1,1, 1,0,-1],
        [1,0,1, 0,1,-1]
    ]

    return lines

def calc_rejection(vector1, vector2):
    '''Return the "rejection" of vector1 onto vector2'''

    # the projection is calculated by
    # vector projection a' = [(a*(b/|b|)](b/|b|)
    # The quantity in square brackets is a scalar quantity.

    # The vector "rejection" is then calc. as = a - a'

    import math

    a1 = vector1[0]
    a2 = vector1[1]
    a3 = vector1[2]

    b1 = vector2[0]
    b2 = vector2[1]
    b3 = vector2[2]

    magnitude_b = math.sqrt(b1**2 + b2**2 + b3**2)

    bu1 = b1 / magnitude_b
    bu2 = b2 / magnitude_b
    bu3 = b3 / magnitude_b

    ap1 = a1 * bu1
    ap2 = a2 * bu2
    ap3 = a3 * bu3

    ap = ap1 + ap2 + ap3

    ap1 = ap * bu1
    ap2 = ap * bu2
    ap3 = ap * bu3

    # Calculate the "rejection" (the part along the plane, i.e. perpend. to
    # plane vector given.
    r1 = a1 - ap1
    r2 = a2 - ap2
    r3 = a3 - ap3

    return [r1, r2, r3]


def project_line_to_plane(line, plane):
    ''' Return 3d vector projection onto given 2d plane
    
    "line" is a six-element list, first three for start-point, next for vector

    "plane" is actually just a vector perpendicular to plane. Because we are
    not doing anything with perspective, location of plane does not matter.
    '''

    # position vector (start-point)
    a = line[0:3]

    # line-segment >end-point vector<, from origin
    b = [line[3] + a[0], line[4] + a[1], line[5] + a[2]]

    proj1 = calc_rejection(a, plane)
    proj2 = calc_rejection(b, plane)
    projected_line = proj1 + proj2
   

    return projected_line


def project_mesh(mesh, viewing_plane):
    for line in mesh:

        proj = project_line_to_plane(line, viewing_plane)

        print(proj, "\n")


def draw_line(line):
    '''
    Accepts a 4-element list/tuple representing a line

    Expects form (startpoint_x, startpoint_y, endpoint_x, endpoint_y)
    '''

    import tkinter

    root = tkinter.Tk()
    canvas = tkinter.Canvas(root)
    canvas.config(background='black')
    canvas.pack()

    canvas.create_line(line[0], line[1], line[2], line[3], fill="light gray", width=1)

    root.mainloop()



plane = (1,1,1)
tet = tetrahedron()
project_mesh(tet, plane)

segment = (45,20, 200, 200)
#draw_line(segment)

