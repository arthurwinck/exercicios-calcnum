def gauss_pivo_sem(self):
    a1 = int
    b1 = int
    x = int
    r = abs(b1 - a1*x)

#Retrosubstituição

x[n]= y[n]/U[n][n]
for i in range(i, n-1):
    soma = 0
    for j in range(i+1, n):
        soma += U[i][j]*x[j]
    x[i] = (y[i]-soma)/U[i][i]

#Decomposição LU - Método de Crout - Revisar indices -> 1 para -> 0
def LUCrout(a: list, b: list):
    n = len(b)

    L = []
    U = []
    y = []

    for k in range(n):
        for i in range(k, n):
            soma = 0
            for r in range(1, k-1):
                soma += L[i][r]*U[r][k]

            L[i][k] = a[i][k] - soma

        U[k][k] = 1

        for j in range(k+1, n):
            soma = 0
            for r in range(1, k-1):
                soma += L[k][r]*U[r][j]
            
            U[k][j] = (a[k][j] - soma)/L[k][k]

    y[1] = b[1]/L[1][1]
    for i in range(2, n):
        soma = 0
        for j in range(0, j-1):
            soma += L[i][j]*y[j]
        
        y[i] = (b[i] - soma)/L[i][i]

LUCrout([[4,2,3], [2, -4 ,1], [-1, 1, 4]], [7, 1, 5])