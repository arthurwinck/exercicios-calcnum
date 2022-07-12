a = [[1, 2, 1][3, 2 ,1][4, 1, 2]]

n = len(a[0])

c1 = 0
c2 = 0

s = [0]*len(a)

for i in range(n):
    s[i] = 0
    for j in range(n):
        # Pega apenas os elementos que não estão na diagonal
        # principal

        if i != j:
            # Realiza o somatório de todos os elementos 
            s[i] = s[i] + abs(a[i][j])