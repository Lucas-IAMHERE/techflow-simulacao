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