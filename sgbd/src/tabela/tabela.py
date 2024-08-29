from esquema.esquema import Esquema
from arvore_b.btree import BTree

class Tabela:
    def __init__(self, nome, esquema):
        self.nome = nome
        self.esquema = Esquema(esquema)
        self.arvore_b = BTree(3)  # Inicializa a Árvore B com grau mínimo (t)

    def inserir(self, registro):
        try:
            self.esquema.validar(registro)
            self.arvore_b.insert((registro['id'], registro))  # Insere o registro usando ID como chave
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

        # Corrige o nome do método para _exibir_arvore
        self._exibir_arvore(self.arvore_b.root, colunas, largura_colunas)

        print(header)

    def _exibir_arvore(self, node, colunas, largura_colunas):
        if node is not None:
            i = 0
            for i in range(len(node.keys)):
                if not node.is_leaf():
                    self._exibir_arvore(node.children[i], colunas, largura_colunas)
                registro = node.keys[i][1]  # A chave é uma tupla (id, registro)
                row = "|" + "|".join(f" {str(registro[coluna]):<{largura}} " for coluna, largura in zip(colunas, largura_colunas)) + "|"
                print(row)
            if not node.is_leaf():
                self._exibir_arvore(node.children[i + 1], colunas, largura_colunas)

    def atualizar(self, id_registro, novos_dados):
        node = self.arvore_b.search(id_registro)
        if node:
            for i, (id_chave, registro) in enumerate(node.keys):
                if id_chave == id_registro:
                    try:
                        for chave, valor in novos_dados.items():
                            if chave in self.esquema.esquema_desc:
                                if not isinstance(valor, self.esquema.esquema_desc[chave]):
                                    raise ValueError(f"Campo '{chave}' deve ser do tipo {self.esquema.esquema_desc[chave].__name__}")
                                registro[chave] = valor
                            else:
                                raise ValueError(f"Campo '{chave}' não faz parte do esquema da tabela")
                        node.keys[i] = (id_chave, registro)  # Atualiza o registro na árvore
                        print(f"Registro com ID {id_registro} atualizado com sucesso.")
                    except ValueError as e:
                        print(f"Erro ao atualizar registro: {e}")
                    return
        print(f"Registro com ID {id_registro} não encontrado na tabela '{self.nome}'.")

    def excluir(self, id_registro):
        print(f"Excluindo registro com ID {id_registro} da tabela '{self.nome}'")
        node = self.arvore_b.search(id_registro)
        if node:
            self.arvore_b.delete(id_registro)
            print(f"Registro com ID {id_registro} excluído com sucesso da tabela '{self.nome}'.")
        else:
            print(f"Registro com ID {id_registro} não encontrado na tabela '{self.nome}'.")


    def search(self, k, node=None):
        if node is None:
            node = self.root
        i = 0
        # Modificação aqui para comparar o primeiro elemento da tupla (o ID)
        while i < len(node.keys) and k > node.keys[i][0]:
            i += 1
        if i < len(node.keys) and k == node.keys[i][0]:
            return node
        elif node.is_leaf():
            return None
        else:
            return self.search(k, node.children[i])

