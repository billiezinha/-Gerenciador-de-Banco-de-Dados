from tabela.tabela import Tabela
from esquema.esquema import Esquema

def main():
    # Seu código de teste aqui
    esquema_desc = {
        'id': int,
        'nome': str,
        'idade': int,
    }

    esquema = Esquema(esquema_desc)
    tabela = Tabela("Clientes", esquema_desc)

    print("Inserindo registros...")
    tabela.inserir({'id': 1, 'nome': 'Alice', 'idade': 30})
    tabela.inserir({'id': 2, 'nome': 'Bob', 'idade': 24})
    tabela.inserir({'id': 3, 'nome': 'Carlos', 'idade': 28})

    print("\nTabela após inserções:")
    tabela.exibirTabela()

    print("\nAtualizando o registro com ID 2...")
    tabela.atualizar(2, {'nome': 'Robert', 'idade': 25})

    print("\nTabela após atualização:")
    tabela.exibirTabela()

    print("\nExcluindo o registro com ID 1...")
    tabela.excluir(1)

    print("\nTabela após exclusão:")
    tabela.exibirTabela()

if __name__ == "__main__":
    main()
