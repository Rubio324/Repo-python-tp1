def es_par(valor):
  """
  Esta función devuelve un valor booleano indicando de la variable
  valor es par
  """

  # chequeamos si el valor modulo 2 es igual a 0
  if valor % 2 == 0:
    return True
  else:
    return False


def es_impar(valor):
  """
  Esta función devuelve un valor booleano indicando de la variable
  valor es impar
  """
  return not es_par(valor)

print(es_par(2))
print(es_impar(2))
print(es_par(7))
print(es_impar(7))