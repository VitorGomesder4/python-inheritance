from contabancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
  def __init__(self, titular, saldo, limite_negativo):
    super().__init__(titular, saldo)#chama o init da classe mãe
    self.limite_negativo = limite_negativo
  
  def sacar(self, saque):
    try:
      saque = float(saque)
    except ValueError:
      raise TypeError("Valor de saque não é um número válido\n")
    
    if self.saldo - saque >= self.limite_negativo:
      self.saldo -= saque
      print("{:.2f}R$ Sacados\nAgora seu saldo é {}R$".format(saque, self.saldo))
    else:
      print("Esse limite vai além de {}".format(self.limite_negativo))