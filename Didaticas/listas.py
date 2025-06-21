#listas 

listas_normais = ["Nome",22, True] # lista normal 

lista_vazia = []

lista_string = list("Python") #Lista aonde cada letra do elemento digitado se torna um item da lista 

print(listas_normais[1])
print(lista_string[0])
print(listas_normais[-1]) # quanto chamamos numeros negativos estaremos chamando os itens no final da lista

# Matriz

primeira_matriz = [
    ["Filipe ",20,"Triste"],
    ["Raiva",24,"Inseguranca"],
    [2,22,111],
]

print(primeira_matriz[0])
print(primeira_matriz[0][0])
print(primeira_matriz[1][2])

#lista fateada e como chama 
lista_fateada = ["p","y","t","h","o","n"]

print(lista_fateada[:2])
print(lista_fateada[2:])
print(lista_fateada[:-1]) # exclui um item da lista 
print(lista_fateada[0:2])
print(lista_fateada[::-1]) # inverte aa lista 

#lista em for 
for lista_fateada in lista_fateada:
    print(lista_fateada)

#lista emunerate 

lojas = ["papel","cigarro","bebida","dinheiro"]

for indice_lista, loja in enumerate(lojas):
   print(f"{indice_lista}: {loja}")

#Adicionando valores de uma lista em outra lista, e modificando os mesmos

numeros_normais = [12,22,2,33,4,54,6,334,0,99,34,26]
numeros_pares = []

for numero in numeros_normais:
    if numero % 2 == 0:
        numeros_pares.append(numero) # o append que adicionou elementos da lista em outra 

numero_elevados_quadrado = []

for numero in numeros_normais:
    numero_elevados_quadrado.append(numero ** 2)

print(numeros_pares)
print(numero_elevados_quadrado)

numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}

# Função map

a = [1, 2, 3]
b = [4, 5, 6]

resultado = map(lambda x, y: x + y, a, b) #lambda e uma função vazia, o metodo map e dividido em duas instancias aonde declaramos o que vai acontecer na primeira instancia  que no caso do exemplo e o x + y e na segunda instancia definida pelas coisas que ven depois da "," são os dados que serao atribuidos ou seja o x = a e y = b x+y e = 4+1
print(list(resultado))
