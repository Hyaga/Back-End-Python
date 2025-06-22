#funçoes 
def exibir_mensagem(): 
    print("Olá mundo!")


def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")


def exibir_mensagem_3(nome="Anônimo"): # quando declacaramos algo como no escopo da função essa informação fica pre gravada para ser o defaut da função
    print(f"Seja bem vindo {nome}!")


exibir_mensagem()
exibir_mensagem_2(nome="Filipe")
exibir_mensagem_3()
exibir_mensagem_3(nome="Dantas")
