class ContaBancaria:
    def __init__(self, nome, saldo=0):
        self.nome = nome
        self.saldo = saldo
        pass

    
    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito valor de {valor} reais, agora seu saldo vale {self.saldo}")

    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Sacou {valor} reais, agora seu saldo é {self.saldo}")
        else:
            print(f'O valor sacado é maior doq o saldo')
        

conta = ContaBancaria('João', 1000)
conta.depositar(500)
conta.sacar(600)

print(conta)