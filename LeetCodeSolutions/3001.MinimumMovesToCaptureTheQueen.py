class Solution:
    def minMovesToCaptureTheQueen(self, a, b, c, d, e, f):
        if abs(c - e) == abs(d - f):
            vert = 1 if (c < e) else -1
            horz = 1 if (d < f) else -1
           
            while(c != e and d != f):
                c += vert
                d += horz
                if(c == a and d == b): 
                    return 2
            return 1

        
        if a == e:
            horz = 1 if (b < f) else -1
            
            while(b != f):
                b += horz
                if((a == c) and (b == d)): 
                    return 2

            return 1

        
        if b == f:
            vert = 1 if (a < e) else -1
            
            while(a != e):
                a += vert
                if((a == c) and (b == d)): 
                    return 2
            return 1

        return 2