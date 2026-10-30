# TED 03 – Gerenciador de Persistência de Dados em Arquivos Estruturados (CSV e JSON)

Projeto desenvolvido para a disciplina de **Algoritmos e Programação Avançada**, correspondente ao **TED 03**. Este módulo implementa um sistema seguro de persistência de dados focado no controle de docentes e disciplinas, realizando operações de leitura, escrita e conversão bidirecional entre arquivos estruturados (`.csv` e `.json`).

##  Integrantes da Dupla
* Gabriel Silva da Rocha (17.1.51556)  
* Vitor Feldkircher (26.1.18554)

##  Funcionalidades Implementadas

* **Conversão Bidirecional:** Converte dados tabulares (CSV delimitado por `;`) para estruturas aninhadas (JSON indentado) sem perda de informações.
* **Gerenciamento de Contexto (`with open`):** Garante a liberação segura de recursos e o descarregamento de buffers do sistema operacional, prevenindo corrupção de arquivos.
* **Codificação Segura:** Utiliza `UTF-8` em todas as operações para preservar acentos e caracteres especiais do português.
* **Backup Preventivo Automático:** Utiliza a biblioteca `shutil` para gerar cópias de segurança datadas (ex: `_backup_20261029_004557`) de qualquer arquivo antes de ele ser sobrescrito.
* **Tratamento Robusto de Exceções (E/S):** Captura e trata erros específicos das famílias `OSError` e `ValueError`, incluindo `FileNotFoundError`, `PermissionError`, `UnicodeDecodeError` e `JSONDecodeError`.

##  Tecnologias Utilizadas
* **Linguagem:** Python 3.14
* **Bibliotecas Nativas:** `csv`, `json`, `shutil`, `pathlib`, `datetime` (Nenhuma dependência externa é necessária).

##  Como Executar e Testar

1. Clone este repositório ou baixe os arquivos em uma mesma pasta.
2. Certifique-se de que os arquivos de origem `professores.csv` e `professores.json` estão presentes no diretório raiz.
3. Abra o terminal na pasta do projeto e execute o script principal:

```bash
python gerenciador.py