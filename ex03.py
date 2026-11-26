################################################################
# Descrição: Ler sucessivamente valores numéricos enquanto     #
#            forem positivos e apresentar no final o           #
#            somatório, a média e o total de valores lidos.    #
# Parâmetros de entrada: Valores numéricos fornecidos          #
# Valores de saída:      Somatório, média e total de valores     #
# Autor:Mariane Alessandra Inacio de Souza                       #
################################################################

somatorio = 0
total_valores = 0

while True:
    valor = float(input("Digite um valor numérico (negativo para parar): "))
    if valor < 0:
        break
    somatorio += valor
    total_valores += 1

if total_valores > 0:
    media = somatorio / total_valores
    print(f"Total de valores lidos: {total_valores}")
    print(f"Somatório: {somatorio}")
    print(f"Média: {media}")
else:
    print("Nenhum valor positivo foi informado.")
