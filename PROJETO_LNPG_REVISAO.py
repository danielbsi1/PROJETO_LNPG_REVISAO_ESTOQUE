from tkinter import *
from tkinter.ttk import Combobox
filename = 'arquivo.txt'

def verificar(event):

    # camposVazios = []

    # if entryNomeProduto.get() == '':
    #     camposVazios.append('Nome produto')
    # elif entryPrecoUnitario.get() == '':
    #     camposVazios.append('Preço unitário')
    # elif entryQuantEstoque.get() == '':
    #     camposVazios.append('Quantidade estoque')
    
    if entryNomeProduto.get() == '' or entryPrecoUnitario.get() == '' or entryQuantEstoque.get() == '' or v0.get() != 'Sim' and v0.get() != 'Não':
        windowVoid = Toplevel()
        windowMain.title('ERRO')
        
        labelAviso = Label(windowVoid ,text='FALTA CAMPO PARA PREENCHER')
        labelAviso.grid(row=1, column=1, padx=10, pady=10, sticky='nswe',  columnspan=2)
        verificarQtdPositiva()

        windowVoid.mainloop()
        
def verificarQtdPositiva():
    if int(entryQuantEstoque.get()) *  0 == 0:

        if int(entryQuantEstoque.get()) < 0:
            windowVoid = Toplevel()
            windowMain.title('ERRO')
        
            labelAviso = Label(windowVoid ,text='Quantidade de estoque menor que 0')
            labelAviso.grid(row=1, column=1, padx=10, pady=10, sticky='nswe',  columnspan=2)
            windowVoid.mainloop()
    else:    
        windowVoid = Toplevel()
        windowMain.title('ERRO')
    
        labelAviso = Label(windowVoid ,text='n eh numero')
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
btnNomeProduto.bind('<Button-1>', )


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