import numpy as np



def swap0(A, i, j):
    if(i!=j):
        A[i] = A[i]+A[j]
        A[j] = A[i]-A[j]
        A[i] = A[i]-A[j]

def swap(A, i, j):
    if(i!=j):
        t = A[i]
        A[i] = A[j]
        A[j] = t
        
def partition(A, i, j, p):
    pivot = A[p]
    swap(A, p, j)#swap to end
    x = i
    for y in range(i, j):
        if A[y] < pivot:
            swap(A, x, y)
            x = x + 1
    if A[j] < A[x]:
        swap(A, j, x)
    return x

def quicksort(A, i, j):
    if i<j:
        s = partition(A, i, j, j)
        quicksort(A, i, s-1)
        quicksort(A, s+1, j)
        
def medSort(A, i, j):
    quicksort(A, i, j)
    return A[(j-i)//2 +i] if (j-i)%2==0 else (A[(j-i)//2 +i]+ A[(j-i)//2 +i +1])/2

def findKth(A, i, j, k): #smalest
    x = partition(A, i, j, (j-i)//2+i)#rand ele??
    if k==x+1:
        return A[x]
    elif (k <= x):
        return findKth(A, i, x-1, k)
    else:
        return findKth(A, x+1, j, k)


def findKth_LUKE(A, start, end, k):  # kth smallest number (indexing at 0)
    x = partition(A, start, end, (end-start)//2 + start)
    if k==x:
        return A[x]
    elif (k < x):
        return findKth(A, start, x-1, k)
    else: 
        return findKth(A, x+1, end, k-x-1)
    
def medRand(A, start, end):
    mid = (end - start)//2 + start


    if((end - start)%2 == 0):   # odd number of elements
        return findKth(A, start, end, mid+1)
    else:
        return (findKth(A, start, end, mid+1) + findKth(A, start, end, mid+2))/2
    
def insertionSort_SLOW(A, start, end):
    k=start
    while k<(end-start+1):
        l=k
        while l>start and A[l-1]>A[l]: 
            swap(A, l, l-1)
            l-=1
        k+=1
        
def insertionSort(A, i, j):
    k=1
    while k<(j-i+1):
        m=A[k]
        l=k-1
        while l>=i and A[l]>m: 
            A[l+1] = A[l]
            l-=1
        A[l+1]=m
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




def medFast(A, i, j, k):
    n = (j-i+1)//k +1            # num of groups
    M = np.empty([n])              # new array for medians

    for x in range(n-1):
        insertionSort(A, i+k*x, i+k*(x+1)-1) 
        M[x] = A[k//2+k*x]

    insertionSort(A, j-j%k, j)  # Sort the last group seperatly since it may be uneven
    M[n-1] = A[(j%k)//2+j-j%k]/1  #if (j%k)%2==0 else (A[(j%k)//2+j-j%k]+ A[(j%k)//2+j-j%k+1])/2

    insertionSort(M, 0, n-1)   # TODO: JOHN, is this right??? No?
        

    split = partition(A, i, j, M[ n//2 ] )

    if split == n//2 or split == n//2 + 1 or split == n//2 - 1:
        return A[split]
    elif split > (j-i + 1)//2:  # Go left
        #return medRand(A, split, j)
        return medFast(A, split, j, k)
    else:
        #return medRand(A, i, split)
        return medFast(A, i, split, k)

    
    #return M[0] if n<=1 else medFast(M, 0, n-1, k) 

#######partiont was broken
#was built not to take in a pivot
#modifyed to take in a pivot
#behaved perfectly (only if the passed in pivot was at index n-1)
#lol fixed

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

def main():
    MAX = 1000
    n = 1234
    
    #A = np.asarray(range(n))
    
    A = np.random.randint(MAX, size=n)
    #A = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    #np.random.shuffle(A)
    assert( len(A) == n)
    B = list(A)
    C = list(A)
    D = list(A)
    E = list(A)
    F = list(A)
    I = list(A)
    
    print(A)
    insertionSort(F, 0, len(F)-1)

    
    
    print("NP: ",np.median(A))
    
    print("Sort:  ", medSort(B,0,n-1))
    print("Rand:  ", medRand(C, 0, n-1))
    A.sort()
    insertionSort(I, 0, n-1)
    print("SORTED: ", 0==sum([abs(A[i]-B[i]) for i in range(n)]))
    print("ISORTED: ", 0==sum([abs(A[i]-I[i]) for i in range(n)]))
    C.sort()
    print("RAND SAME ELE: ", 0==sum([abs(A[i]-C[i]) for i in range(n)]))
    
    print("Big kth: ", kthTestingArr(A))
    
    #print("Fast3: ", medFast(D, 0, n-1, 3))
    #print("Fast5: ", medFast(E, 0, n-1, 5))
    #print("Fast7: ", medFast(F, 0, n-1, 7))

    kthTesting(100)
    IST(500)


if __name__ == "__main__":
    main()
