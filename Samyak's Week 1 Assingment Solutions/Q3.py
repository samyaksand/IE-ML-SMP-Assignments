
def minimum(a, n):
    
    minpos = a.index(min(a))
    print ("The minimum is at position", minpos + 1 )
    maxpos = a.index(max(a)) 
    print ("The maximum is at position", maxpos + 1 )


arr = [1,2,3,4,5,6,7,8,9,10] 
minimum(arr, len(arr))