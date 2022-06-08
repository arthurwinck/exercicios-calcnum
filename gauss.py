def gauss_pivo_sem(matriz: list, b: list):
    x = [0]*len(matriz)
    matriz = pivotacao(matriz)
    

def pivotacao(matriz):
    for j in range(len(matriz[0])):
        zeros = 0
        lista_col = []
        for i in range(len(matriz)):
            if matriz[i][j] == 0:
                zeros += 1
            lista_col.append(matriz[i][j])

        if zeros < len(matriz) - 1:
            pos_pivo = lista_col.index(max(lista_col))

            if pos_pivo[0] != 0:
                temp = matriz[pos_pivo]
                matriz[pos_pivo] = matriz[0]
                matriz[0] = temp

    return matriz

#Retrosubstituição

# x[n]= y[n]/U[n][n]
# for i in range(i, n-1):
#     soma = 0
#     for j in range(i+1, n):
#         soma += U[i][j]*x[j]
#     x[i] = (y[i]-soma)/U[i][i]

# #Decomposição LU - Método de Crout - Revisar indices -> 1 para -> 0
# def LUCrout(a: list, b: list):
#     n = len(b)

#     L = []
#     U = []
#     y = []

#     for k in range(n):
#         for i in range(k, n):
#             soma = 0
#             for r in range(1, k-1):
#                 soma += L[i][r]*U[r][k]

#             L[i][k] = a[i][k] - soma

#         U[k][k] = 1

#         for j in range(k+1, n):
#             soma = 0
#             for r in range(1, k-1):
#                 soma += L[k][r]*U[r][j]
            
#             U[k][j] = (a[k][j] - soma)/L[k][k]

#     y[1] = b[1]/L[1][1]
#     for i in range(2, n):
#         soma = 0
#         for j in range(0, j-1):
#             soma += L[i][j]*y[j]
        
#         y[i] = (b[i] - soma)/L[i][i]

gauss_pivo_sem([[-0.421, 0.784 ,0.279], [0.448, 0.832 ,0.193], [0.421, 0.784, 0.207]], [0, 1, 0])