from classes import ItemLargura, ResultadoCusto


def get_best_option(item: ItemLargura) -> ResultadoCusto:
  """
    Recebe o ItemLargura e retorna o ResultadoCusto com a melhor forma de se chegar em 4mm
    utilizando um algoritmo guloso com backtracking
  """
  cost_per_mm = get_cost_per_mm(item)
  return greedy_choice(item.reduction_needed(), item, cost_per_mm, [], 0)
