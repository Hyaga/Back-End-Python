class _BancoDeDados:  # Convenção de classe "privada"
    def __init__(self):
        self.__dados = []  # Atributo "privado"

    def inserir_dado(self, dado):  # Método "público" para inserção
        self.__dados.append(dado)

    def obter_todos_os_dados(self):  # Método público para leitura
        return self.__dados.copy()

# Uso externo:
bd = _BancoDeDados()
bd.inserir_dado("cliente1")
bd.inserir_dado("cliente2")

print(bd.obter_todos_os_dados())