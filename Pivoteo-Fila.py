def PIVOTEO (A,b):
    n = len(A)
    s=[]
    m=0
    for i in range (n):
        s.append (max (A[i]))
    for k in range (n-1):
        for i in range(n-1):
            for j in range(m,n-1):
                if (abs(A[j][k])/s[j])<(abs(A[j+1][k])/s[j+1]):
                    Atemp=A[j+1]
                    stemp=s[j+1]
                    btemp=b[j+1]
                    A[j+1]=A[j]
                    s[j+1]=s[j]
                    b[j+1]=b[j]
                    A[j]=Atemp
                    s[j]=stemp
                    b[j]=btemp
        m+=1
    return A,b


A = [[3,-2,-1,-1],[2,-1,2,1],[5,-2,-2,-1],[1,1,2,5]]
b = [-6,17,-14,12]

PIVOTEO(A,b)

# =============================================================================
# A = [[1,-2,9,-1],[3,6,3,2],[2,3,-2,3],[4,-5,7,1]]
# b = [18.0, 2.0, 7.0, 9.0]
# =============================================================================
