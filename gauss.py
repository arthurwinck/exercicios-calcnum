def gauss_pivo_sem(matriz: list, b: list):
    x = [0]*len(matriz)
    
    
    for j in range(len(matriz[0]) - 1):
        maior = matriz[j][j]
        linha_maior = j

        for i in range(len(matriz)):
            if abs(matriz[i][j]) > abs(maior):
                maior = matriz[i][j]
                linha_maior = i

        if linha_maior != 0:
            temp = matriz[linha_maior]
            matriz[linha_maior] = matriz[j]
            matriz[j] = temp

            temp = b[linha_maior]
            b[linha_maior] = b[j]
            b[j] = temp
    
        #print(matriz)

        for l in range(j+1, len(matriz)):
            mult = matriz[l][j]/matriz[j][j]
            for k in range(len(matriz[0])):
                #print(f"{matriz[l][k]} = {matriz[l][k]} - {mult*matriz[l][j]}")
                matriz[l][k] = matriz[l][k] - mult*matriz[j][k]
                
            b[l] = b[l] - mult*b[l]


    print(matriz)
    print(b)

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