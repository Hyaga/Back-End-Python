# identação de blocos

def sacar(valor):
    saldo = 500

    if saldo >= valor: 
        print("Valor valido")
        print("Retire o dinheiro no caixa")

# estruturas condicionais são os if else e ilif

opcao = int(input("Informe qual opcao voce deseja escolher [1] Verificar idade [2] Sacar: "))


if opcao == 1:
    MAIOR_IDADE = 18
    idade = int(input("Informe sua idade : "))
    
    if idade >= MAIOR_IDADE:
        print("Voce e maior de idade")
    else:
        print("Voce e menor de idade")
        
elif opcao == 2:
    sacar(400) 
else:
    print("Voce digitou uma opção invalida")