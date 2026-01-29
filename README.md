# Ramais
Aplicação de console para cadastro e consulta de ramais, desenvolvida em Python seguindo boas práticas de projeto através da arquitetura MVC (Model-View-Controller).

Descrição
- Projeto didático para gerenciar ramais (inserir, listar, atualizar e remover) via linha de comando.
- Organizado com separação clara entre `models`, `views` e `controlers` para facilitar manutenção e testes.

Principais conceitos
- Arquitetura: MVC — responsabilidades separadas entre camada de dados (`models`), lógica/controladores (`controlers`) e interface/entrada (`views`).
- Boas práticas: estrutura modular, testes automatizados, e código legível e testável.

Requisitos
- Python 3.10+ (ou versão compatível especificada em `requirements.txt`).

Instalação
1. Crie e ative um ambiente virtual:

```powershell
python -m venv .venv
& .\.venv\Scripts\Activate.ps1
```

2. Instale dependências:

```powershell
pip install -r requirements.txt
```

Uso
- Execute a aplicação a partir do módulo principal (ex.: `src.views.index`):

```powershell
python -m src.views.index
```

- A interface é via console; siga as instruções apresentadas para cadastrar, listar ou remover ramais.

Testes
- Execute a suíte de testes com `pytest`:

```powershell
pytest -q
```

Contribuição
- Abra issues para discutir mudanças e envie PRs com descrições claras das alterações.
- Siga o padrão de estilo e adicione testes para código novo.

Licença
- Consulte o arquivo `LICENSE` para os termos de uso.
