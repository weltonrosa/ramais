import os
import sys
from pathlib import Path

file = Path(__file__).resolve()
parent, root = file.parent, file.parents[2]
sys.path.append(str(root))

from src.models.pessoa import Pessoa
from src.controlers.pessoa import PessoaController

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
    except ValueError:
        print(margem1 +'Opção inválida. Por favor, digite um número.')
        decisao = -1  # Continua no loop
        continue

    if decisao == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(margem1 + 'Cadastro de Pessoas\n')
        print(margem2 + separador + '\n')
        nome      = input(margem2 + 'Digite o nome.....: ')
        sobrenome = input(margem2 + 'Digite o sobrenome: ')
        idade     = int(input(margem2 + 'Digite a idade....: '))
        cpf       = input(margem2 + 'Digite o CPF......: ')

        try:
            pessoa = Pessoa(nome, sobrenome, idade, cpf)
            PessoaController.salvar_pessoa(pessoa)
            os.system('cls' if os.name == 'nt' else 'clear')
            print(margem1 + 'Pessoa cadastrada com sucesso!')
        except Exception as e:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{margem1} Erro ao cadastrar pessoa: {e}")

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
