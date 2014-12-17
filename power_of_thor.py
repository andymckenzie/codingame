import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# LX: the X position of the light of power
# LY: the Y position of the light of power
# TX: Thor's starting X position
# TY: Thor's starting Y position
LX, LY, TX, TY = [int(i) for i in raw_input().split()]

# game loop
while 1:
    E = int(raw_input()) # The level of Thor's remaining energy, representing the number of moves he can still make.
    
    if 'dX' not in vars(): 
        dX = LX - TX 
    if 'dY' not in vars(): 
        dY = LY - TY

    #print dX, dY
    
    if abs(dX) == abs(dY): 
        #print dX, dY
        if dX < 0 and dY < 0: 
            print "NW" 
        if dX < 0 and dY > 0: 
            print "SW" 
        if dX > 0 and dY < 0: 
            print "NE" 
        if dX > 0 and dY > 0: 
            print "SE"
    if abs(dX) > abs(dY): 
        if dX < 0:
            print "W"
            dX += 1
        if dX > 0: 
            print "E"
            dX -= 1
    if abs(dX) < abs(dY): 
        if dY > 0: 
            print "S"
            dY = dY - 1
        if dY < 0: 
            print "N"
            dY = dY + 1

        
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    
    #print "SE" # A single line providing the move to be made: N NE E SE S SW W or NW