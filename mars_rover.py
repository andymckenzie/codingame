mport sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

N = int(raw_input()) # the number of points used to draw the surface of Mars.
LANDX = []
LANDY = []
for i in xrange(N):
    # LAND_X: X coordinate of a surface point. (0 to 6999)
    # LAND_Y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    LAND_X, LAND_Y = [int(i) for i in raw_input().split()]
    LANDX.append(LAND_X)
    LANDY.append(LAND_Y) 
    
LANDX_flat_middle = ()
for i in xrange(0, len(LANDY)): 
    if i >= 1: 
        if LANDY[i] - LANDY[i-1] == 0: 
            LANDX_flat_middle = ((LANDX[i] + LANDX[i-1]) / 2)

# game loop
while 1:
    # HS: the horizontal speed (in m/s), can be negative.
    # VS: the vertical speed (in m/s), can be negative.
    # F: the quantity of remaining fuel in liters.
    # R: the rotation angle in degrees (-90 to 90).
    # P: the thrust power (0 to 4).
    X, Y, HS, VS, F, R, P = [int(i) for i in raw_input().split()]
    
    Pow = 3
    Rot = 0
    
    if abs(X - LANDX_flat_middle) < 100: 
        Rot = 0 
    elif LANDX_flat_middle > LANDX_flat_middle: 
        Rot = 20 
    elif X < LANDX_flat_middle:
        Rot = -20 
    
    if abs(VS) > 35: 
        Pow = 4
    
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    
    print Rot, Pow # R P. R is the desired rotation angle. P is the desired thrust power.