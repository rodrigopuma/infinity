import json

def gerador_id(reiniciar=False):
    with open("./data/IDS.json", "r", encoding="utf-8") as f:
        try:
            ids = json.load(f)
        except:
            ids = {
                "ativos": [],
                "inativos": []
                }
    try:
        maior_id_ativo = max(ids["ativos"])
    except ValueError:
        maior_id_ativo = 0
        tem_id_ativo = False
    else:
        tem_id_ativo = True
    try:
        maior_id_inativo = max(ids["inativos"])
    except ValueError:
        maior_id_inativo = 0
        tem_id_inativo = False
    else:
        tem_id_inativo = True
    
    id_gerado = max(maior_id_ativo if tem_id_ativo else 0, maior_id_inativo if tem_id_inativo else 0)
    if id_gerado > 0 and (tem_id_ativo or tem_id_inativo):
        id_gerado += 1
    elif id_gerado == 0 and (tem_id_ativo or tem_id_inativo):
        id_gerado = 1
    else:
        id_gerado = 0
    ids["ativos"].append(id_gerado)
    with open("./data/IDS.json", "w", encoding="utf-8") as f:
        json.dump(ids, f, ensure_ascii=False, indent=4)
    if reiniciar:
        return 0
    return id_gerado

def validador_resposta(choice, *args):
    while choice not in args:
        print(f'Escolha inválida. Opções válidas: {args}')
        choice = input('Selecione: ')
    return choice

def solicitar_id(mensagem: str):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print('Digite um número válido.')