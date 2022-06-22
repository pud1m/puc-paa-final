import time, re
from classes import ItemLargura
from greedy import get_best_option


def sanitize_line(line):
  # Recebe uma linha do arquivo e a sanitiza
  return re.sub(r' +', ' ', line).replace('\n', '') + ' 0 0'


def get_payload_from_file(number):
  # Pega listas para testes de arquivo. Recebe o número do LaminacaoTeste.txt como param
  inputs = []
  with open(f'LaminacaoTeste{number}.txt', 'r') as f:
    lines = f.readlines()
    # Para cada linha:
    for line in lines:
      # Cria um objeto com a largura e os valores para cada redução de expessura e adiciona à lista
      item_largura = ItemLargura(sanitize_line(line))
      inputs.append(item_largura)
  return inputs


if __name__ == '__main__':
  print('FPAA 2022/1')
  print('==============================')


  # Define os tipos de teste (arquivos)
  test_cases = [1, 2, 3, 4]

  # Define os algoritmos a serem usados
  algorithms = [
    {
    'name': 'Greedy',
    'function': get_best_option
    },
  ]


  # Para cada teste de caso
  test_results = []
  for case in test_cases:
    print('*****')
    print(f'Rodando Teste {case}')

    # Pega os inputs
    inputs = get_payload_from_file(case)

    algorithm_results = []

    # Para cada algoritmo
    for algorithm in algorithms:
      print(algorithm['name'])
      result_list = []
      start = time.perf_counter_ns()
      for item in inputs:
        result_list.append(algorithm['function'](item))
      algorithm_results.append({
        'name': algorithm['name'],
        'exec_time': f'{(time.perf_counter_ns() - start)} ns',
        'results': result_list,
        'best_result': min(result_list, key=lambda x: x.custo),
      })

    # Adiciona o resultado do teste à lista de resultados
    test_results.append({
      'case': case,
      'results': algorithm_results
    })

  print('============================== \n')
  

  # Imprime os resultados
  print('************* RESULTADOS *************')
  for test in test_results:
    print(f'====== >Caso de teste #{test["case"]}')
    for algorithm in test['results']:
      print(f'**** Algoritmo {algorithm["name"]} executado em {algorithm["exec_time"]}')
      print(f'**** Melhor resultado: {algorithm["best_result"]}')
      for result in algorithm['results']:
        print(result)
      print('\n')
    print('\n')


  print('==============================')
