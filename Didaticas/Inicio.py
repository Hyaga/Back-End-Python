print("Hello Word")
print("Este sera o inicio do meu aprendizado com o back end em python")

# declaração tipos de dados 
idade = 23
numerofloat = 33.33
nome = "Filipe"

print("Meu nome e :",nome, "meu conhecimento sobre back-end",numerofloat ,"minha idade :",idade)

# alteração de dados sem 
idade = 22
numerofloat = 20.22
nome= "Pedro"

print("Meu nome e :",nome, "meu conhecimento sobre back-end",numerofloat ,"minha idade :",idade)

# Declaração de constante 

PI = 3.14159
NOME_DA_EMPRESA = "OpenAI"

print("Valor de pi:",PI,"Nome da Empresa:",NOME_DA_EMPRESA)

PI = 4
print(PI)

print(5//2)

#Inserção de inputs

nome_input = input("Digite seu noome:")

print(nome_input)

#Inserção de alguns operadores de atribuição

numero = 10

numero +18 #soma
print("O valor do numero na soma e:",numero)

numero - 8 #subtração
print("O valor do numero na subtração e :",numero)

numero *2 #multiplicaçao
print("O valor do numero na multiplicação e : ",numero)

numero / 4 #divisao
print("O valor do numero na divisao e:",numero)

numero **2 #exponencial
print("O valor do numero exponenciação",numero)

# operadores de identidade

numero_identidade, segundo_numero_identidade = 200, 200
curso = "Fisica"
nome_curso = curso

print(curso is nome_curso)
print(curso is numero_identidade)
print(numero_identidade is not segundo_numero_identidade)
print(numero_identidade is segundo_numero_identidade)

# formas de usar for 

for i in range(5):
    print(i)
    
nomes = ["Ana", "Bruno", "Carlos"]

for nome in nomes:
    print(nome)

texto = "Python"

for letra in texto:
    print(letra)

for i in range(10, 0, -2):
    print(i)


