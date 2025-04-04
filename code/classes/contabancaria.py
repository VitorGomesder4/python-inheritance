class ContaBancaria():
  def __init__(self, titular, saldo):
    self.titular = titular
    self.saldo = saldo

  def exibir_info(self):
    print("Titular da conta: {}\nSaldo da conta: {}".format(self.titular, self.saldo))

  def depositar(self, deposito):
    try:
      deposito = float(deposito)
    except ValueError:
      raise TypeError("Valor não é um número válido\n")

    self.saldo += deposito
    print("{:.2f}R$ Depositados\nAgora seu saldo é {}R$".format(deposito, self.saldo))
  
  def sacar(self, saque):
    try:
      saque = float(saque)
    except ValueError:
      raise TypeError("Valor de saque não é um número válido\n")
    
    if saque < self.saldo:
      self.saldo -= saque
      print("{:.2f}R$ Sacados\nAgora seu saldo é {}R$".format(saque, self.saldo))
    else:
      print("Saldo insuficiente para o saque.")