# identação de blocos

def sacar(valor):
    saldo = 500

    if saldo >= valor: 
        print("Valor válido")
        print("Retire o dinheiro no caixa")
    else:
        print("Saldo insuficiente")


MAIOR_IDADE = 18

# Loop para garantir que o usuário escolha uma opção válida
while True:
    opcao = int(input("Informe qual opção você deseja escolher [1] Verificar idade [2] Sacar: "))

    if opcao == 1:
        idade = int(input("Informe sua idade: "))
        
        if idade >= MAIOR_IDADE:
            print("Você é maior de idade")
        else:
            print("Você é menor de idade")
        break  # Sai do while após execução

    elif opcao == 2:
        sacar(400)
        break  # Sai do while após execução

    else:
        print("Você digitou uma opção inválida. Tente novamente.")
