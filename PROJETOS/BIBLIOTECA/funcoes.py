# from main import ARQUIVO_LIVROS, ARQUIVO_USUARIOS
import json

biblioteca = []
usuarios = []
informacoes_livro = {
    'id': int,
    'titulo': str,
    'autor': str,
    'copias': int
}

ARQUIVO_LIVROS = 'livros.json'
ARQUIVO_USUARIOS = 'usuarios.json'

def renovar_ids():
    biblioteca = listar_livros()
    contador = 0
    for livro in biblioteca:
        contador += 1
        livro['id'] = contador
    with open(ARQUIVO_LIVROS, 'w', encoding='utf-8') as arquivo:
        return json.dump(biblioteca, arquivo, indent=4, ensure_ascii=False)

def listar_livros(path=ARQUIVO_LIVROS):
    with open(path, 'r', encoding='utf-8') as arquivo:
        return list(json.load(arquivo))

def verificar_qtd_livros(titulo: None):
    titulo = input('Digite o titulo do livro que deseja ver: ') if titulo is None else titulo
    biblioteca = listar_livros()
    for livro in biblioteca:
        if livro['titulo'] == titulo:
            qtd_livros = livro['copias']
            print(f'Temos {qtd_livros} cópias desse livro no estoque')
            return int(qtd_livros)

    
def adicionar_livros():
    biblioteca = listar_livros() # antiga
    for informacao in informacoes_livro:
        if informacao == 'id':
            continue
        informacoes_livro[informacao] = input(f'{informacao}: ')
    biblioteca.append(informacoes_livro) # nova
    renovar_ids()
    with open(ARQUIVO_LIVROS, 'w', encoding='utf-8') as arquivo:
        json.dump(biblioteca, arquivo, indent=4, ensure_ascii=False)
    
    

verificar_qtd_livros('MVFS')

