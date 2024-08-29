import sqlite3
from arvore_b.btree import BTree

# Função para conectar ao banco de dados e criar a tabela, se não existir
def connect_db():
    conn = sqlite3.connect('btree.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS BTreeData (
            id INTEGER PRIMARY KEY,
            key INTEGER NOT NULL,
            value TEXT NOT NULL
        )
    ''')
    conn.commit()
    return conn, cursor

# Função para carregar dados do banco de dados para a árvore B
def load_data(cursor, btree):
    cursor.execute("SELECT key, value FROM BTreeData ORDER BY key")
    rows = cursor.fetchall()
    for row in rows:
        btree.insert((row[0], row[1]))

# Função para inserir dados no banco de dados
def insert_to_db(cursor, conn, key, value):
    cursor.execute("INSERT INTO BTreeData (key, value) VALUES (?, ?)", (key, value))
    conn.commit()

# Função para deletar dados do banco de dados
def delete_from_db(cursor, conn, key):
    cursor.execute("DELETE FROM BTreeData WHERE key = ?", (key,))
    conn.commit()

# Função para inserir dados iniciais no banco de dados e na árvore B
def insert_initial_data(cursor, conn, btree):
    initial_data = [
        (10, "Item 10"),
        (20, "Item 20"),
        (5, "Item 5"),
        (6, "Item 6"),
        (12, "Item 12"),
        (30, "Item 30"),
        (7, "Item 7"),
        (17, "Item 17")
    ]
    
    for key, value in initial_data:
        btree.insert((key, value))
        insert_to_db(cursor, conn, key, value)

def print_menu():
    print("\nEscolha uma opção:")
    print("1. Inserir uma chave")
    print("2. Excluir uma chave")
    print("3. Buscar uma chave")
    print("4. Exibir a árvore")
    print("5. Sair")

def main():
    t = int(input("Digite o valor mínimo de chaves por nó (t): "))
    btree = BTree(t)

    conn, cursor = connect_db()
    
    # Inserir dados iniciais no banco de dados e na árvore B
    insert_initial_data(cursor, conn, btree)

    while True:
        print_menu()
        choice = input("Opção: ")

        if choice == "1":
            key = int(input("Digite a chave a ser inserida: "))
            value = input("Digite o valor associado à chave (ex: 'nome', 'idade', etc.): ")
            btree.insert((key, value))
            insert_to_db(cursor, conn, key, value)
            print(f"Chave {key} inserida com sucesso.")
        elif choice == "2":
            key = int(input("Digite a chave a ser excluída: "))
            btree.delete((key,))
            delete_from_db(cursor, conn, key)
            print(f"Chave {key} excluída com sucesso.")
        elif choice == "3":
            key = int(input("Digite a chave a ser buscada: "))
            node = btree.search(key)
            if node:
                for k, v in node.keys:
                    if k == key:
                        print(f"Chave {key} encontrada com valor '{v}'.")
                        break
            else:
                print(f"Chave {key} não encontrada.")
        elif choice == "4":
            print("Árvore B:")
            btree.traverse(btree.root)
            print()  # Nova linha para melhor formatação
        elif choice == "5":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

    conn.close()

if __name__ == "__main__":
    main()
