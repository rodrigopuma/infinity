import utils.menu as M
from utils.funtions import limpar_terminal
from utils.create import create_product, vender
from utils.read import retornar_produtos
limpar_terminal()

state = ""

while True:
    if state == "main_choice" or state == "":
        state = "main_choice"
        main_choice = M.main_menu()
        limpar_terminal()
    
    match main_choice:
        case 1:
            state = "produto_choice"
            produto_choice = M.menu_produto()
            limpar_terminal()
            match produto_choice:
                case 1:
                    create_product()
                case 2:
                    retornar_produtos(listar_produtos=True)
                    limpar_terminal()
                case 3:
                    ... # editar
                case 4:
                    ... # remover
                case 5:
                    continue # voltar
        case 2:
            venda_choice = M.menu_venda()
            limpar_terminal()
            match venda_choice:
                case 1:
                    ... # criar
                case 2:
                    ... # listar
                case 3:
                    ... # editar
                case 4:
                    ... # remover
                case 5:
                    continue # voltar
