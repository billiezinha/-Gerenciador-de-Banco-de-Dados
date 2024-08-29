import time
from tabela import Tabela

esquema = {
    "id": int,
    "nome": str,
    "idade": int
}
tabela = Tabela("Clientes", esquema)

def medir_tempo_insercao(tabela, num_registros):
    inicio = time.time()
    for i in range(num_registros):
        tabela.inserir({"id": i, "nome": f"Cliente {i}", "idade": 30 + (i % 20)})
    fim = time.time()
    print(f"Tempo para inserir {num_registros} registros: {fim - inicio} segundos")

medir_tempo_insercao(tabela, 1000)
medir_tempo_insercao(tabela, 10000)
medir_tempo_insercao(tabela, 100000)


def medir_tempo_busca(tabela, num_buscas):
    inicio = time.time()
    for i in range(num_buscas):
        tabela.arvore_b.search(i)  # Busca pelo ID
    fim = time.time()
    print(f"Tempo para buscar {num_buscas} registros: {fim - inicio} segundos")


# medir_tempo_busca(tabela, 1000)
# medir_tempo_busca(tabela, 10000)
# medir_tempo_busca(tabela, 100000)

def medir_tempo_atualizacao(tabela, num_atualizacoes):
    inicio = time.time()
    for i in range(num_atualizacoes):
        tabela.atualizar(i, {"nome": f"Cliente Atualizado {i}", "idade": 40 + (i % 20)})
    fim = time.time()
    print(f"Tempo para atualizar {num_atualizacoes} registros: {fim - inicio} segundos")

# medir_tempo_atualizacao(tabela, 1000)
# medir_tempo_atualizacao(tabela, 10000)
# medir_tempo_atualizacao(tabela, 100000)

def medir_tempo_exclusao(tabela, num_exclusoes):
    inicio = time.time()
    for i in range(num_exclusoes):
        tabela.excluir(i)
    fim = time.time()
    print(f"Tempo para excluir {num_exclusoes} registros: {fim - inicio} segundos")


# medir_tempo_exclusao(tabela, 1000)
# medir_tempo_exclusao(tabela, 10000)
# medir_tempo_exclusao(tabela, 100000)

# !pip install memory-profiler

from memory_profiler import memory_usage
# from tabela import Tabela

# Função para medir o consumo de memória
def medir_memoria_insercao(tabela, num_registros):
    def inserir_dados():
        for i in range(num_registros):
            tabela.inserir({"id": i, "nome": f"Cliente {i}", "idade": 30 + (i % 20)})

    mem_inicial = memory_usage()[0]
    inserir_dados()
    mem_final = memory_usage()[0]
    print(f"Consumo de memória para inserir {num_registros} registros: {mem_final - mem_inicial} MB")


# medir_memoria_insercao(tabela, 1000)
# medir_memoria_insercao(tabela, 10000)
# medir_memoria_insercao(tabela, 100000)

def medir_memoria_atualizacao(tabela, num_atualizacoes):
    def atualizar_dados():
        for i in range(num_atualizacoes):
            tabela.atualizar(i, {"nome": f"Cliente Atualizado {i}", "idade": 40 + (i % 20)})

    mem_inicial = memory_usage()[0]
    atualizar_dados()
    mem_final = memory_usage()[0]
    print(f"Consumo de memória para atualizar {num_atualizacoes} registros: {mem_final - mem_inicial} MB")

# medir_memoria_atualizacao(tabela, 1000)
# medir_memoria_atualizacao(tabela, 10000)
medir_memoria_atualizacao(tabela, 100000)

def medir_memoria_exclusao(tabela, num_exclusoes):
    def excluir_dados():
        for i in range(num_exclusoes):
            tabela.excluir(i)

    mem_inicial = memory_usage()[0]
    excluir_dados()
    mem_final = memory_usage()[0]
    print(f"Consumo de memória para excluir {num_exclusoes} registros: {mem_final - mem_inicial} MB")


# medir_memoria_exclusao(tabela, 1000)
medir_memoria_exclusao(tabela, 10000)
# medir_memoria_exclusao(tabela, 100000


