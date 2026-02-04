'''
Cadastro de Ramais

Autor: Welton C. O. Rosa
Data: 26/01/2026

Ultima Atualização: 02/02/2026
Atualizado por: Welton C. O. Rosa

Versão: 1.0
Python Version: 
Bibliotecas: os, sys, Path, logging, re
Funções disponíveis: 

Exemplo de uso:
    
python src/views/index.py ou
python -m src.views.index

'''

import logging
import os
import sys
import csv
from pathlib import Path
from typing import Optional
from logging import CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET, basicConfig
from logging import FileHandler, StreamHandler

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[2]
sys.path.append(str(root))

from src.models.pessoa import Pessoa
from src.controlers.pessoa import PessoaController

file_handler = FileHandler('ramais.log', encoding='utf-8', mode='a')
file_handler.setLevel(WARNING)

stream_handler = StreamHandler()
stream_handler.setLevel(WARNING)

basicConfig(
    level = DEBUG,
    format = '%(asctime)s: %(levelname)s:-* %(message)s',
    handlers = [file_handler, stream_handler]
)

os.system('cls' if os.name == 'nt' else 'clear')
margem1 = ' ' * 40
margem2 = ' ' * 10
separador = '=' * 80

def solicitar_campo(prompt: str, validator=None) -> Optional[str]:
    while True:
        valor = input(margem2 + f"{prompt}: ").strip()
        if valor.lower() == 'esc':
            return None
        if validator and not validator(valor):
            print(margem2 + 'Entrada inválida. Tente novamente ou digite ESC para cancelar.')
            continue
        return valor


def obter_formulario() -> Optional[dict]: 
    print(margem1 + 'Preencha os dados (digite ESC a qualquer momento para cancelar):\n')
    nome_completo = solicitar_campo('Nome Completo', lambda v: len(v) > 0)
    if nome_completo is None:
        return None
    ramal = solicitar_campo('Ramal', lambda v: v.isdigit())
    if ramal is None:
        return None
    departamento = solicitar_campo('Departamento', lambda v: len(v) > 0)
    if departamento is None:
        return None
    secretaria = solicitar_campo('Secretaria', lambda v: len(v) > 0)
    if secretaria is None:
        return None
    return {
        'nome_completo': nome_completo,
        'ramal': ramal,
        'departamento': departamento,
        'secretaria': secretaria
    }

decisao = -1
while decisao != 0:
    os.system('cls' if os.name == 'nt' else 'clear')    
    print(margem1 + 'Menu Principal\n'
          + margem2 + separador + '\n\n'
          + margem1 +'[ 1 ] - Cadastrar Pessoa \n'
          + margem1 +'[ 2 ] - Listar Pessoas \n'
          + margem1 +'[ 0 ] - Sair \n\n'
          + margem2 + separador
         )
    try:
        decisao = int(input(margem1 + 'Escolha uma opção: '))
        logging.debug('Opção escolhida no menu principal: %d', decisao)
    except ValueError as e:
        input(margem1 +'Opção inválida, pressione <<Enter>> para continuar.')
        logging.error('Erro de entrada inválida no menu principal: %s', e)
        decisao = -1  # Continua no loop
        continue

    if decisao == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        form = obter_formulario()
        if form is None:
            input(margem2 + 'Operação cancelada. Pressione <<Enter>> para continuar...')
            continue

        print('\n' + margem2 + separador + '\n')
        print(margem2 + 'Confirme os dados:')
        print(margem2 + f"Nome Completo: {form['nome_completo']}")
        print(margem2 + f"Ramal: {form['ramal']}")
        print(margem2 + f"Departamento: {form['departamento']}")
        print(margem2 + f"Secretaria: {form['secretaria']}")
        confirmar = input(margem2 + 'Confirma o cadastro? (s/n): ').strip().lower()
        if confirmar.startswith('s'):
            csv_file = root / 'ramais.csv'
            try:
                write_header = not csv_file.exists()
                with open(csv_file, 'a', encoding='utf-8', newline='') as f:
                    writer = csv.writer(f)
                    if write_header:
                        writer.writerow(['nome_completo', 'ramal', 'departamento', 'secretaria'])
                    writer.writerow([form['nome_completo'], form['ramal'], form['departamento'], form['secretaria']])
                print(margem2 + 'Dados cadastrados com sucesso! (salvo em ramais.csv)')
                logging.info('Cadastro salvo: %s', form)
            except Exception as e:
                print(margem2 + f'Erro ao salvar os dados: {e}')
                logging.error('Erro ao salvar cadastro: %s', e)
        else:
            print(margem2 + 'Cadastro cancelado.')
        input(margem2 + 'Pressione <<Enter>> para continuar...')
        os.system('cls' if os.name == 'nt' else 'clear')

    elif decisao == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        pessoas = PessoaController.listar_pessoas()
        print(margem1 + 'Listagem de Pessoas Cadastradas')
        print(margem2 + separador + '\n')
        for p in pessoas:
            print(f'{margem2} {p.apresentar()}')
        print('\n' + margem2 + separador + '\n')
        input(margem2 + 'Pressione <<Enter>> para continuar...')
        os.system('cls' if os.name == 'nt' else 'clear')
