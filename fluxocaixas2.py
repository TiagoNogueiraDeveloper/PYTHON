listacaixas_entrada = []
listacaixas_saida = []
#Exibição do programa e orientação
print('Bem-vindo ao seu datador de caixas')
print('----------------------------------')
print('Digite o número [1] para registrar caixas entrando!')
print('Digite o número [2] para registrar caixas saindo!.')
print('Digite o número [3] para ver o seu relatório de entrada.')
print('Digite o número [4] para ver o seu relatório de saída.')
print('Digite qualquer outra coisa para desligar o programa.')
print('@DATADOR RODANDO')
#Funções e o que cada uma faz
def entrando():
    horaentrada = str(input('Horário que o carregamento chegou: '))
    categoriaprod = str(input('Categoria dos produtos na caixa: '))
    produto = str(input('Nome do produto na caixa: '))
    try:
        qtdcaixas = int(input('Quantidade de caixas de determinado produto: '))
    except ValueError:
        print('Por favor, insira um número válido.')
        return
    listacaixas_entrada.append((horaentrada, categoriaprod, produto, qtdcaixas))
def saida():
    horarioentrega = str(input('Horário da entrega: '))
    categoriaprod = str(input('Categoria dos produtos na caixa: '))
    produto = str(input('Nome do produto na caixa: '))
    try:
        qtdcaixas = int(input('Quantidade de caixas de determinado produto: '))
    except ValueError:
        print('Por favor, insira um número válido.')
        return
    listacaixas_saida.append((horarioentrega, categoriaprod, produto, qtdcaixas))

def relatentrada():
  for horaentrada, categoria, prod, quantidade in listacaixas_entrada:
    print('------------------------------------')
    print('RELATÓRIO DE REESTOQUE')
    print('------------------------------------')
    print(f'Horário do carregamento: {horaentrada}')
    print(f'Categoria: {categoria}')
    print(f'Nome do produto: {prod}')
    print(f'Quantidade de caixas: {quantidade}')

def relatsaida():
  for horarioentrega, categoriaprod, produto, quantidade in listacaixas_saida:
    print('-------------------------------------')
    print('RELATÓRIO DE ENTREGAS')
    print('-------------------------------------')
    print(f'Horário do carregamento: {horarioentrega}')
    print(f'Categoria: {categoriaprod}')
    print(f'Nome do produto: {produto}')
    print(f'Quantidade de caixas: {quantidade}')
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
  else:
    print('DESLIGANDO')
    break



