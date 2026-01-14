from enum import Enum

class Prioridade(Enum):
    ALTA = "Alta"
    MEDIA = "Média"
    BAIXA = "Baixa"

class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []
        self._next_id = 1

    def adicionar_tarefa(self, titulo, descricao, prioridade=Prioridade.MEDIA):
        tarefa = {
            "id": self._next_id,
            "titulo": titulo,
            "descricao": descricao,
            "prioridade": prioridade.value,
            "concluida": False
        }
        self.tarefas.append(tarefa)
        self._next_id += 1
        return tarefa