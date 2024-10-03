import tkinter as tk 
from tkinter import messagebox 

def login():
    usuario = entry_user.get()
    senha = entry_pwd.get()

    if usuario == 'admin' and senha == '12345':
        messagebox.showinfo("Login", 'Login realizado com sucesso')
        root.destroy()
        formulario()
    else:
        messagebox.showerror("Erro", "Usuario ou senha incorretos")

def fechar_aplicação():
    root.quit()

def formulario():
    global entry_user, entry_pwd, root
    root = tk.Tk()
    root.title("Login")
    tk.Label(root, text="Usuario:").grid(row=0, column=0)
    tk.Label(root, text="Senha:").grid(row=1, column=0)
    entry_user = tk.Entry(root)
    entry_user.grid(row=0, column=1)
    entry_pwd = tk.Entry(root, show="*")
    entry_pwd.grid(row=1, column=1)

    
#criação de tela 

root = tk.Tk()
root ['bg'] = '#121212'
root.title("Tela de Login")
root.geometry("300x150")

label_usuario = tk.Label(root, text="Nome de Usuario")
label_usuario.pack(padx=8)
entry_user = tk.Entry(root)
entry_user.pack()

#Senha
label_senha = tk.Label(root, text="Senha")
label_senha.pack(padx=8)
entry_pwd = tk.Entry(root,show="*")
entry_pwd.pack()

#Botão de Login
botao_login = tk.Button(root, text="Login", command=login)
botao_login.pack(padx=20)

#Botão Fechar
botao_fechar = tk.Button(root, text="Fechar", command=fechar_aplicação)
botao_fechar.pack(padx=20)

root.mainloop()
