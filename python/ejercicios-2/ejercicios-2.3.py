# Escribir un programa especifico que calcule la serie de Fibonacci hasta un numero especifico.

def fibonacci(num):
    a,b = 0,1
    fibonacci_lista = [0]
    for i in range(num):
        if b > num: return fibonacci_lista
        else:
            fibonacci_lista.append(b)
            a,b = b,a+b

resultado = fibonacci(20)
print(resultado)