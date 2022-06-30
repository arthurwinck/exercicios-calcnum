# Eliminação de gauss com troca física de linhas

def gauss_pivo_com(matriz: list, b: list):
    x = [0]*len(matriz)
    
    # Pivotamento -----------------------

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
    

        for l in range(j+1, len(matriz)):
            mult = matriz[l][j]/matriz[j][j]
            for k in range(len(matriz[0])):
                matriz[l][k] = matriz[l][k] - mult*matriz[j][k]
                
            b[l] = b[l] - mult*b[j]


    # Retrosubstituição ---------------------------

    x[-1] = b[-1]/matriz[-1][-1]

    for i in range(len(matriz) - 2, -1, -1):
        soma = 0
        for j in range(i+1, len(matriz)):
            soma += matriz[i][j]*x[j]

        x[i] = (b[i] - soma)/matriz[i][i]

    # Resíduo -----------------------
    r = [0]*len(matriz)

    for c in range(len(matriz)):
        soma = 0
        for v in range(len(matriz)):
            soma += matriz[c][v]*x[v]

        r[c] = b[c] - soma

    print(f"Matriz A: {matriz}")
    print(f"Vetor B: {b}")
    print(f"Vetor X: {x}")
    print(f"Resíduo: {r}")


#gauss_pivo_com([[-0.421, 0.784 ,0.279], [0.448, 0.832 ,0.193], [0.421, 0.784, 0.207]], [0, 1, 0])
#gauss_pivo_com([[4, 2, 3], [2, -4, -1], [-1, 1, 4]], [7, 1, -5])
gauss_pivo_com([[3, 4, 3], [1, 5, -1], [6, 3, 7]], [10, 7, 15])
