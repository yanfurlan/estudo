# Definindo as duas matrizes 2x2
matriz1 = [
    [1, 2],
    [3, 4]
]

matriz2 = [
    [5, 6],
    [7, 8]
]

# Inicializando a matriz de resultado
resultado = [
    [0, 0],
    [0, 0]
]

# Somando as matrizes
for i in range(2):
    for j in range(2):
        resultado[i][j] = matriz1[i][j] + matriz2[i][j]

# Exibindo a matriz resultante
print("A soma das duas matrizes é:")
for linha in resultado:
    print(linha)
