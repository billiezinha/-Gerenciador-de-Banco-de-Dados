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