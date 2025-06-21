# Entrada do número de itens
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

for _ in range(n):
    linha = input().strip()
    
    # Separando nome e tema com base na vírgula
    nome, tema = map(str.strip, linha.split(','))

    # Adicionando ao dicionário
    if tema in eventos:
        eventos[tema].append(nome)
    else:
        eventos[tema] = [nome]

# Exibindo os resultados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")
