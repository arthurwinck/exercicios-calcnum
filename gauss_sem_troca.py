# Eliminação de gauss com troca física de linhas

def gauss_pivo_com(matriz: list, b: list):
    x = [0]*len(matriz)
    posmap = [i for i in range(len(matriz))]
    
    # Pivotamento -----------------------

    for j in range(len(matriz[0]) - 1):
        maior = matriz[posmap[j]][posmap[j]]
        linha_maior = posmap[j]

        for i in range(len(matriz)):
            if abs(matriz[posmap[posmap[i]]][posmap[j]]) > abs(maior):
                maior = matriz[posmap[i]][posmap[j]]
                linha_maior = posmap[i]

        if linha_maior != 0:
            posmap[linha_maior], posmap[j] = posmap[j], posmap[linha_maior]

        for l in range(j+1, len(matriz)):
            mult = matriz[posmap[l]][posmap[j]]/matriz[posmap[j]][posmap[j]]
            for k in range(len(matriz[0])):
                matriz[posmap[l]][posmap[k]] = matriz[posmap[l]][posmap[k]] - mult*matriz[posmap[j]][posmap[k]]
                
            b[posmap[l]] = b[posmap[l]] - mult*b[posmap[j]]


    # Retrosubstituição ---------------------------

    x[-1] = b[-1]/matriz[-1][-1]

    for i in range(len(matriz) - 2, -1, -1):
        soma = 0
        for j in range(i+1, len(matriz)):
            soma += matriz[posmap[i]][posmap[j]]*x[posmap[j]]

        x[posmap[i]] = (b[posmap[i]] - soma)/matriz[posmap[i]][posmap[i]]


    # Resíduo -----------------------
    r = [0]*len(matriz)

    for c in range(len(matriz)):
        soma = 0
        for v in range(len(matriz)):
            soma += matriz[posmap[c]][v]*x[v]

        r[posmap[c]] = b[posmap[c]] - soma


    print(f"Matriz A: {matriz}")
    print(f"Vetor B: {b}")
    print(f"Vetor X: {x}")
    print(f"Vetor Resíduo: {r}")

gauss_pivo_com([[-0.421, 0.784 ,0.279], [0.448, 0.832 ,0.193], [0.421, 0.784, 0.207]], [0, 1, 0])
#gauss_pivo_com([[4, 2, 3], [2, -4, -1], [-1, 1, 4]], [7, 1, -5])