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