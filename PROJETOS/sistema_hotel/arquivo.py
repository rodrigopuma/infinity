from classes import Hotel, Funcionario, Quarto, Reserva
import json

ARQUIVO_FUNCIONARIOS = 'db/funcionarios.json'
ARQUIVO_QUARTOS = 'db/quartos.json'
ARQUIVO_RESERVAS = 'db/reservas.json'

def ler_arquivo(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as arch_json:
        try:
            return json.load(arch_json)
        except json.decoder.JSONDecodeError:
            return []
        
def escrever_arquivo(arquivo, obj_dict):
    lista = ler_arquivo(arquivo)
    lista.append(obj_dict)
    
    with open(arquivo, 'w', encoding='utf-8') as arch_db:
        json.dump(lista, arch_db, indent=4, ensure_ascii=False)
