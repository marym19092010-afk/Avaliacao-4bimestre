################################################################
# Descrição: Ler vetor A com 20 inteiros e construir vetor B   #
#            onde cada elemento é o somatório de 1 até o       #
#            valor correspondente armazenado em A.             #
# Parâmetros de entrada: 20 valores inteiros para a matriz A   #
# Valores de saída:      Elementos da matriz B                 #
# Autor:Mariane Alessandra Inacio de Souza                     #
################################################################

matriz_a = []
for i in range(20):
    val = int(input(f"Digite o elemento inteiro {i+1} da matriz A: "))
    matriz_a.append(val)

matriz_b = []
for val in matriz_a:
    somatorio = 0
    for j in range(1, val + 1):
        somatorio += j
    matriz_b.append(somatorio)

print("Elementos da matriz B:")
for i, val in enumerate(matriz_b):
    print(f"B[{i+1}] = {val}")
