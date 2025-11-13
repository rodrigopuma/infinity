# 📋 Gerenciador de Tarefas (Python)

Um projeto simples de gerenciador de tarefas feito em Python, utilizando apenas programação funcional, arquivos JSON para armazenamento dos dados e interação via terminal.

---

## 🎯 Funcionalidades

- ✅ Criar tarefas com:

  - Nome
  - Descrição
  - Categoria
  - Prioridade (`alta`, `media`, `baixa`)
  - Status de conclusão

- ✅ Listar todas as tarefas
- ✅ Filtrar tarefas por prioridade
- ✅ Filtrar tarefas por categoria
- ✅ Marcar tarefa como concluída
- ✅ Atualizar dados da tarefa
- ✅ Remover tarefa
- ✅ Salvar e carregar tarefas em arquivo JSON automaticamente

---

## 🗂️ Estrutura do Projeto

```bash
gerenciador_tarefas/
├── main.py           # Arquivo principal (menu e execução)
├── tarefas.py        # Funções para manipular as tarefas (CRUD)
├── arquivos.py       # Funções de salvar/carregar arquivos JSON
├── lista_tarefa.json # Arquivo com as tarefas salvas (gerado automaticamente)
└── README.md
```

## 🎯 Funcionalidades

- ✅ Criar tarefas
- ✅ Salvar e carregar tarefas em arquivo JSON automaticamente

- Listar todas as tarefas:

  - Puxar do arquivo Json
  - Jogar para o Python
  - Tratar como lista de dicionarios
  - Devolver como lista de dicionarios ao úsuario

- Filtrar tarefas por prioridade
- Filtrar tarefas por categoria
- Marcar tarefa como concluída
- Atualizar dados da tarefa
- Remover tarefa
