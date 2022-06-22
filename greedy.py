from classes import ItemLargura, ResultadoCusto, TestManager
from common import get_cost_per_mm


def greedy_choice(
    test_case: TestManager,
    current_item: ItemLargura,
    rolos: list = [],
    total_cost: int = 0
  ) -> ResultadoCusto:
  """
    O parâmetro de escolha gulosa é o custo por mm de redução, e não
    simplesmente o menor custo de redução 
  """
  reduction = current_item.reduction_needed()

  cost_per_mm = get_cost_per_mm(current_item)
  if '3' in cost_per_mm and reduction < 3: cost_per_mm.pop('3')
  if '2' in cost_per_mm and reduction < 2: cost_per_mm.pop('2')

  best_cilinder_size = int(min(cost_per_mm, key=cost_per_mm.get))
  reduction -= best_cilinder_size
  reduction_cost = current_item.cost_by_number(best_cilinder_size)
  rolos.append(ResultadoCusto.build_rolo_info(
    current_item.width, best_cilinder_size, reduction_cost
    ))
  total_cost += reduction_cost

  if reduction == 0:
    return ResultadoCusto(current_item, total_cost, rolos)
  else:
    current_item = test_case.get_cost(current_item.width - best_cilinder_size)
    return greedy_choice(test_case, current_item, rolos, total_cost)


def get_best_option(test_case: TestManager) -> ResultadoCusto:
  """
    Recebe o TestManager e retorna o ResultadoCusto com a melhor forma de se chegar em 4mm
    utilizando um algoritmo guloso
  """
  initial_item = test_case.widthList.pop(0)
  best_result = greedy_choice(test_case, initial_item, [], 0)
  best_result.item = initial_item
  return best_result
