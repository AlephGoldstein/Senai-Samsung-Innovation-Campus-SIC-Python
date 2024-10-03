from tkinter import *

def janela_principal():
   janela1 = Tk()
   janela1.geometry("300x300+200+200")
   janela1 ["bg"] = "green"

   bt1 = Button(janela1, text="abrir a segunda janela",command = lambda:
   janela_secundaria(janela1)) ## der erro, apague o 'e' no lambda e:
   bt1.place(x = 50, y =100)

def janela_secundaria(master):
   janela2 = Toplevel(master)
   janela2.transient(master)
   janela2.geometry("300x300+200+200")
   janela2["bg"] = "green"

   bt1 = Button(janela2, text = "Voltar", command = janela2.destroy)
   bt1.place(x = 50, y = 100)

janela_principal()