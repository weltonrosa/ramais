# Documentação da Classe Pessoa
# Esta documentação descreve a classe Pessoa localizada em src/models/pessoa.py
# Autor: Welton Candido de Oliveira Rosa
# Data: 2024-06-15
# Versão: 1.0
# ------------------------------------------------------------------------------
# Sumário
# 1. Introdução
# 2. Atributos da Classe
# 3. Métodos da Classe	
# 4. Exemplo de Uso
# ------------------------------------------------------------------------------
# 1. Introdução
# A classe Pessoa representa uma entidade de pessoa com informações básicas como:
# Nome, Sobrenome, Idade e CPF.
# Ela é utilizada para modelar dados de pessoas em aplicações Python.
# ------------------------------------------------------------------------------
# 2. Atributos da Classe
# - nome (str): O primeiro nome da pessoa.
# - sobrenome (str): O sobrenome da pessoa.
# - idade (int): A idade da pessoa em anos.
# - cpf (str): O CPF da pessoa.
# ------------------------------------------------------------------------------
# 3. Métodos da Classe
# - __init__(self, nome: str, sobrenome: str, idade: int, cpf: str): Inicializa 
# - uma nova instância da classe Pessoa com os atributos fornecidos.
# - nome_completo(self) -> str: Retorna o nome completo da pessoa no formato "nome sobrenome".
# - apresentar(self) -> str: Retorna uma string de apresentação da pessoa, incluindo nome completo e idade.
# ------------------------------------------------------------------------------
# 4. Exemplo de Uso
# ```python
# from src.models.pessoa import Pessoa
#
# pessoa = Pessoa("João", "Silva", 30, "123.456.789-00")
# print(pessoa.nome_completo())  # Saída: João Silva
# print(pessoa.apresentar())     # Saída: Olá, meu nome é João Silva e tenho 30 anos.
# ```
# ------------------------------------------------------------------------------
