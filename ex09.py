################################################################
# Descrição: Ler matriz A (12 valores divisíveis por 2 ou 3) e  #
#            matriz B (12 valores não múltiplos de 5) com      #
#            validação. Construir matriz C com a junção.       #
# Parâmetros de entrada: Valores numéricos para preencher A e B#
# Valores de saída:      Elementos da matriz C (24 elementos)  #
# Autor:Mariane alessandra Inacio de Souza                     #
################################################################

matriz_a = []
print("Preenchendo a Matriz A (apenas valores divisíveis por 2 ou 3):")
while len(matriz_a) < 12:
    val = int(input(f"Digite o {len(matriz_a)+1}º valor para A: "))
    if val % 2 == 0 or val % 3 == 0:
        matriz_a.append(val)
    else:
        print("Valor inválido! Deve ser divisível por 2 ou 3.")

matriz_b = []
print("\nPreenchendo a Matriz B (apenas valores que não sejam múltiplos de 5):")
while len(matriz_b) < 12:
    val = int(input(f"Digite o {len(matriz_b)+1}º valor para B: "))
    if val % 5 != 0:
        matriz_b.append(val)
    else:
        print("Valor inválido! Não pode ser múltiplo de 5.")

matriz_c = matriz_a + matriz_b

print("\nElementos da Matriz C (junção de A e B):")
for i, val in enumerate(matriz_c):
    print(f"C[{i+1}] = {val}")
