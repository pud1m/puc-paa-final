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
  
  def __str__(self):
    # Retorna o objeto como string
    return f'Expessura {str(self.item.width).rjust(2, "0")} --> Custo: {str(self.custo).rjust(2, "0")}. Rolos: {self.tamanho_rolos}'
