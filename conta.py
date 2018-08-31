#criar uma classe conta, com os atributos(numero,agencia,tipo,saldo) e metodos(depósito, saque, transferencia e consultar saldo)

class Conta:
    def __init__(self, numero, agencia, tipo, saldo):
        self.numero = numero
        self.agencia = agencia
        self.tipo = tipo
        self.saldo = saldo

    def depósito(self,qtd):
        if self.numero & self.agencia:
            self.saldo += qtd

    def saque(self,qtd):
        if self.numero & self.agencia:
            if self.saldo >= qtd:
                self.saldo -= qtd

    def transferencia(self,Conta, qtd):
        if self.numero & self.agencia:
            if self.saldo >= qtd:
                self.saldo -=qtd
                Conta.saldo += qtd

    def mostrar_saldo(self):
        if self.numero & self.agencia:
            print('Seu saldo é de: R$', self.saldo)


meu_conta = Conta(111, 12 - 1, 'poupança', 100.00)
meu_conta.depósito(100.00)
meu_conta.saque(50.00)
ww_conta = Conta(222, 21-2,'conta corrente', 200.00)
meu_conta.transferencia(ww_conta, 150.00)
print(meu_conta.saldo, ww_conta.saldo)
ww_conta.mostrar_saldo()
