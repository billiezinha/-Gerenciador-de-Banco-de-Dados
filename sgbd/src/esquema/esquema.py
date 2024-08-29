class Esquema:
    def __init__(self, esquema_desc):
        self.esquema_desc = esquema_desc

    def validar(self, registro):
        for chave, valor in registro.items():
            tipo_esperado = self.esquema_desc.get(chave)
            if tipo_esperado and not isinstance(valor, tipo_esperado):
                raise ValueError(f"Valor inválido para a coluna '{chave}'. Esperado {tipo_esperado.__name__}, obtido {type(valor).__name__}.")
