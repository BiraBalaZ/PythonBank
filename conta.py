class Conta:
    def __init__(self, numero, titular, saldo, limite=1000.0):
        # Iniciando uma conta
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    
    # Função para depositar dinheiro em uma conta
    def deposita(self, valor):
        self.saldo += valor

    # Função para sacar dinheiro de uma conta
    def saca(self, valor):
        self.saldo -= valor

        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            return True

    # Função para ver o extrato de uma conta
    def extrato(self):
        print('A conta {} tem R$ {} de saldo.'.format(self.numero, self.saldo))

    # Função para transferência de contas
    def transfere(self, destino, valor):
        #self.saldo -= valor
        #destino.saldo += valor

        retirou = self.saca(valor)

        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            return True
