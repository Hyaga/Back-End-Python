# strings 

curso = "pyThon E o flUXo"

print(curso.upper()) # tudo maiusculo

print(curso.lower()) # tudo minusculo

print(curso.title()) # Titulo

print(curso.center(12, "#")) # Junções

print(".".join(curso)) # Junções


palavra_exemplo1 = "   Longe   "

print(palavra_exemplo1.strip()) # Tira todos espaços 

print(palavra_exemplo1.lstrip()) # Tira todos espaços esquerda

print(palavra_exemplo1.rstrip()) #  Tira todos espaços direita


nome =  input("Digite seu nome:")
idade = int(input("Digite sua idade:"))
materia = input("Digite seu curso :")
profissão = input("Digite sua profissao:")

# interpolação f - string
print(f"Olá , me chamo {nome}. Eu tenho{idade} anos, trabalho com {profissão} e estou cursando {materia}")

# edição usando f - string

PI = 3.145545
print(f"Valor de PI editado : {PI:2f}")
print(f"Valor de PI editado : {PI:10.2f}")
