from tkinter import *
from tkinter.ttk import Combobox
filename = 'arquivo.txt'



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
btnNomeProduto.bind('<Button-1>')

windowMain.mainloop()