from colorama import init, Fore, Style
import stdiomask
from time import sleep
#biblioteca msvcrt (Microsoft Visual C Runtime) para obter entrada de teclado no console
import msvcrt

init(autoreset=True)


# limpar a tela do terminal
def clear_screen():
    print("\033c", end="")

# imprimir menu no terminal
def print_menu(items, selected_item):
    clear_screen()
    for i, item in enumerate(items):
        if i == selected_item:
            print(f"{Fore.GREEN}>>> {item}{Style.RESET_ALL}")
        else:
            print(f"    {item}")

# Fazer login
def fazer_login():
    login = input(f"{Fore.YELLOW}Nome:{Style.RESET_ALL} ")
    senha = stdiomask.getpass(prompt=f'{Fore.YELLOW}Senha:{Style.RESET_ALL} ', mask='')
    return(login, senha)

def search__user(login, senha):
    usuarios = []
    try:
        with open('usuarios.txt', 'r+', encoding='Utf-8', newline='') as arquivo:
            for linha in arquivo:
                linha = linha.strip(",")
                usuarios.append(linha.split())
            for usuario in usuarios:
                nome = usuario[0]
                password = usuario[1]
                if login == nome and senha == password:
                    return True
    except FileNotFoundError:
        raise Exception("Usuário não encontrado. :'( ")

def Menu():
    items = [
        "Cadastrar usuário",
        "Fazer login",
        "Sair"
    ]
    selected_item = 0

    while True:
        clear_screen()
        print_menu(items, selected_item)

        key = msvcrt.getch()

        if key == b'\xe0':
            key = msvcrt.getch()

            if key == b'H':     # Seta para cima
                selected_item = (selected_item - 1) % len(items)
            elif key ==b'P':    # Seta para Baixo
                selected_item = (selected_item + 1) % len(items)
        elif key == b'\r':     # Tecla enter
            clear_screen()
            if selected_item == 0:  # Cadastrar usuário
                login, senha = fazer_login()
                if login == senha:
                    print()
                    print(f'Sua {Fore.LIGHTCYAN_EX}senha{Style.RESET_ALL} deve ser {Fore.LIGHTRED_EX}diferente{Style.RESET_ALL} do {Fore.LIGHTCYAN_EX}login{Style.RESET_ALL}.')
                    print()
                    exit()
                user = search__user(login, senha)
                if user == True:
                    print()
                    print(f'Usuário {Fore.RED}já existe{Style.RESET_ALL}!')
                    print()
                    sleep(2)
                    exit()
                else:
                    with open('usuarios.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
                        arquivo.writelines(f'{login}    {senha}\n')
                    print()
                    print(f"{Fore.CYAN}Cadastro aprovado!{Style.RESET_ALL}")
                    print()
                    exit()

            elif selected_item == 1:    # Fazer Login
                login, senha = fazer_login()
                user = search__user(login, senha)
                if user == True:
                    print()
                    print(f"{Fore.CYAN}Login realizado com sucesso!{Style.RESET_ALL}")
                    print()
                    sleep(1)
                    exit()
                else:
                    print()
                    print(f"{Fore.RED}Nome ou senha inválidos{Style.RESET_ALL}")
                    print()
                    sleep(2)
            else:
                clear_screen()
                print()
                print(f"{Fore.GREEN}O programa foi encerrado com sucesso!{Style.RESET_ALL}")
                print()
            break


# Chama a função para iniciar o programa
Menu()