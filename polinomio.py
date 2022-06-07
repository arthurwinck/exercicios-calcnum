def polinomio(a, b, c, n, x0, erro):
    b[1] = a[1]
    c[1] = b[1]
    b[n] = 1

    while (abs(b[n]) > erro):
        for i in range(2, n-1):
            b[i] = b[i-1]*x0 + a[i]
            c[i] = c[i-1]*x0 + b[i]

        b[n] = b(n-1)*x0+a(n)
        x0 = x0 - b[n] / c[n-1]

    # Executar mais um já que x0 está uma iteração atrasada? x0 = x0 - b[n] / c[n-1]
    return x0

