import secrets
import string
import random
from typing import List

# ==============================================================================
# ⚠️ CONFIGURAÇÃO CRÍTICA
# Define o comprimento máximo de caracteres (usado apenas para informação)
MAX_COMPRIMENTO_PERMITIDO = 256 

# Configuração FIXA da Senha FORTE (Não Customizável)
COMPRIMENTO_FIXO = 16
REQ_MIN_MIN = 4
REQ_MIN_MAI = 4
REQ_MIN_NUM = 4
REQ_MIN_SIM = 4
# ==============================================================================

# Definições Padrão
MINUSCULAS = string.ascii_lowercase
MAIUSCULAS = string.ascii_uppercase
NUMEROS = string.digits
SIMBOLOS = '!@#$%^&*()-_+=[]{}|;:,.<>?' 

def gerar_senha_fixa() -> str:
    """
    Gera uma senha forte usando os requisitos fixos definidos no topo do script.
    """
    senha: List[str] = []
    
    total_len = COMPRIMENTO_FIXO
    req_minusculas = REQ_MIN_MIN
    req_maiusculas = REQ_MIN_MAI
    req_numeros = REQ_MIN_NUM
    req_simbolos = REQ_MIN_SIM
    
    total_requerido = req_minusculas + req_maiusculas + req_numeros + req_simbolos
    
    # 1. Checagem de sanidade (Caso as constantes sejam mal configuradas)
    if total_requerido > total_len:
        return f"Erro Crítico: As constantes internas ({total_requerido}) excedem o comprimento total fixo ({total_len}). Verifique o código."
    
    # 2. Garantir a Cota Obrigatória
    senha.extend(secrets.choice(MINUSCULAS) for _ in range(req_minusculas))
    senha.extend(secrets.choice(MAIUSCULAS) for _ in range(req_maiusculas))
    senha.extend(secrets.choice(NUMEROS) for _ in range(req_numeros))
    senha.extend(secrets.choice(SIMBOLOS) for _ in range(req_simbolos))
    
    # 3. Preencher o Restante
    caracteres_disponiveis = MINUSCULAS + MAIUSCULAS + NUMEROS + SIMBOLOS
    restante = total_len - len(senha)
    senha.extend(secrets.choice(caracteres_disponiveis) for _ in range(restante))
    
    # 4. Embaralhar e Retornar
    random.shuffle(senha)
    return "".join(senha)

# --- Exemplo de Uso (Função Principal) ---

if __name__ == "__main__":
    print("--- Gerador de Senhas Forte Simples e Rápido ---")
    
    print("\n--- Configuração de Senha Fixa ---")
    print(f"Comprimento: {COMPRIMENTO_FIXO} (Máx: {MAX_COMPRIMENTO_PERMITIDO})")
    print(f"Requisitos Mínimos (4 de cada): Minúsculas, Maiúsculas, Números, Símbolos.")
    print("------------------------------------------")

    
    escolha = input("Deseja Gerar a Senha Forte? (S/n) ").strip().upper()
    
    if escolha == 'S' or escolha == '':
        
        print("\nGerando Senha...")
        senha_gerada = gerar_senha_fixa()
        
        # Imprimir o resultado
        if senha_gerada.startswith("Erro Crítico:"):
            print("\n" + "="*40)
            print(senha_gerada)
            print("="*40)
        else:
            print("\n" + "="*40)
            print(f"✔️ SENHA FORTE GERADA ({len(senha_gerada)} caracteres):")
            print(f"** {senha_gerada} **")
            print("="*40)
    else:
        print("\nOperação Cancelada. Nenhuma senha foi gerada.")
