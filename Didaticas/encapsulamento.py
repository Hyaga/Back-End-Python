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

class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0

    @x.setter
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
        self._x = 0


foo = Foo(10)
print(foo.x)
del foo.x
print(foo.x)
foo.x = 10
print(foo.x)