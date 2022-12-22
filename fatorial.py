def fatorial(n):
    numero = 1
    i = 1
    while i <= n :
        numero *= i 
        i += 1
    return numero

print(fatorial(5))

def calcula_euler(x,n):
    i = 1
    soma = 0
    while i < n :
        soma += (x**i)/fatorial(i)
        i += 1
    return soma + 1 