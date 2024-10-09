import tkinter as tk

janela = tk.Tk()
janela.title("Eventos com tkinter")
janela.geometry("1000x500")
label = tk.Label(janela, text="Nome")
label.pack(padx=8)
entrada = tk.Entry(janela)
entrada.pack(pady=10)
janela.mainloop()