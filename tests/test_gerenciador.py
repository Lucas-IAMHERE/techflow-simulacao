import pytest
from src.gerenciador import GerenciadorTarefas, Prioridade

def test_adicionar_tarefa():
    gerenciador = GerenciadorTarefas()
    tarefa = gerenciador.adicionar_tarefa("Estudar", "Revisar Python")
    assert len(gerenciador.listar_tarefas()) == 1
    assert tarefa["titulo"] == "Estudar"

def test_prioridade_padrao():
    gerenciador = GerenciadorTarefas()
    tarefa = gerenciador.adicionar_tarefa("Teste", "Desc")
    assert tarefa["prioridade"] == "Média"

    def test_excluir_tarefa():
    gerenciador = GerenciadorTarefas()
    t = gerenciador.adicionar_tarefa("Lixo", "Remover")
    gerenciador.excluir_tarefa(t["id"])
    assert len(gerenciador.listar_tarefas()) == 0

def test_atualizar_prioridade():
    gerenciador = GerenciadorTarefas()
    t = gerenciador.adicionar_tarefa("Urgente", "Mudar pra alta", Prioridade.BAIXA)
    gerenciador.atualizar_prioridade(t["id"], Prioridade.ALTA)
    # Busca a tarefa atualizada na lista
    tarefa_atualizada = gerenciador.listar_tarefas()[0]
    assert tarefa_atualizada["prioridade"] == "Alta"