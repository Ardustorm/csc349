import numpy as np

def swap0(A, i, j):
    if(i!=j):
        A[i] = A[i]+A[j]
        A[j] = A[i]-A[j]
        A[i] = A[i]-A[j]


def findKth_LUKE(A, start, end, k):  # kth smallest number (indexing at 0)
    x = partition(A, start, end, (end-start)//2 + start)
    if k==x:
        return A[x]
    elif (k < x):
        return findKth(A, start, x-1, k)
    else: 
        return findKth(A, x+1, end, k-x-1)



def insertionSort_SLOW(A, start, end):
    k=start
    while k<(end-start+1):
        l=k
        while l>start and A[l-1]>A[l]: 
            swap(A, l, l-1)
            l-=1
        k+=1


def breakFast__BROKEN(A, i, j, k):
    n = (j-i+1)//k +1            # num of groups
    M = np.empty([n])              # new array for medians

    for x in range(n-1):
        insertionSort(A, i+k*x, i+k*(x+1)-1) 
        M[x] = A[k//2+k*x]

    insertionSort(A, j-j%k, j)
    M[n-1] = A[(j%k)//2+j-j%k]/1  #if (j%k)%2==0 else (A[(j%k)//2+j-j%k]+ A[(j%k)//2+j-j%k+1])/2
        
    return M[0] if n<=1 else medFast(M, 0, n-1, k) 



def kthTesting(n):
    Z = list(range(n,0,-1))
    #Z = list(range(0,n))
    #print(Z)
    all = True
    for i in range(1,n+1):
        X=list(Z)
        k = findKth(X, 0, n-1, i)
        #print("K: ", k)
        #print(X)
        quicksort(X, 0,n-1)
        #print("kth:", X[i-1]==k)
        if(X[i-1]!=k):
            all = False
    print("All Kth: ", all)
    
def kthTestingArr(A):
    B = list(A)
    B.sort()
    n = len(A)
    all = True
    for i in range(1,n+1):
        C=list(A)
        k = findKth(C, 0, n-1, i)
        #print("K: ", k)
        #print(C)
        #print("kth:", B[i-1]==k)
        if(B[i-1]!=k):
            all = False
    return all

def IST(n):
    A = list(range(n,0,-1))
    #print(A)
    I=list(A)
    insertionSort(I, 0, n-1)
    #print(I)
    quicksort(A, 0,n-1)
    print("SortISF: ", 0==sum([abs(A[i]-I[i]) for i in range(n)]))