import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# N: the total number of nodes in the level, including the gateways
# L: the number of links
# E: the number of exit gateways
N, L, E = [int(i) for i in raw_input().split()]
nodes = []
for i in xrange(L):
    # N1: N1 and N2 defines a link between these nodes
    N1, N2 = [int(i) for i in raw_input().split()]
    nodes.append((N1,N2))
gate = []
for i in xrange(E):
    gate.append(int(raw_input()))
    
#print gate

# game loop
while 1:
    SI = int(raw_input()) # The index of the node on which the Skynet agent is positioned this turn
    
    #if (28, 35) in nodes: 
    #    print "yes"
    
    
    correct_flag = 0 
    
    #if skynet has an immediate path to a gateway, delete that 
    E_SI_flag = 0 
    for E in gate: 
        print >> sys.stderr, (E, SI), type((E, SI)), type((28, 35))
        for i, k in nodes: 
            if E == i and k == SI: 
                print (str(E)+" "+str(SI))
                correct_flag = 1
        for i, k in nodes: 
            if SI == i and k == E: 
                print (str(SI)+" "+str(E))
                correct_flag = 1
    
    #if no immediate path, then just delete any other edge that exists    
    deleted = []
    if correct_flag == 0: 
        for i, k in nodes: 
            if (i, k) not in deleted: 
                print (str(i)+" "+str(k))
                break
    #print "0 1"
        
    
