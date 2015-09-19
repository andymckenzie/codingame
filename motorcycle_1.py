import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

road = int(raw_input()) # the length of the road before the gap.
gap = int(raw_input()) # the length of the gap.
platform = int(raw_input()) # the length of the landing platform.

JUMP_FLAG = False

# game loop
while 1:
    speed = int(raw_input()) # the motorbike's speed.
    coord_x = int(raw_input()) # the position on the road of the motorbike.
    
    
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    
    print >> sys.stderr, str(coord_x)
    
    print >> sys.stderr, str(road)

    print >> sys.stderr, str(JUMP_FLAG)

    
    # A single line containing one of 4 keywords: SPEED, SLOW, JUMP, WAIT.
    
    #LOGIC
    
    if JUMP_FLAG is False:
        if(abs(coord_x - road) < 4): 
            JUMP_FLAG = True
            print "JUMP" 
        else if 
        else:  
            print "SPEED"
    if JUMP_FLAG is True: 
        print "SLOW"

