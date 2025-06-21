#Desafio para adicionarmos itens ao carrinho e soma-los

carrinho = []
total = 0.0

# Entrada do número de itens
itens = int(input().strip())

# Loop para adicionar itens ao carrinho
for _ in range(itens):
    linha = input().strip()
    
    # Encontra a última ocorrência de espaço para separar nome e preço
    posicao_espaco = linha.rfind(" ")
    
    # Separa o nome do produto e o preço
    item = linha[:posicao_espaco]
    preco = float(linha[posicao_espaco + 1:])
    
    # Adiciona ao carrinho
    carrinho.append((item, preco))
    total += preco
    #For que imprime os dados da lista 
for item, preco in carrinho:
    print(f"{item}: R${preco:.2f}")
print(f"Total: R${total:.2f}") #chamada do total

 