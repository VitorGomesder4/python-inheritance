from contabancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):
  def rendimento(self, taxa):
    try:
      taxa = float(taxa)
    except ValueError:
      raise TypeError("Valor de taxa não é um número válido (1 - 100%)\n")

    if taxa > 0 and taxa <= 100:
      taxa_decimal = taxa/100
      rendimento_p = self.saldo * taxa_decimal
      self.saldo += rendimento_p
      print("Saldo {}R$ (+{}R$ rendimento acrescentado)".format(self.saldo, rendimento_p))

    else:
      print("A taxa deve ser > 0 e <= 100.")