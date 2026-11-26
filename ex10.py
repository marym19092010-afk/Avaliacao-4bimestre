################################################################
# Descrição: Ler matriz A com 10 elementos inteiros e          #
#            apresentar o total de elementos ímpares e o       #
#            percentual em relação ao total de elementos.      #
# Parâmetros de entrada: 10 valores inteiros para a matriz A   #
# Valores de saída:      Total de ímpares e percentual         #
# Autor:Mariane Alessandra inacio de Souza                     #
################################################################

matriz_a = []
for i in range(10):
    val = int(input(f"Digite o elemento inteiro {i+1} da matriz A: "))
    matriz_a.append(val)

tot_impares = 0
for val in matriz_a:
    if val % 2 != 0:
        tot_impares += 1

percentual = (tot_impares / len(matriz_a)) * 100

print(f"Total de elementos ímpares: {tot_impares}")
print(f"Percentual de números ímpares: {percentual:.2f}%")
