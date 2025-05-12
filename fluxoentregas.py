listacaixas = []
#Exibição do programa
print('Bem-vindo ao seu datador de caixas')
print('----------------------------------')
print('Digte o número [1] para registrar caixas saindo!')
print('Digite qualquer outro número para ver o relatório do datador.')
print('@DATADOR RODANDO')
#recolhendo informação
def classificacao():
    categoriaprod = str(input('Categoria dos produtos na caixa: '))
    produto = str(input('Nome do produto na caixa: '))
    qtdcaixas = int(input('Quantidade de caixas de determinado produto: '))
    listacaixas.append((categoriaprod, produto, qtdcaixas))


while True:
  opcaoselecionada = (input('Digite a opção a ser selecionada: '))

  if opcaoselecionada == '1':
    classificacao()
  else:
    break

for categoria, prod, quantidade in listacaixas:
  print('------------------------------------')
  print(f'Categoria: {categoria}')
  print(f'Nome do produto: {prod}')
  print(f'Quantidade de caixas: {quantidade}')



