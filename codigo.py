def imc(peso, altura):
  altura_quadrada = altura ** 2
  meu_imc = peso / altura_quadrada
  print(f'O meu imc é {meu_imc:.1f}')
  return meu_imc

