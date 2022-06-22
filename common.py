from classes import ItemLargura


def get_cost_per_mm(item: ItemLargura):
  """
    Recebe o ItemLargura e retorna o custo por mm para cada nível de redução
  """
  return_dict = {}
  if item.custo_1 is not None: return_dict['1'] = item.custo_1
  if item.custo_2 is not None: return_dict['2'] = item.custo_2 / 2
  if item.custo_3 is not None: return_dict['3'] = item.custo_3 / 3
  return return_dict
