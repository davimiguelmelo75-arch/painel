import sys
import time

# Senha direta para testes
SENHA_CORRETA = "larp123"

def login():
    print("========================================")
    print("       🔒 ACESSO RESTRITO - DAVI        ")
    print("========================================")
    
    tentativas = 3
    while tentativas > 0:
        senha = input("\n🔑 Digite a senha para entrar: ").strip()
        
        if senha == SENHA_CORRETA:
            print("\n✅ Acesso liberado! Abrindo o painel...")
            time.sleep(1)
            return True
        else:
            tentativas -= 1
            if tentativas > 0:
                print(f"❌ Senha incorreta! Tentativas restantes: {tentativas}")
            else:
                print("\n🚫 Acesso bloqueado por muitas tentativas erradas!")
                sys.exit()

def menu_painel():
    print("\n========================================")
    print("       INTERFACE / PAINEL: 1            ")
    print("========================================")
    print("[1] Executar Scan de Portas Nativo")
    print("[0] Sair")
    
    opcao = input("\nOpção > ")
    if opcao == "1":
        print("\n[!] Executando scan...")
    elif opcao == "0":
        print("\nEncerrando painel...")
        sys.exit()
    else:
        print("\nOpção inválida!")

if __name__ == "__main__":
    if login():
        menu_painel()
