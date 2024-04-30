## Importação de Objeto
from processamento_dados import Dados

path_json = 'data_raw/dados_empresaA.json'
path_csv  = 'data_raw/dados_empresaB.csv'

## Leitura dos dados
dados_empresA = Dados.leitura_dados(path_json,'json')
dados_empresB = Dados.leitura_dados(path_csv,'csv')

## Tranformação
key_map = {'Nome do Item' : 'Nome do Produto',
            'Classificação do Produto' : 'Categoria do Produto',
            'Valor em Reais (R$)' : 'Preço do Produto (R$)',
            'Quantidade em Estoque' : 'Quantidade em Estoque',
            'Nome da Loja':'Filial',
            'Data da Venda': 'Data da Venda'}

dados_empresB.rename_columns(key_map)

dados_fusao = Dados.join(dados_empresA, dados_empresB)

## Gravação
path_dados_combinados = "data_processed/dados_combinados.csv"
dados_fusao.gravando_arquivo(path_dados_combinados)
