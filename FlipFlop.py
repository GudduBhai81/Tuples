def palind(r):
    g = len(r) -1
    d = 0
    while(d<g):
        if(r[g]!=r[d]):
            return False
        g-=1
        d+=1
    return True


r = ("NAAN", 1, 2, 3, 3, "HELLO")

if(palind(r)):
    print("The Tuple is Flip-Flop.")
else:
    print("The Tuple is not Flip-Flop.")