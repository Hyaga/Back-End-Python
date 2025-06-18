menu  = """
Escolha a opção desejada

[1] - Sacar
[2] - Depositar
[3] - Extrato
[4] - Sair

"""
saldo_bancario = 0
limite_de_saque = 500
saques = 0
LIMITE_DE_QUANTIDADES_SAQUE = 3
extrato = ""
while True:
  
    input(menu)

    if menu == 1:
        deposito = int(input("Digite o valor que voce deseja depositar:"))
        if deposito > 0:
            saldo_bancario += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
        else:
            print("O valor informado é inválido, por favor insira um valor valido.")
    elif menu ==2:
        deposito = float(input("Informe o valor do saque: "))

        excedeu_saldo = deposito > saldo_bancario

        excedeu_limite = deposito > limite_de_saque 


        excedeu_saques = saques >= LIMITE_DE_QUANTIDADES_SAQUE 

        if excedeu_saldo:
            print("Você não tem saldo suficiente.")

        elif excedeu_limite:
            print(" Voce nao tem saldo suficiente para sacar.")

        elif excedeu_saques:
            print("Voce ja atingiu o máximo de saques excedido.")

        elif deposito > 0:
            saldo_bancario -= deposito
            extrato += f"Saque: R$ {deposito:.2f}\n"
            saques += 1

    elif menu == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo_bancario:.2f}")
        print("==========================================")

    elif menu == "4":
        break

    else:
        print("Por favor selecione novamente a operação desejada.")