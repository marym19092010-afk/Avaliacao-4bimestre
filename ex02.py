################################################################
# Descrição: Escrever um programa que calcule e apresente o    #
#            somatório do número de grãos de trigo que se pode #
#            obter num tabuleiro de xadrez (1 no primeiro      #
#            quadro e o dobro nos seguintes até o 64º).        #
# Parâmetros de entrada: Nenhum                                #
# Valores de saída:      O somatório total de grãos de trigo     #
# Autor:Mariane Alessandra Inacio de Souza                       #
################################################################

graos_quadro = 1
somatorio_total = 0

for quadro in range(1, 65):
    somatorio_total += graos_quadro
    if quadro < 64:
        graos_quadro += graos_quadro

print(f"O somatório total de grãos de trigo no tabuleiro é: {somatorio_total}")
```[cite: 2]
