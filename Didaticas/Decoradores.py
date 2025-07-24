def mensagem(nome):
    return f"Oi {nome}"


def mensagem_longa(nome):
    return f"Olá tudo bem com você {nome}?"


def executar(funcao, nome): # Aqui que ocorre o diferencial pois se não tivesse passado o nome como parametro na hora de chamar a função o nome teria que ser colocado diretamente no return
    return funcao(nome)


print(executar(mensagem, "Joao"))
print(executar(mensagem_longa, "Joao"))

def calculadora(operacao):
    def soma(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def mul(a, b):
        return a * b

    def div(a, b):
        return a / b

    match operacao:
        case "+":
            return soma
        case "-":
            return sub
        case "*":
            return mul
        case "/":
            return div


op = calculadora("+")
print(op(2, 2))
op = calculadora("-")
print(op(2, 2))
op = calculadora("*")
print(op(2, 2))
op = calculadora("/")
print(op(2, 2))
