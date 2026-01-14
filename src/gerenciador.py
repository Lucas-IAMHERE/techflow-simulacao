from enum import Enum

class Prioridade(Enum):
    ALTA = "Alta"
    MEDIA = "Média"
    BAIXA = "Baixa"

class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []
        self._next_id = 1