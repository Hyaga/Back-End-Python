def mensagem(nome):
    return f"Oi {nome}"


def mensagem_longa(nome):
    return f"Olá tudo bem com você {nome}?"


def executar(funcao, nome): # Aqui que ocorre o diferencial pois se não tivesse passado o nome como parametro na hora de chamar a função o nome teria que ser colocado diretamente no return
    return funcao(nome)


print(executar(mensagem, "Joao"))
print(executar(mensagem_longa, "Joao"))