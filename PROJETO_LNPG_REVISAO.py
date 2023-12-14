from tkinter import *
from tkinter.ttk import Combobox
filename = 'arquivo.txt'

def limpar(event):
    entryNomeProduto.delete(0, END)
    entryPrecoUnitario.delete(0, END)
    entryQuantEstoque.delete(0, END)
    

def verificar(event):
    
    
    if entryNomeProduto.get() == '' or entryPrecoUnitario.get() == '' or entryQuantEstoque.get() == '' or v0.get() != 'Sim' and v0.get() != 'Não':
        windowVoid = Toplevel()
        windowVoid.title('ERRO')
        
        labelAviso = Label(windowVoid ,text='FALTA CAMPO PARA PREENCHER')
        labelAviso.grid(row=1, column=1, padx=10, pady=10, sticky='nswe',  columnspan=2)
        verificarQtdPositiva()
        verificarPrecoUnitario()
        windowVoid.mainloop()
    else:
        verificarQtdPositiva()
        verificarPrecoUnitario()
    
    
    

def  verificarPrecoUnitario(event):
     
    a = entryPrecoUnitario.get()
    try:
        a = float(entryPrecoUnitario.get())
    
        if a < 0:
            windowVoid = Toplevel()
            windowVoid.title('ERRO')

            labelAviso = Label(windowVoid ,text='Preço unitário menor que 0')
            labelAviso.grid(row=1, column=1, padx=10, pady=10, sticky='nswe',  columnspan=2)
            windowVoid.mainloop()
    except:
        windowVoid = Toplevel()
        windowVoid.title('ERRO')

        labelAviso = Label(windowVoid ,text='Não é um valor válido')
        labelAviso.grid(row=1, column=1, padx=10, pady=10, sticky='nswe',  columnspan=2)
        windowVoid.mainloop()


def verificarQtdPositiva(event):
    a = entryQuantEstoque.get()
    try:
        a = int(entryQuantEstoque.get())
    
        if a < 0:
            windowVoid = Toplevel()
            windowVoid.title('ERRO')

            labelAviso = Label(windowVoid ,text='Quantidade de estoque menor que 0')
            labelAviso.grid(row=1, column=1, padx=10, pady=10, sticky='nswe',  columnspan=2)
            windowVoid.mainloop()
    except:
    

        windowVoid = Toplevel()
        windowVoid.title('ERRO')

        labelAviso = Label(windowVoid ,text='Não é um valor válido')
        labelAviso.grid(row=1, column=1, padx=10, pady=10, sticky='nswe',  columnspan=2)
        windowVoid.mainloop()
 

windowMain = Tk()
windowMain.title('CONTROLE DE ESTOQUE')

labelEstoque = Label(text='SISTEMA DE CONTROLE DE ESTOQUE')
labelEstoque.grid(row=0, column=0, padx=10, pady=10, sticky='nswe',  columnspan=3)

labelNomeProduto = Label(text='Nome do produto: ')
labelNomeProduto.grid(row=1, padx=10, pady=10, column=0, sticky='nswe', columnspan=1)
entryNomeProduto = Entry(windowMain)
entryNomeProduto.grid(row=1, padx=10, pady=10, column=1, sticky='nswe', columnspan=3)

labelQuantEstoque = Label(text='Quantidade em estoque: ')
labelQuantEstoque.grid(row=2, padx=10, pady=10, column=0, sticky='nswe', columnspan=1)
entryQuantEstoque = Entry(windowMain)
entryQuantEstoque.grid(row=2, padx=10, pady=10, column=1, sticky='nswe', columnspan=2)


labelPrecoUnitario = Label(text='Preço unitário: ')
labelPrecoUnitario.grid(row=3, padx=10, pady=10, column=0, sticky='nswe', columnspan=1)
entryPrecoUnitario = Entry(windowMain)
entryPrecoUnitario.grid(row=3, padx=10, pady=10, column=1, sticky='nswe', columnspan=2)



btnNomeProduto = Button(text='Enviar')
btnNomeProduto.grid(row=11, padx=10, pady=10, column=0, sticky='nswe', columnspan=1)
btnNomeProduto.bind('<Button-1>', verificar)

btnNomeProduto = Button(text='Limpar')
btnNomeProduto.grid(row=11, padx=10, pady=10, column=1, sticky='nswe', columnspan=2)
btnNomeProduto.bind('<Button-1>', limpar)


v0=StringVar()
v0.set('1')
labelGelado = Label(windowMain,text='É gelado?' )
labelGelado.grid(row=4, padx=10, pady=10, column=0, sticky='nswe', columnspan=1)
labelGelado.configure(font=("Helvetica", 9))
r1=Radiobutton(windowMain, text="Sim", variable=v0, value='Sim')
r2=Radiobutton(windowMain, text="Não", variable=v0, value='Não')
r1.grid(row=4, padx=10, pady=10, column=2, sticky='nswe', columnspan=1)
r2.grid(row=4, padx=10, pady=10, column=1, sticky='nswe', columnspan=1)


windowMain.mainloop()