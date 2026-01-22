listacaixas_entrada = []
listacaixas_saida = []
#Exibição do programa e orientação
print('Bem-vindo ao seu datador do fluxo de entregas.')
print('----------------------------------')
print('Digite o número [1] para registrar caixas entrando')
print('Digite o número [2] para registrar caixas saindo.')
print('Digite o número [3] para ver o seu relatório de entrada.')
print('Digite o número [4] para ver o seu relatório de saída.')
print('Digite o número [0] para desligar o programa.')
#Funções e o que cada uma faz
def entrando():
    horaentrada = str(input('Horário que o carregamento chegou (HH:MM): '))
    categoriaprod = str(input('Categoria dos produtos na caixa: '))
    produto = str(input('Nome do produto na caixa: '))
    # Tratamento de erro para garantir que a quantidade seja um número inteiro
    try:
        qtdcaixas = int(input('Quantidade de caixas de determinado produto: '))
    except ValueError:
        print('Por favor, insira um número válido.')
        return
    pesoproduto = float(input('Peso do produto na caixa em kg (XX.XX): '))
    contemimposto = str(input('A caixa contém imposto? (sim/não): ')).lower()
    if contemimposto == 'sim':
        contemimposto = True
    elif contemimposto == 'não' or contemimposto == 'nao':
        contemimposto = False
    else:
        print('Por favor, insira "Sim" ou "Não".')
        return
    # Tratamento de erro para garantir que o valor do imposto seja um número válido
    if contemimposto:
        try:
            valorimposto = float(input('Valor do imposto sobre a caixa (R$XX.xx): '))
        except ValueError:
            print('Por favor, insira um valor numérico válido para o imposto.')
            return
    if contemimposto:
        listacaixas_entrada.append((horaentrada, categoriaprod, produto, qtdcaixas, pesoproduto, contemimposto, valorimposto))
    else:
        listacaixas_entrada.append((horaentrada, categoriaprod, produto, qtdcaixas, pesoproduto, contemimposto))
    print ('Registro de entrada adicionado com sucesso.')
def saida():
    horarioentrega = str(input('Horário da entrega (HH:MM): '))
    categoriaprod = str(input('Categoria dos produtos na caixa: '))
    produto = str(input('Nome do produto na caixa: '))
    # Tratamento de erro para garantir que a quantidade seja um número inteiro
    try:
        qtdcaixas = int(input('Quantidade de caixas de determinado produto: '))
    except ValueError:
        print('Por favor, insira um número válido.')
        return
    listacaixas_saida.append((horarioentrega, categoriaprod, produto, qtdcaixas))
    print('Registro de saída adicionado com sucesso.')

def relatentrada():
  for horaentrada, categoria, prod, quantidade, pesoproduto, contemimposto, valorimposto in listacaixas_entrada:
    print('------------------------------------')
    print('RELATÓRIO DE REESTOQUE')
    print('------------------------------------')
    print(f'Horário do carregamento: {horaentrada}')
    print(f'Categoria: {categoria}')
    print(f'Nome do produto: {prod}')
    print(f'Quantidade de caixas: {quantidade}')
    print(f'Peso do produto: {pesoproduto} kg')
    print(f'Contém imposto: {"Sim" if contemimposto else "Não"}')
    if contemimposto:
      print(f'Valor do imposto: R${valorimposto:.2f}')
    print('-------------------------------------')


def relatsaida():
  for horarioentrega, categoriaprod, produto, quantidade in listacaixas_saida:
    print('-------------------------------------')
    print('RELATÓRIO DE ENTREGAS')
    print('-------------------------------------')
    print(f'Horário do carregamento: {horarioentrega}')
    print(f'Categoria: {categoriaprod}')
    print(f'Nome do produto: {produto}')
    print(f'Quantidade de caixas: {quantidade}')
    print('-------------------------------------')

#Funcionamento
while True:
  opcaoselecionada = (input('Digite a opção a ser selecionada: '))

  if opcaoselecionada == '1':
   entrando()
  elif opcaoselecionada == '2':
    saida()
  elif opcaoselecionada == '3':
    relatentrada()
  elif opcaoselecionada == '4':
   relatsaida()
  elif opcaoselecionada not in ['1', '2', '3', '4', '0']:
    print('Opção inválida. Por favor, selecione uma opção válida.')
  elif opcaoselecionada == '0':
    print('Programa encerrado.')
    break
