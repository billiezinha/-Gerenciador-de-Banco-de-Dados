# from esquemas.tabela import Tabela

# # Definindo um esquema para a tabela "Clientes"
# esquema_clientes = {
#     "id": int,
#     "nome": str,
#     "email": str,
#     "telefone": str,
#     "pais": str
# }

# # Criando uma tabela chamada "Clientes"
# tabela_clientes = Tabela("Clientes", esquema_clientes)

# # Inserindo registros válidos
# tabela_clientes.inserir({"id": 1, "nome": "João", "email": "joao@mail.com", "telefone": "123456789", "pais": "Brasil"})
# tabela_clientes.inserir({"id": 2, "nome": "Maria", "email": "maria@mail.com", "telefone": "987654321", "pais": "Espanha"})

# # Tentando inserir um registro inválido (telefone como inteiro em vez de string)
# tabela_clientes.inserir({"id": 3, "nome": "Carlos", "email": "carlos@mail.com", "telefone": 123456789})

# # Listando os registros na tabela
# print(tabela_clientes.exibirTabela())

# /src/main.py

from b_tree.b_tree import BTree

def main():
    btree = BTree(3)  # Grau mínimo t = 3

    # Insere valores na Árvore B
    for val in [10, 20, 5, 6, 12, 30, 7, 17]:
        btree.insert(val)

    # Travessia para mostrar a árvore
    print("Traversal of tree:")
    btree.traverse(btree.root)
    print("\n")

    # Busca na árvore
    result = btree.search(6)
    if result:
        print("Encontrou")
    else:
        print("Não encontrou")

if __name__ == "__main__":
    main()
