import csv
import json
import shutil
from datetime import datetime
from pathlib import Path

def criar_backup(caminho_arquivo):
    """Gera um backup automático dos dados originais antes de qualquer alteração."""
    arquivo_obj = Path(caminho_arquivo)
    
    if arquivo_obj.exists():
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nome_backup = f"{arquivo_obj.stem}_backup_{timestamp}{arquivo_obj.suffix}"
        caminho_backup = arquivo_obj.with_name(nome_backup)
        
        try:
            shutil.copy2(arquivo_obj, caminho_backup)
            print(f"[Segurança] Backup gerado com sucesso: {caminho_backup.name}")
        except PermissionError:
            print(f"[Erro de E/S] Sem permissão para fazer backup de '{caminho_arquivo}'.")
        except OSError as e:
            print(f"[Erro de E/S] Falha na operação de backup: {e}")

def converter_csv_para_json(origem, destino):
    """Lê dados estruturados de um CSV e converte para JSON."""
    try:
        with open(origem, mode='r', encoding='utf-8', newline='') as arquivo_csv:
            leitor = csv.DictReader(arquivo_csv, delimiter=';')
            dados = list(leitor)
            
        criar_backup(destino)
        
        with open(destino, mode='w', encoding='utf-8') as arquivo_json:
            json.dump(dados, arquivo_json, ensure_ascii=False, indent=4)
            
        print(f"[Conversão] Sucesso: '{origem}' foi convertido para '{destino}'.")

    except FileNotFoundError:
        print(f"[Erro de Acesso] O arquivo origem '{origem}' não foi encontrado.")
    except UnicodeDecodeError:
        print(f"[Erro de Conteúdo] Falha de codificação. '{origem}' não é um UTF-8 válido.")
    except Exception as e:
        print(f"[Erro Inesperado] {e}")

def converter_json_para_csv(origem, destino):
    """Lê uma estrutura JSON e a converte para o formato CSV."""
    try:
        with open(origem, mode='r', encoding='utf-8') as arquivo_json:
            dados = json.load(arquivo_json)
            
        if not dados:
            print("[Aviso] O arquivo JSON fornecido não contém dados.")
            return

        criar_backup(destino)
        
        with open(destino, mode='w', encoding='utf-8', newline='') as arquivo_csv:
            cabecalho = dados[0].keys()
            escritor = csv.DictWriter(arquivo_csv, fieldnames=cabecalho, delimiter=';')
            
            escritor.writeheader()
            escritor.writerows(dados)
            
        print(f"[Conversão] Sucesso: '{origem}' foi convertido para '{destino}'.")

    except FileNotFoundError:
        print(f"[Erro de Acesso] O arquivo origem '{origem}' não existe.")
    except json.JSONDecodeError as e:
        print(f"[Erro de Conteúdo] O JSON '{origem}' está corrompido. Linha: {e.lineno}.")
    except PermissionError:
        print(f"[Erro de E/S] Permissão negada para salvar em '{destino}'.")
    except Exception as e:
        print(f"[Erro Inesperado] {e}")

if __name__ == "__main__":
    print("\n--- INICIANDO GERENCIADOR DE PERSISTÊNCIA (DOCENTES) ---")
    
    print("\n1. Testando: CSV -> JSON")
    converter_csv_para_json("professores.csv", "saida_professores.json")
    
    print("\n2. Testando: JSON -> CSV")
    converter_json_para_csv("professores.json", "saida_professores.csv")
    
    print("\n3. Testando: Backup Automático (Sobrescrevendo arquivo recém-criado)")
    converter_csv_para_json("professores.csv", "saida_professores.json")
    
    print("\n4. Testando: Tratamento de Exceções de Acesso")
    converter_csv_para_json("arquivo_inexistente.csv", "teste.json")
    
    print("\n5. Testando: Tratamento de Exceções de Conteúdo (Corrompido)")
    Path("corrompido.json").write_text("{ \"professor\": \"Jakson\"", encoding="utf-8")
    converter_json_para_csv("corrompido.json", "teste.csv")
    print("-" * 56)