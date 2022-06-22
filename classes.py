class ItemLargura(object):
  def __init__(self, line):
    # Construtor
    # Separa os valores da linha
    items = line.split(' ')
    # O primeiro valor é a expessura
    width = items.pop(0)

    # Testa se os valores são inteiros. Se não, define como None
    items_filtered = []
    for item in items:
      if item.isdigit():
        items_filtered.append(int(item))
      else:
        items_filtered.append(None)

    self.width = int(width)
    self.custo_1 = items_filtered[0]
    self.custo_2 = items_filtered[1]
    self.custo_3 = items_filtered[2]

  def reduction_needed(self):
    # Retorna quantos mm precisam ser reduzidos para chegar a 4
    return self.width - 4 if self.width > 4 else 0

  def cost_by_number(self, number):
    # Recebe um número e retorna o custo da redução desse número
    if number == 1:
      return self.custo_1
    elif number == 2:
      return self.custo_2
    elif number == 3:
      return self.custo_3
    else:
      return None

  def __str__(self):
    # Retorna o objeto como string
    return f'Largura {self.width}: {self.custo_1 or "X"}/{self.custo_2 or "X"}/{self.custo_3 or "X"}'



class ResultadoCusto(object):
  def __init__(self, item: ItemLargura, cost: int, rolos: list):
    # Construtor
    self.custo = cost
    self.tamanho_rolos = rolos
    self.item = item

  def get_rolo_pretty_print(self):
    # Retorna uma versão mais bonita da lista de rolos
    rolo_list = ''
    for rolo in self.tamanho_rolos:
      rolo_list += f' {rolo}\n'
    return rolo_list
  
  @staticmethod
  def build_rolo_info(width: int, cil_size: int, cost: int):
    # Constroi infors do rolo como string
    return (
      f' De {width}mm -> {width - cil_size}mm. Reducao de {cil_size}mm. Custo: {cost}'
      )
  
  def __str__(self):
    # Retorna o objeto como string
    return f'Expessura {str(self.item.width).rjust(2, "0")} --> Custo total: {str(self.custo).rjust(2, "0")}. Rolos:\n{self.get_rolo_pretty_print()}'



class TestManager(object):
  def __init__(self, itemList: list, case_number: int, algorithm_results: list):
    # Construtor
    self.widthList = itemList
    self.case_number = case_number
    self.algorithm_results = algorithm_results
  
  def get_cost(self, current_mm: int) -> ItemLargura:
    # Retorna o ItemLargura para uma espessura determinada
    for item in self.widthList:
      if item.width == current_mm:
        return item
    return None

  def print_results(self):
    # Imprime os resultados
    print(f'======> Caso de teste #{self.case_number}')
    for algorithm in self.algorithm_results:
      print(f'**** Algoritmo {algorithm["name"]} executado em {algorithm["exec_time"]}')
      print(f'**** Melhor resultado: {algorithm["best_result"]}')
      print('\n')
