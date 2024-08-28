from .esquema import Esquema

class Tabela:
    def __init__(self, nome, esquema):
        self.nome = nome
        self.esquema = Esquema(esquema)
        self.registros = []

    def inserir(self, registro):
        try:
            self.esquema.validar(registro)
            self.registros.append(registro)
            print(f"Registro inserido com sucesso: {registro}")
        except ValueError as e:
            print(f"Erro ao inserir registro: {e}")

    def exibirTabela(self):
        colunas = list(self.esquema.esquema_desc.keys())  
        largura_colunas = [max(len(coluna), 10) for coluna in colunas]  

        header = "+" + "+".join("-" * (largura + 2) for largura in largura_colunas) + "+"
        header_row = "|" + "|".join(f" {coluna:<{largura}} " for coluna, largura in zip(colunas, largura_colunas)) + "|"

        print(f"Tabela {self.nome}:")
        print(header)
        print(header_row)
        print(header)

        for registro in self.registros:
            row = "|" + "|".join(f" {str(registro[coluna]):<{largura}} " for coluna, largura in zip(colunas, largura_colunas)) + "|"
            print(row)

        print(header)

    def atualizar(self, id_registro, novos_dados):
        for registro in self.registros:
            if registro['id'] == id_registro:
                for chave, valor in novos_dados.items():
                    if chave in self.esquema.esquema_desc:
                        if not isinstance(valor, self.esquema.esquema_desc[chave]):
                            raise ValueError(f"Campo '{chave}' deve ser do tipo {self.esquema.esquema_desc[chave].__name__}")
                        registro[chave] = valor
                    else:
                        raise ValueError(f"Campo '{chave}' não faz parte do esquema da tabela")
                print(f"Registro com ID {id_registro} atualizado com sucesso.")
                return
        print(f"Registro com ID {id_registro} não encontrado na tabela '{self.nome}'.")


    def excluir(self, id_registro):
        print(f"Excluindo registro com ID {id_registro} da tabela '{self.nome}'")
        print("Registros antes da exclusão:", self.registros)
        
        for i, registro in enumerate(self.registros):
            print(f"Verificando registro: {registro}")
            if registro['id'] == id_registro:
                del self.registros[i]
                print(f"Registro com ID {id_registro} excluído com sucesso da tabela '{self.nome}'.")
                print("Registros após a exclusão:", self.registros)
                return
        
        print(f"Registro com ID {id_registro} não encontrado na tabela '{self.nome}'.")


        

