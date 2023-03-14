def fibonacci(n):
    # Casos base
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Caso geral
    a = 0
    b = 1
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
        if c == n:
            return True
    
    return False


# Exemplo de uso
num = int(input("Digite um número: "))
if fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
