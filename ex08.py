################################################################
# Descrição: Ler 15 elementos reais para matriz A. Construir   #
#            matriz B dividindo por 2 os índices pares e       #
#            multiplicando por 1.5 os índices ímpares.         #
# Parâmetros de entrada: 15 valores reais para a matriz A      #
# Valores de saída:      Elementos da matriz B                 #
# Autor:Mariane Alessandra Inacio de Souza                   #
################################################################

matriz_a = []
for i in range(15):
    val = float(input(f"Digite o elemento real {i+1} da matriz A: "))
    matriz_a.append(val)

matriz_b = []
for i, val in enumerate(matriz_a):
    if i % 2 == 0:
        matriz_b.append(val / 2)
    else:
        matriz_b.append(val * 1.5)

print("Elementos da matriz B:")
for i, val in enumerate(matriz_b):
    print(f"B[{i+1}] = {val:.2f}")
