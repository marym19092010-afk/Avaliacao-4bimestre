################################################################
# Descrição: Apresentar o resultado inteiro da divisão de dois  #
#            números (quociente) usando laço de repetição,     #
#            sem utilizar o operador aritmético de divisão.    #
# Parâmetros de entrada: Dividendo e divisor                   #
# Valores de saída:      Quociente inteiro da divisão          #
# Autor:Mariane Alessandra Inacio de Souza                     #
################################################################

dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))

if divisor == 0:
    print("Erro: O divisor não pode ser zero.")
else:
    quociente = 0
    acumulado = abs(divisor)
    alvo = abs(dividendo)
    
    while acumulado <= alvo:
        quociente += 1
        acumulado += abs(divisor)
        
    if (dividendo < 0) ^ (divisor < 0):
        quociente = -quociente
        
    print(f"O resultado inteiro da divisão é: {quociente}")
