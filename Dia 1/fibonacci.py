def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    return fib_sequence[:n]

# Teste
print(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
