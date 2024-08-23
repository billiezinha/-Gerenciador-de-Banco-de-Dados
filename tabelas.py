class Esquema:
    def __init__(self, esquema_desc):
        self.esquema_desc = esquema_desc

    def validar(self, registro):
        for chave, valor in registro.items():
            tipo_esperado = self.esquema_desc.get(chave)
            if tipo_esperado and not isinstance(valor, tipo_esperado):
                raise ValueError(f"Valor inválido para a coluna '{chave}'. Esperado {tipo_esperado.__name__}, obtido {type(valor).__name__}.")
            
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
#


# Definindo um esquema para a tabela "Clientes"
esquema_clientes = {
    "id": int,
    "nome": str,
    "email": str,
    "telefone": str,
    "pais": str
}

# Criando uma tabela chamada "Clientes"
tabela_clientes = Tabela("Clientes", esquema_clientes)

# Inserindo registros válidos
tabela_clientes.inserir({"id": 1, "nome": "João", "email": "joao@mail.com", "telefone": "123456789", "pais": "Brasil"})
tabela_clientes.inserir({"id": 2, "nome": "Maria", "email": "maria@mail.com", "telefone": "987654321", "pais": "Espanha"})

# Tentando inserir um registro inválido (telefone como inteiro em vez de string)
tabela_clientes.inserir({"id": 3, "nome": "Carlos", "email": "carlos@mail.com", "telefone": 123456789})

# Listando os registros na tabela
print(tabela_clientes.exibirTabela())



