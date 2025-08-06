# Gerenciador de Tarefas em Linha de Comando

Este é um projeto simples de gerenciamento de tarefas desenvolvido em Python. Ele permite que você organize suas tarefas diárias diretamente do terminal, com opções para criar, visualizar, atualizar, remover e filtrar tarefas.

---

## Funcionalidades

O Gerenciador de Tarefas oferece as seguintes funcionalidades:

---

- Criar Tarefa: Adicione uma nova tarefa com nome, descrição, prioridade e categoria.

- Listar Tarefas: Visualize todas as tarefas salvas em uma lista organizada.

- Marcar como Concluída: Altere o status de uma tarefa para "concluída".

- Remover Tarefa: Exclua uma tarefa específica da sua lista.

- Filtrar por Prioridade: Exiba apenas as tarefas com prioridade "alta", "média" ou "baixa".

- Filtrar por Categoria: Exiba as tarefas pertencentes a uma categoria específica (por exemplo, "trabalho", "estudo", "pessoal").

- Atualizar Tarefa: Edite os detalhes de uma tarefa existente.

---

## Como Usar

### Pré-requisitos

---

Certifique-se de que você tem o Python 3 instalado em sua máquina.

Executando o Projeto
Clone o repositório.

---

Navegue até a pasta do projeto pelo terminal e execute o `main.py`

Bash

```
cd "PROJETOS/PROJETO FUNÇÕES"
python main.py
```

Um menu interativo aparecerá no terminal, e você poderá escolher a opção desejada.

## Estrutura do Projeto

O projeto é dividido em três arquivos principais e um arquivo **`.json`** para armazenamento:

- **`main.py`**: O arquivo principal que contém o `menu interativo` e a `lógica central` do programa.

- **`funcoes.py`**: Módulo que agrupa todas as funções de manipulação das tarefas, como `criar`, `remover`, `atualizar` e `exibir`.

- **`tarefa.py`**: Módulo responsável pela leitura e escrita do arquivo `tarefas.json`, garantindo que as tarefas sejam `salvas e carregadas` de forma persistente.

- **`tarefas.json`**: Arquivo responsável pelo `armazenamento das tarefas`.

## Contribuição

Contribuições são `bem-vindas!` Se você tiver sugestões de melhoria, novas funcionalidades ou quiser corrigir um bug, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Exemplo de Uso

Ao executar o `main.py`, você verá algo assim:

```
Menu de Tarefas
[0] - Criar Tarefa
[1] - Ver todas as Tarefas
[2] - Marcar Tarefa como concluída
[3] - Remover Tarefa
[4] - Filtrar por prioridade
[5] - Filtrar por categoria
[6] - Atualizar Tarefa
Qual opção você deseja:
```
