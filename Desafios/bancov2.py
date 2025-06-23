import textwrap


def menu():
    menu = """\n
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar contas
    [6]\tNovo usuário
    [7]\tSair
    => """
    return input(textwrap.dedent(menu))
    
def deposito(saldo_bancario,valor_deposito,extrato, /):
    if valor_deposito > 0:
        saldo_bancario += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito:.2f}"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ O valor informado é inválido, por favor insira um valor valido. @@@")
    return saldo_bancario, extrato
    
def sacar(*,saldo_bancario,valor_deposito,extrato,limite,saques,limite_de_saque):
    excedeu_saldo = valor_deposito > saldo_bancario
    excedeu_limite = valor_deposito > limite
    excedeu_saques = saques >= limite_de_saque 

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

    return saldo_bancario, extrato, saques
    
def exibir_extrato(saldo_bancario, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo_bancario:.2f}")
    print("==========================================")
    
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo_bancario = 0
    limite= 500
    saques = 0
    limite_de_saque = 3
    extrato = ""
    usuarios = []
    contas = []

    while True:
        opcao = menu() 

        if opcao == "1":
            valor_deposito = float(input("Informe o valor do depósito: "))

            saldo_bancario, extrato = deposito(saldo_bancario, valor_deposito, extrato)
        elif opcao == "2":
            valor_deposito = float(input("Informe o valor do saque: "))

            saldo_bancario, extrato, saques = sacar(
                saldo_bancario=saldo_bancario,
                valor_deposito=valor_deposito,
                extrato=extrato,
                limite=limite,
                saques=saques,
                limite_de_saque=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo_bancario,extrato=extrato)
        elif opcao == "4":
            criar_usuario(usuarios)
        elif opcao == "5":
            listar_contas(contas)
        elif opcao == "6":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)


        elif opcao == "7":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()