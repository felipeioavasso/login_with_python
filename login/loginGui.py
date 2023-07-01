import os
import PySimpleGUI as sg

# Definindo o Layout da janela

class LoginGui:
    def __init__(self):
        
        sg.theme('BlueMono')
        layout = [
            [sg.T("", size=(1,1))],
            [sg.Text(" Nome: ", expand_x=True), sg.Input(size=(100,1), justification="left", key="nome")],
            [sg.Text("Senha: ", expand_x=True), sg.Input(size=(100,1), justification="left", key="senha", password_char="*")],
            [sg.T("", size=(1,1))],
            [sg.T("", size=(5,1)), sg.Button("Fazer Login"), sg.Button("Cadastrar usuário")], 
        ]
    
    # Declarar janela
        self.janela = sg.Window("Login", layout, size=(300,150))

    def run(self):
        while True:
            event, values = self.janela.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == "Fazer Login":
                login = values["nome"]
                senha = values["senha"]
                user = search_user(login, senha)
                if user:
                    sg.popup("Login realizado com sucesso!")
                else:
                    sg.popup("Nome ou senha inválidos")
            elif event == "Cadastrar usuário":
                login = values["nome"]
                senha = values["senha"]
                if login == senha:
                    sg.popup("A senha deve ser diferente do nome.")
                else:
                    user = search_user(login, senha)
                    if user:
                        sg.popup("Usuário já existe!")
                    else:
                        sg.popup("Cadastro aprovado!")
        self.janela.close()

def search_user(login, senha):
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
        return False

def create_user(login, senha):
    with open('usuarios.txt', 'a+', encoding='Utf-8', newline='') as arquivo:
                        arquivo.writelines(f'{login}    {senha}\n')

login_gui = LoginGui()
login_gui.run()
    