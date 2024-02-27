def solution(l):
    # Your code here
    n = len(l)
    lucky_triples_no = 0
    
    for y in range(1,n-1):
        x_count = 0
        # before y
        for x in range(y):
            if l[y]%l[x] == 0:
                x_count+=1
        # after y
        z_count = 0
        for z in range(y+1,n):
            if l[z]%l[y] == 0:
                z_count+=1
        
        lucky_triples_no += x_count*z_count
    
    return lucky_triples_no
