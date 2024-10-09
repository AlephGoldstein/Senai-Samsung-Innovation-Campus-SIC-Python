import tkinter as tk

def calcular():
    try:
        resultado.set(eval(entrada.get()))
    except:
        resultado.set("ERRO")
calculadora = tk.Tk()
calculadora.title("Cerebro Virtual")

entrada = tk.Entry(calculadora, width=20, font=("ARIAL",24))
entrada.grid(row=0,column=0,columnspan=5)

botao_calcular = tk.Button(calculadora, text="=", command=calcular,width=20,font=("Arial",24))
botao_calcular.grid(row=1,column=0,columnspan=5)

resultado = tk.StringVar()
label_resultado = tk.Label(calculadora, textvariable=resultado, font=("Arial",24))
label_resultado.grid(row=2,column=0,columnspan=5)

calculadora.mainloop()