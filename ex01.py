################################################################
# Descrição: Elaborar um programa que apresente os resultados  #
#            das potências do valor de base 3, elevado a um    #
#            expoente que varie do valor 0 até o valor 15.     #
# Parâmetros de entrada: Nenhum (expoente varia de 0 a 15)     #
# Valores de saída:      As potências de 3 de 0 a 15             #
# Autor:Mariane Alessandra inacio de Souza                       #
################################################################

potencia = 1
for expoente in range(16):
    print(f"3 elevado a {expoente} = {potencia}")
    if expoente < 15:
        proxima = 0
        for _ in range(3):
            proxima += potencia
        potencia = proxima
