def fibonacci(n):
   
    if n < 0:
        return "O número deve ser maior ou igual a zero."

    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)

    if n in fib_sequence:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci." 


# Solicita ao usuário um número;
numero = int(input("Informe um número: "))

# Chama a função e imprime o resultado
resultado = fibonacci(numero)
print(resultado)
    