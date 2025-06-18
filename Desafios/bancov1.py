
menu  ="""
---- Menu ----

[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Sair

Escolha a opção desejada:"""

saldo_bancario = 0
limite_de_saque = 500
saques = 0
LIMITE_DE_QUANTIDADES_SAQUE = 3
extrato = ""

while True:

    opcao = input(menu)

    if opcao == "1":
        valor_deposito = float(input("Informe o valor do depósito: "))

        if valor_deposito > 0:
            saldo_bancario += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"

        else:
            print("O valor informado é inválido, por favor insira um valor valido.")

    elif opcao == "2":
        valor_deposito = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor_deposito > saldo_bancario

        excedeu_limite = valor_deposito > limite_de_saque 


        excedeu_saques = saques >= LIMITE_DE_QUANTIDADES_SAQUE 

        if excedeu_saldo:
            print("Você não tem saldo suficiente.")

        elif excedeu_limite:
            print(" Voce nao tem saldo suficiente para sacar.")

        elif excedeu_saques:
            print("Voce ja atingiu o máximo de saques excedido.")

        elif valor_deposito > 0:
            saldo_bancario -= valor_deposito
            extrato += f"Saque: R$ {valor_deposito:.2f}\n"
            saques += 1

        else:
            print("O valor informado é maior do que o permitido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo_bancario:.2f}")
        print("==========================================")

    elif opcao == "4":
        break

    else:
        print("Por favor selecione novamente a operação desejada.")