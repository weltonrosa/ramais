'''
Cadastro de Ramais

Autor: Welton C. O. Rosa
Data: 26/01/2026

Ultima Atualização: 28/01/2026
Atualizado por: Welton C. O. Rosa

Versão: 1.0
Python Version: 
Bibliotecas: os, sys, Path, logging
Funções disponíveis: 

Exemplo de uso:
    

'''

import logging
import os
import sys
from pathlib import Path
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

basicConfig(
    level = DEBUG,
    format = '%(asctime)s: %(levelname)s:-* %(message)s',
    handlers = [file_handler, stream_handler]
)

os.system('cls' if os.name == 'nt' else 'clear')
margem1 = ' ' * 40
margem2 = ' ' * 10
separador = '=' * 80

decisao = -1
while decisao != 0:    
    print(margem1 + 'Menu Principal\n'
          + margem2 + separador + '\n\n'
          + margem1 +'[1] - Cadastrar Pessoa \n'
          + margem1 +'[2] - Listar Pessoas \n'
          + margem1 +'[0] - Sair \n\n'
          + margem2 + separador
         )
    try:
        decisao = int(input(margem1 + 'Escolha uma opção: '))
    except ValueError as e:
        print(margem1 +'Opção inválida. Por favor, digite um número.')
        logging.error('Erro de entrada inválida: %s', e)
        decisao = -1  # Continua no loop
        continue

    if decisao == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(margem1 + 'Cadastro de Pessoas\n')
        print(margem2 + separador + '\n')
        nome      = input(margem2 + 'Digite o nome.....: ')
        sobrenome = input(margem2 + 'Digite o sobrenome: ')
        idade     = int(input(margem2 + 'Digite a idade....: '))
        ramal     = input(margem2 + 'Digite o Ramal......: ')
        print(margem2 + separador + '\n')

        try:
            pessoa = Pessoa(nome, sobrenome, idade, ramal)
            PessoaController.salvar_pessoa(pessoa)
            print(margem1 + 'Pessoa cadastrada com sucesso!')
            input(margem1 + 'Pressione <<Enter>> para continuar...')
            logging.info('Pessoa cadastrada: %s', pessoa.nome_completo())
            os.system('cls' if os.name == 'nt' else 'clear')
        except Exception as e:
            print(f"{margem1} Erro ao cadastrar pessoa: {e}")
            logging.error('Erro ao cadastrar pessoa: %s', e)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
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
