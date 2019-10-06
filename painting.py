color = [[12,23,14],[10,30,15],[16,22,35],[14,24,20]]

def find_buckets(A):
    num_of_shades = 3
    minimum_wastage = float("inf")
    I,J,K,L = -1,-1,-1,-1
    for i in range (num_of_shades):
        for j in range (num_of_shades):
            for k in range (num_of_shades):
                for l in range (num_of_shades):
                    total_amount = color[0][i] + color[1][j] + color[2][k] + color[3][l]
                    wastage = total_amount - A
                    if(wastage < 0):
                        continue
                    elif(wastage < minimum_wastage):
                        minimum_wastage = wastage
                        I,J,K,L = i,j,k,l

    if(I>-1 and J>-1 and K>-1 and L>-1):
        print("minimum_wastage for the area {:d} is {:.0f}".format(A, minimum_wastage))
        print("relevent indices are [(0,{:d}), (1,{:d}), (2,{:d}), (3,{:d})] \n".format(I,J,K,L))
    else:
        print("Sorry!!! Amount of paints are not enough for paint the whole area")
        
                        
find_buckets(100)
find_buckets(90)
