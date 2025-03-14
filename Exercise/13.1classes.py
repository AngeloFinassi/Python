#Fz o msm programa usando classes de forma dinamica
# vendedor = "Ângelo"
# meta = 1500
# vendas = 1200

#Ao usar o self estou me dizendo que aquela variavel é do Vendedor
class Vendedor():
    #Função para setar parametros do Vendedor
    def __init__(self, nome):
        #self.nome = nome 'do vendedor'
        self.nome = nome

    def vendas(self, vendas):
        #self.vendas = vendas 'do vendedor'
        self.vendas = vendas

    def meta(self, meta):
        #self.metas = meta 'do vendedor'
        self.meta = meta

        #se a venda 'do vendedor' >= a meta 'do vendedor', ent ele bateu a meta
        if self.vendas >= self.meta:
            print(self.nome, "Bateu a meta", self.meta)
        else:
            print(self.nome, "Não Bateu a meta", self.meta)

    #Um método estático não acessa atributos de instância nem de classe
    @staticmethod
    def exibir_boas_vindas():
        print("Bem-vindo ao mundo dos vendedores!")

#Se chamar a meta sem charmar vendas anteriormente da erro
#não tem como trabalhar com uma caracteristica que não foi definida no __init__ ou não setada por outra função
print("-=" * 30)
vendedor1 = Vendedor("Ângelo")
vendedor1.vendas(2000)
vendedor1.meta(1000)

print("-=" * 30)
vendedor2 = Vendedor("Carol")
vendedor2.vendas(200)
vendedor2.meta(1000)

