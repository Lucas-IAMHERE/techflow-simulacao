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
    

    def listar_tarefas(self):
        return self.tarefas

    def excluir_tarefa(self, id_tarefa):
        for index, tarefa in enumerate(self.tarefas):
            if tarefa["id"] == id_tarefa:
                del self.tarefas[index]
                return True
        return False
    
    def atualizar_prioridade(self, id_tarefa, nova_prioridade):
        for tarefa in self.tarefas:
            if tarefa["id"] == id_tarefa:
                tarefa["prioridade"] = nova_prioridade.value
                return True
        return False