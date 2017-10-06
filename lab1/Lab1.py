import numpy as np
RANGE = 100

def randMatr(n):
    return np.random.randint(-RANGE,RANGE,size=(n,n))

def multIter(n, A, B):
    """
    Goes through two arrays and preforms Matric Multiplication
    in an iterative way.
    """
    N=range(n)
    C = [[0 for i in N] for j in N] # Generates the return array
    for i in N:
        for j in N:
            for s in N:
                C[i][j] += A[i][s]*B[s][j] # Do the monster math
    return C


def sum(n, A, B):
    """
    Computes the sum of the arrays
    """
    return [ [ A[j][i]+B[j][i] for i in range(n) ] for j in range(n) ]
    
def multDC(n, Ax, Ay, Bx, By, A, B):
    if(n==1):
        #print(A[Ay[0]][Ax[0]]*B[By[0]][Bx[0]])
        #print(n, Ax, Ay, Bx, By)
        return [[A[Ay[0]][Ax[0]]*B[By[0]][Bx[0]]]]
    
    
    A_L = (Ax[0],Ax[0] + (Ax[1]-Ax[0])//2)
    A_R = (Ax[0] + (Ax[1]-Ax[0])//2, Ax[1])
    A_T = (Ay[0],Ay[0] + (Ay[1]-Ay[0])//2)
    A_B = (Ay[0]+(Ay[1]-Ay[0])//2, Ay[1])

    B_L = (Bx[0],Bx[0] + (Bx[1]-Bx[0])//2)
    B_R = (Bx[0] + (Bx[1]-Bx[0])//2, Bx[1])
    B_T = (By[0],By[0] + (By[1]-By[0])//2)
    B_B = (By[0]+(By[1]-By[0])//2, By[1])


    
    XP = multDC(n//2, A_L, A_T, B_L, B_T, A, B)
    XQ = multDC(n//2, A_L, A_T, B_R, B_T, A, B) 
    YR = multDC(n//2, A_R, A_T, B_L, B_B, A, B)
    YS = multDC(n//2, A_R, A_T, B_R, B_B, A, B)
    
    ZP = multDC(n//2, A_L, A_B, B_L, B_T, A, B)
    ZQ = multDC(n//2, A_L, A_B, B_R, B_T, A, B)
    WR = multDC(n//2, A_R, A_B, B_L, B_B, A, B)
    WS = multDC(n//2, A_R, A_B, B_R, B_B, A, B)

    C = sum(n//2, XP, YR)        # Calculate TopLeft matrix
    #print(C)
    TR = sum(n//2, XQ, YS)       # Find the other 3 results
    BL = sum(n//2, ZP, WR)
    BR = sum(n//2, ZQ, WS)
    
    #C = C + BL
    C.extend(BL)                # Generate Left of Array
    #print(C)
    
    for y in range(n//2):                # Append TopRight to output Matrix C
        #C[y] = C[y]+TR[y] 
        C[y].extend(TR[y] )
    
    for y in range(n//2):                # Append Bottom
        #C[y] = C[y]+BR[y]
        C[y+n//2].extend(BR[y])
    
    #print(C)
    return C  


def dif(n, A, B):
    """
    Computes the dif of the arrays
    """
    return [ [ A[j][i]-B[j][i] for i in range(n) ] for j in range(n) ]

def sumRange(Ax, Ay, Bx, By, A, B):
    """
    Computes the sum of the arrays
    """
    return [ [ A[j][i]+B[l][k] for i,k in zip(range(*Ax),range(*Bx))] for j,l in zip(range(*Ay),range(*By))]

def difRange(Ax, Ay, Bx, By, A, B):
    """
    Computes difference of specific ranges in the arrays
    """
    return [ [A[j][i]-B[l][k] for i,k in zip(range(*Ax),range(*Bx)) ] for j,l in zip(range(*Ay),range(*By)) ]

def multStrassen(n, Ax, Ay, Bx, By, A, B):
    if(n==1):
        return [[A[Ay[0]][Ax[0]]*B[By[0]][Bx[0]]]]

    # A = [[ X, Y],       B = [[ P, Q],
    #      [ Z, W]]            [ R, S]]

    
    A_L = (Ax[0],Ax[0] + (Ax[1]-Ax[0])//2)
    A_R = (Ax[0] + (Ax[1]-Ax[0])//2, Ax[1])
    A_T = (Ay[0],Ay[0] + (Ay[1]-Ay[0])//2)
    A_B = (Ay[0]+(Ay[1]-Ay[0])//2, Ay[1])

    B_L = (Bx[0],Bx[0] + (Bx[1]-Bx[0])//2)
    B_R = (Bx[0] + (Bx[1]-Bx[0])//2, Bx[1])
    B_T = (By[0],By[0] + (By[1]-By[0])//2)
    B_B = (By[0]+(By[1]-By[0])//2, By[1])
    
    N = (0,n//2)

    # p1 = X(Q-S)
    p1 = multStrassen(n//2, A_L, A_T, N, N, A, difRange(B_R, B_T, B_R, B_B, B, B))
    # p2 = (X+Y)S
    p2 = multStrassen(n//2, N, N, B_R, B_B, sumRange(A_L, A_T, A_R, A_T, A, A), B) 
    # p3= (Z+W)P
    p3 = multStrassen(n//2, N, N, B_L, B_T, sumRange(A_L, A_B, A_R, A_B, A, A), B)
    # p4 = W(R-P)
    p4 = multStrassen(n//2, A_R, A_B, N, N, A, difRange(B_L, B_B, B_L, B_T, B, B))
    # p5 = (X+W)(P+S)
    p5 = multStrassen(n//2, N, N, N, N, sumRange(A_L, A_T, A_R, A_B, A, A), sumRange(B_L, B_T, B_R, B_B, B, B))
   #  p6 = (Y-W)(R+S)
    p6 = multStrassen(n//2, N, N, N, N, difRange(A_R, A_T, A_R, A_B, A, A), sumRange(B_L, B_B, B_R, B_B, B, B))
    # p7 = (X-Z)(P+Q)
    p7 = multStrassen(n//2, N, N, N, N, difRange(A_L, A_T, A_L, A_B, A, A), sumRange(B_L, B_T, B_R, B_T, B, B))


    
    C = sum(n//2,p4,sum(n//2,p5,dif(n//2,p6,p2)))        # Calculate TopLeft matrix
    
    TR = sum(n//2, p1, p2)       # Find the other 3 results
    BL = sum(n//2, p3, p4)
    BR = sum(n//2,p1,dif(n//2,dif(n//2,p5,p3), p7))
    
    C.extend(BL)                # Generate Left of Array
        
    for y in range(n//2):                # Append TopRight to output Matrix C
        C[y].extend(TR[y] )
    
    for y in range(n//2):                # Append Bottom
        C[y+n//2].extend(BR[y])
    

    return C    
     

    
    
    
    
    
    
def main():   
    n = 128
    A = randMatr(n)
    B = randMatr(n)
    #A = np.asarray([[1,2],[3,4]])
    #B = np.asarray([[1,0],[0,1]])
    #A = np.asarray([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
    #B = np.asarray([ [1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1] ] )
    #B = np.asarray([ [0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0] ] )
        
    C0 = A.dot(B)
    C1 = multIter(n, A, B)
    N = range(n)
    C2 = multDC(n,(0,n), (0,n), (0,n), (0,n), A, B)
    C3 = multStrassen(n,(0,n), (0,n), (0,n), (0,n), A, B)
    #print(C0)
    #print(np.asarray(C1))
    #print(np.asarray(C2))
    #print(np.asarray(C3))
    print(np.array_equal(C0, C1))
    print(np.array_equal(C0, C2))
    print(np.array_equal(C0, C3))

if __name__ == "__main__":
    main()
