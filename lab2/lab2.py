import numpy as np

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

#find kth and mean with kth +1
def findKthAndMean(A, i, j, k): #smalest
    return (findKth(A, i, j, k) + findKth(A, i, j, k+1))/2


def medRand(A, start, end):
    mid = (end - start)//2 + start
    if((end - start)%2 == 0):   # odd number of elements
        return findKth(A, start, end, mid+1)/1
    else:
        return (findKth(A, start, end, mid+1) + findKth(A, start, end, mid+2))/2




        
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


#ele may not be in list
def partitionElement(A, start, end, pivot):
    # returns index of partition after partitioning
    x = start
    for y in range(start, end+1):
        if A[y] < pivot:
            swap(A, x, y)
            x = x + 1
    return x


def medFast(A, i, j, k):
    n = (j-i+1)//k +1            # num of groups
    M = np.empty([n])              # new array for medians


    if(i==j):
        return A[i]

    
    for x in range(n-1):
        insertionSort(A, i+k*x, i+k*(x+1)-1) 
        M[x] = A[k//2+k*x]

    insertionSort(A, j-j%k, j)  # Sort the last group seperatly since it may be uneven
    M[n-1] = A[(j%k)//2+j-j%k]/1  #if (j%k)%2==0 else (A[(j%k)//2+j-j%k]+ A[(j%k)//2+j-j%k+1])/2
    if(n==1):
        return M[0]
    
    
    pivot = medFast(M, 0, n-1, k)        

    #partition
    x = partitionElement(A, i, j, pivot)


    mid=(j-i)//2+i
    if((j - i)%2 == 0):   # odd number of elements
        if (mid < x):
            return findKth(A, i, x-1, mid+1)/1
        else:
            return findKth(A, x, j, mid+1)/1 #now includes x in upper range
    else:
        if (mid < x):
            return findKthAndMean(A, i, x-1, mid+1)
        else:
            return findKthAndMean(A, x, j, mid+1)
    

def main():
    MAX = 10000
    n = 120
    
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
    
    
    print("Fast3: ", medFast(D, 0, n-1, 3))
    #print("Fast5: ", medFast(E, 0, n-1, 5))
    #print("Fast7: ", medFast(F, 0, n-1, 7))



if __name__ == "__main__":
    main()
