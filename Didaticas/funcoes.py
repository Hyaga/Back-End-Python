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
def somar(numero_a, numero_b):
    return numero_a + numero_b

def subtrair(numero_a,numero_b):
    return numero_a - numero_b

def exibir_resultado_soma(numero_a, numero_b, funcao): 
    resultado = funcao(numero_a, numero_b)
    print(f"O resultado da operação {numero_a} + {numero_b} = {resultado}")

# Lê os valores do teclado e converte para int
numero_a = int(input())
numero_b = int(input())

# Chama a função
exibir_resultado_soma(numero_a, numero_b, subtrair)
