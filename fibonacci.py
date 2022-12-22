def calcula_fibonacci(n):
    l = [0]*n
    l[0] = 1
    l[1] = 1
    for i in range(2,n):
        l[i] = l[i-1] + l[i-2]
    return l 

print(calcula_fibonacci(6))