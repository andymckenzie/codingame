import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# game loop
while 1:
    SX, SY = [int(i) for i in raw_input().split()]
    MH_list = []
    for i in xrange(8):
        MH = int(raw_input()) # represents the height of one mountain, from 9 to 0. Mountain heights are provided from left to right.
        MH_list.append(MH)
    
    max_height_index = MH_list.index(max(MH_list))
    if SX == max_height_index:
        print "FIRE"
    else: 
        print "HOLD"
    
    
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    
    #print "HOLD" # either:  FIRE (ship is firing its phase cannons) or HOLD (ship is not firing).