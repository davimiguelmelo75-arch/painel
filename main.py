import os
import sys
import time

SENHA_CORRETA = "larp123"

def limpar_tela():
    os.system('clear' if os.name != 'nt' else 'cls')

def login():
    limpar_tela()
    print("┌──────────────────────────────────────────────┐")
    print("│         🔒 SISTEMA DE AUTENTICAÇÃO           │")
    print("└──────────────────────────────────────────────┘")
    
    tentativas = 3
    while tentativas > 0:
        senha = input("\n🔑 Digite a chave de acesso: ").strip()
        
        if senha == SENHA_CORRETA:
            print("\n[+] Chave validada! Acessando sistema...")
            time.sleep(1)
            limpar_tela()  # Limpa tudo antes de exibir o painel principal!
            return True
        else:
            tentativas -= 1
            if tentativas > 0:
                print(f"[-] Chave incorreta! Tentativas restantes: {tentativas}")
            else:
                print("\n[!] Acesso bloqueado por excesso de tentativas.")
                sys.exit()

def menu_painel():
    while True:
        print("==================================================")
        print("           ⚡ PAINEL DE CONTROLE v2.0 ⚡           ")
        print("==================================================")
        print("  Desenvolvido por: Davi")
        print("--------------------------------------------------")
        print("  [1] 📡 Executar Scan de Portas Nativo")
        print("  [2] 🔄 Limpar Tela")
        print("  [0] 🚪 Sair do Painel")
        print("==================================================")
        
        opcao = input("\n[Painel]> ").strip()
        
        if opcao == "1":
            limpar_tela()
            print("==================================================")
            print("              📡 SCAN DE PORTAS                   ")
            print("==================================================")
            print("\n[!] Iniciando varredura no alvo...")
            # Cole aqui o seu código do scan
            input("\nPressione ENTER para voltar ao menu...")
            limpar_tela()
            
        elif opcao == "2":
            limpar_tela()
            
        elif opcao == "0":
            limpar_tela()
            print("Saindo do sistema... Até logo!")
            sys.exit()
            
        else:
            limpar_tela()
            print("⚠️ Opção inválida! Tente novamente.\n")

if __name__ == "__main__":
    if login():
        menu_painel()
