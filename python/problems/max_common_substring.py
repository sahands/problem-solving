import pprint;

def max_common_substring(x,y):
    n = len(x);
    m = len(y);
    
    t = [[0 for j in xrange(m)] for i in xrange(n)];
    
    max_val = 0;
    max_index = (0,0);
    
    for i in xrange(1,n):
        for j in xrange(1,m):
            if x[i-1]==y[j-1]:
                t[i][j]= 1 + t[i-1][j-1];
                if t[i][j] > max_val:
                    max_val = t[i][j];
                    max_index = (i-max_val,j-max_val);
            else:
                t[i][j]= 0;
                
    #pprint.pprint(t);
    
    return (max_val, max_index);
    
    
    
if __name__=="__main__":
    (x,y) = ("abcdefeeeeasdf","aeeebcdeeeasdf");
    (l,(i,j)) = max_common_substring(x,y);
    
    print l, i, j;
    print x[i:i+l];
    print y[j:j+l];
    