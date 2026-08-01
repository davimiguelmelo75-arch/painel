
import os
import socket
class Painel1:
    def __init__(self):
        self.nome = "1"
        # Cores ANSI
        self.VERDE = "\033[92m"
        self.AZUL = "\033[96m"
        self.AMARELO = "\033[93m"
        self.VERMELHO = "\033[91m"
        self.RESET = "\033[0m"

    def scan_portas_nativo(self, alvo):
        """Faz a varredura sem precisar do Nmap instalado"""
        print(f"\n{self.AZUL}[*] Escaneando portas principais em {alvo}...{self.RESET}\n")
        
        # Lista das portas mais comuns para testar
        portas = [21, 22, 23, 25, 53, 80, 110, 443, 8080, 3306]
        
        # Limpa o domínio caso o usuário digite com http://
        alvo_limpo = alvo.replace("http://", "").replace("https://", "").split("/")[0]
        
        try:
            ip = socket.gethostbyname(alvo_limpo)
            print(f"{self.VERDE}[+] IP Resolvido: {ip}{self.RESET}\n")
        except socket.gaierror:
            print(f"{self.VERMELHO}[-] Não foi possível resolver o domínio/IP.{self.RESET}")
            return

        print("PORTA     STATUS")
        print("-----------------")
        for porta in portas:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1.0) # Tempo limite de conexão
            resultado = sock.connect_ex((ip, porta))
            
            if resultado == 0:
                print(f"{porta}/tcp    {self.VERDE}ABERTA{self.RESET}")
            else:
                print(f"{porta}/tcp    {self.VERMELHO}FECHADA{self.RESET}")
            sock.close()

    def abrir_interface(self):
        while True:
            os.system("clear" if os.name != "nt" else "cls")
            print(f"{self.AZUL}┌──────────────────────────────────────────┐{self.RESET}")
            print(f"{self.AZUL}│            INTERFACE / PAINEL: {self.VERDE}{self.nome}{self.AZUL}     │{self.RESET}")
            print(f"{self.AZUL}└──────────────────────────────────────────┘{self.RESET}\n")
            print(f" {self.VERDE}[1]{self.RESET} Executar Scan de Portas Nativo")
            print(f" {self.VERDE}[0]{self.RESET} Sair")
            print("──────────────────────────────────────────")

            opcao = input(f"{self.AMARELO}Opção > {self.RESET}").strip()

            if opcao == "1":
                alvo = input("\nDigite o IP ou Site (ex: scanme.nmap.org): ").strip()
                if alvo:
                    self.scan_portas_nativo(alvo)
                input("\nPressione ENTER para voltar...")
            elif opcao == "0":
                print("\nEncerrando painel...")
                break
