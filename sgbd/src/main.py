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

# from esquemas.tabela import Tabela

# esquema_clientes = {
#     "id": int,
#     "nome": str,
#     "email": str,
#     "telefone": str,
#     "pais": str
# }

# # Criando a tabela "Clientes"
# tabela_clientes = Tabela("Clientes", esquema_clientes)

# # Inserindo registros válidos
# tabela_clientes.inserir({"id": 3, "nome": "jose", "email": "joao@mail.com", "telefone": "123456789", "pais": "Brasil"})
# tabela_clientes.inserir({"id": 4, "nome": "Maria", "email": "maria@mail.com", "telefone": "987654321", "pais": "Espanha"})

# # Tentando inserir um registro inválido para testar a validação
# #tabela_clientes.inserir({"id": 3, "nome": "Carlos", "email": "carlos@mail.com", "telefone": 123456789})  # Telefone como número em vez de string

# # Exibindo a tabela
# tabela_clientes.exibirTabela()

# # Atualizando um registro existente
# tabela_clientes.atualizar(4, {"nome": "João Silva", "email": "joaosilva@mail.com"})
# tabela_clientes.exibirTabela()

# Exibindo a tabela novamente para verificar a atualização
# tabela_clientes.excluir()
# tabela_clientes.exibirTabela()
# tabela_clientes.atualizar(2, {"nome": "João Silva", "telefone": "123456789", "pais": "Brasil"})  # Telefone como número em vez de string

# tabela_clientes.exibirTabela()

# from arvore.b_tree import BTree

# def main():
#     btree = BTree(3)  # Grau mínimo t = 3

#     # Insere valores na Árvore B
#     for val in [10, 20, 5, 6, 12, 30, 7, 17]:
#         btree.insert(val)

#     # Travessia para mostrar a árvore
#     print("Traversal of tree:")
#     btree.traverse(btree.root)
#     print("\n")

#     # Busca na árvore
#     result = btree.search(6)
#     if result:
#         print("Encontrou")
#     else:
#         print("Não encontrou")

# if __name__ == "__main__":
#     main()

from arvore.b_tree import BTree

def exibir_menu():
    print("\nMenu:")
    print("1. Inserir valor")
    print("2. Deletar valor")
    print("3. Buscar valor")
    print("4. Exibir Árvore B")
    print("5. Sair")
    escolha = input("Escolha uma opção: ")
    return escolha

def inserir_valor(btree):
    valor = int(input("Digite o valor a ser inserido: "))
    btree.insert(valor)
    print(f"Valor {valor} inserido.")

def deletar_valor(btree):
    valor = int(input("Digite o valor a ser deletado: "))
    btree.delete(valor)
    print(f"Valor {valor} deletado.")

def buscar_valor(btree):
    valor = int(input("Digite o valor a ser buscado: "))
    resultado = btree.search(valor)
    if resultado:
        print(f"Valor {valor} encontrado na árvore.")
    else:
        print(f"Valor {valor} não encontrado na árvore.")

def exibir_arvore(btree):
    print("Exibindo Árvore B:")
    print_tree(btree.root, btree)

def print_tree(node, btree, nivel=0):
    if node is not None:
        print(" " * (nivel * 4) + str(node.keys))
        if not btree.is_leaf(node):
            for child in node.children:
                print_tree(child, btree, nivel + 1)

def main():
    grau_minimo = int(input("Digite o grau mínimo da Árvore B: "))
    btree = BTree(grau_minimo)

    while True:
        escolha = exibir_menu()

        if escolha == '1':
            inserir_valor(btree)
        elif escolha == '2':
            deletar_valor(btree)
        elif escolha == '3':
            buscar_valor(btree)
        elif escolha == '4':
            exibir_arvore(btree)
        elif escolha == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
