# Aluno: Gabriel Teixeira Rodrigues
# CES-22: Programação Orientada a Objetos
# Professora Karla Donato Fook       

class Order():


    def execute(self):
        pass


class SaldoVerificarOrder(Order):

    def __init__(self, conta):
        self.conta = conta

    def execute(self):
        self.conta.saldo()


class ExtratoVerificarOrder(Order):

    def __init__(self, conta):
        self.conta = conta

    def execute(self):
        self.conta.extrato()


class TransferenciaRealizarOrder(Order):

    def __init__(self, conta):
        self.conta = conta

    def execute(self):
        self.conta.transfer()


class Banco:

    def saldo(self):
        print("Esse é o seu saldo.")


    def extrato(self):
        print("Esse é o seu extrato.")


    def transfer(self):
        print("Transferência realizada com sucesso.")


class Agente:

    def __init__(self):
        self.__order_queue = []

    def place_order(self, order):
        self.order = order
        order.execute()

banco = Banco()
ver_saldo = SaldoVerificarOrder(banco)
ver_extrato = ExtratoVerificarOrder(banco)
transferir = TransferenciaRealizarOrder(banco)

agent = Agente()
agent.place_order(ver_saldo)
agent.place_order(ver_extrato)
agent.place_order(transferir)
