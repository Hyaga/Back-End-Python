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

# usando uma função dentro de outra função
def somar(a, b):
    return a + b


def exibir_resultado_soma(a, b, funcao): 
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")


exibir_resultado_soma(10, 10, somar) 