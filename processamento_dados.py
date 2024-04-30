
import json
import csv

class Dados:

    def __init__(self,path, tipo_dados):
        self._path = path
        self._tipo_dados = tipo_dados
        self.dados = self.leitura_dados()
        self.nome_colunas = self.get_colums()


    def _leitura_json(self):
        dados_json = []
        with open(self._path, 'r') as file:
            dados_json = json.load(file)

        return dados_json

    def _leitura_csv(self):
        dados_csv = []
        with open(self._path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)

        return dados_csv

    def leitura_dados(self):
        dados = []
        if self._tipo_dados == 'csv':
            dados = self._leitura_csv()
        
        if self._tipo_dados == 'json':
            dados = self._leitura_json()

        if self._tipo_dados == 'list':
            dados = self._path
            self._path = 'Lista em memória'
        
        return dados
    
    def get_colums(self):
        return list(self.dados[-1].keys())
    
    def rename_columns(self, key_map):
        new_dados = []

        for old_dict in self.dados:
            dict_temp = {}
            for old_key, value in old_dict.items():
                dict_temp[key_map[old_key]] = value
            new_dados.append(dict_temp)

        self.dados = new_dados
        self.nome_colunas = self.get_colums()

    def join(dadosA,dadosB):
        combined_list = []
        combined_list.extend(dadosA.dados)
        combined_list.extend(dadosB.dados)

        if len(combined_list) == (len(dadosA.dados) + len(dadosB.dados)):
            return Dados(combined_list, 'list')
        
        print(f'Problema de acesso')

    def _transforma_dados_tabela(self):
        nome_colunas = self.get_colums()
        dados_combinado_tabela = [nome_colunas]

        try:

            for row in self.dados:
                linha = []
                for coluna in self.nome_colunas:
                    linha.append(row.get(coluna, 'indisponível'))
                
                dados_combinado_tabela.append(linha)
            
            return dados_combinado_tabela
        
        except:
            print(f'Problema com junção de arquivos')

    def gravando_arquivo(self, path):
        dados_combinado_tabela = self._transforma_dados_tabela()
        try:
            with open(path,'w') as file:
                writer = csv.writer(file)
                writer.writerows(dados_combinado_tabela)
        
        except FileExistsError as error:
            print(error)

        finally:
            print(f'Programa finalizado')