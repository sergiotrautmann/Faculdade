class Conta:
    def __init__(self, numero, agencia, tipo, saldo):
        self.numero = numero
        self.agencia = agencia
        self.tipo = tipo
        self.saldo = saldo

    def deposito(self,qtd):
        if self.numero & self.agencia:
            self.saldo += qtd

    def saque(self,qtd):
        if self.numero & self.agencia:
            if self.saldo >= qtd:
                self.saldo -= qtd

    def transferencia(self, conta, qtd):
        if self.numero & self.agencia:
            if self.saldo >= qtd:
                self.saldo -= qtd
                conta.receber(qtd)

    def receber(self, qtd):
        if self.numero & self.agencia:
            if self.saldo >= qtd:
                self.saldo += qtd


    def mostrar_saldo(self):
        if self.numero & self.agencia:
            return self.saldo

meu_conta = Conta(111, 12 - 1, 'poupança', 100.00)
meu_conta.deposito(100.00)
meu_conta.saque(50.00)

ww_conta = Conta(222, 21-2,'conta corrente', 200.00)
meu_conta.transferencia(ww_conta, 150.00)

print(meu_conta.saldo, ww_conta.saldo)
print(f'O saldo da conta é: {meu_conta.mostrar_saldo()}')