from classes import ItemLargura, ResultadoCusto


def get_cost_per_mm(item: ItemLargura):
  """
    Recebe o ItemLargura e retorna o custo por mm para cada nível de redução
  """
  return_dict = {}
  if item.custo_1 is not None: return_dict['1'] = item.custo_1
  if item.custo_2 is not None: return_dict['2'] = item.custo_2 / 2
  if item.custo_3 is not None: return_dict['3'] = item.custo_3 / 3
  return return_dict


def greedy_choice(
    reduction: int,
    item: ItemLargura,
    cost_per_mm: object,
    rolos: list = [],
    total_cost: int = 0
  ) -> ResultadoCusto:
  """
    O parâmetro de escolha gulosa é o custo por mm de redução, e não
    simplesmente o menor custo de redução 
  """
  if reduction == 0: return ResultadoCusto(item, total_cost, rolos)
  if '3' in cost_per_mm and reduction < 3: cost_per_mm.pop('3')
  if '2' in cost_per_mm and reduction < 2: cost_per_mm.pop('2')

  best_cilinder_size = int(min(cost_per_mm, key=cost_per_mm.get))
  reduction -= best_cilinder_size
  rolos.append(best_cilinder_size)
  total_cost += item.cost_by_number(best_cilinder_size)

  return greedy_choice(reduction, item, cost_per_mm, rolos, total_cost)



def get_best_option(item: ItemLargura) -> ResultadoCusto:
  """
    Recebe o ItemLargura e retorna o ResultadoCusto com a melhor forma de se chegar em 4mm
  """
  cost_per_mm = get_cost_per_mm(item)
  return greedy_choice(item.reduction_needed(), item, cost_per_mm)
