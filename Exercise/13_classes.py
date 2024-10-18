class ContaBanco:
    #define caracteristicas sobre o objeto
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

    #trabalha com caracteristicas ja definidas
    #self se refere a caracteristica daquele objeto
    def verificarSaldo(self):
        print(f"Saldo atual: {self.saldo}")
        self.printBonito()
        
    def retirada(self, valor):
        self.saldo -= valor
        print(f"Valor Retirado:{valor}")
        #Mais recomendado, o self não tem relação com métodos estátisticos
        ContaBanco.printBonito()
        

    def depositar(self, valor):
        self.saldo += valor
        print(f"Valor Depositado:{valor}")
        ContaBanco.printBonito()
    
    @staticmethod
    def printBonito():
        print('=-' * 30)

conta1 = ContaBanco('Angelo', 1000)
conta1.verificarSaldo()

conta1.depositar(100)
conta1.verificarSaldo()


conta1.retirada(200)
conta1.verificarSaldo()

#Acessar dados
print(conta1.saldo)
print(conta1.nome)