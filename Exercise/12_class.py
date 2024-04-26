class MinhaClasse:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def somar(self):
        return self.x + self.y

# Criando um objeto da classe MinhaClasse
objeto = MinhaClasse(3, 4)

# Acessando atributos e chamando métodos
print(objeto.y)  # Saída: 3
print(objeto.somar())  # Saída: 7
