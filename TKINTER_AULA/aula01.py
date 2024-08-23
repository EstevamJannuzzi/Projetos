from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()

class Funcs():
    def limpa_tela(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.cidade_entry.delete(0, END)

    def conecta_bd(self):
        self.conn = sqlite3.connect('clientes.bd')
        self.cursor = self.conn.cursor(); print('Conectando ao banco de dados')

    def desconecta_bd(self):
        self.conn.close(); print('Desconectando ao banco de dados')

    def montaTabelas(self):
        self.conecta_bd(); print('Conectando ao banco de dados')

        # Criar Tabela

        self.cursor.execute('''
                            CREATE TABLE IF NOT EXISTS clientes (
                            cod INTEGER PRIMARY KEY,
                            nome_cliente CHAR (40) NOT NULL,
                            telefone INTEGER(20),
                            cidade CHAR(40)
                            );
                            ''')
        self.conn.commit(); print('Banco de dados criado')
        self.desconecta_bd()

    def add_cliente(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.cidade = self.cidade_entry.get()
        self.conecta_bd()

        self.cursor.execute(""" INSERT INTO clientes (nome_cliente, telefone, cidade) VALUES (?, ?, ?)""", (self.nome, self.telefone, self.cidade))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()

    def select_lista(self):
        self.listaCLI.delete(*self.listaCLI.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes ORDER BY nome_cliente ASC; """)
        for i in lista:
            self.listaCLI.insert('', END, values=i)
        self.desconecta_bd()


class Aplication(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_de_tela()
        self.widgets_frame_1()
        self.lista_frame_2()
        self.montaTabelas()
        self.select_lista()
        root.mainloop()
    
    def tela(self):
        self.root.title('Cadastro de Clientes')
        self.root.configure(background='#1E3643')
        self.root.geometry('700x500')
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=500, height=400)

    def frames_de_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg= '#DCDCDC', highlightbackground= '#5F9EA0', highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        self.frame_2 = Frame(self.root, bd=4, bg= '#DCDCDC', highlightbackground= '#5F9EA0', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_frame_1(self):
        # Botões
        self.bt_limpar = Button(self.frame_1, text= 'Limpar', bd=2, bg= '#107bd2', fg= '#FFFFFF', font= ('verdana', 8, 'bold'), command= self.limpa_tela)
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

        self.bt_buscar = Button(self.frame_1, text= 'Buscar', bd=2, bg= '#107bd2', fg= '#FFFFFF', font= ('verdana', 8, 'bold'))
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        self.bt_novo = Button(self.frame_1, text= 'Novo', bd=2, bg= '#107bd2', fg= '#FFFFFF', font= ('verdana', 8, 'bold'), command=self.add_cliente)
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        self.bt_alterar = Button(self.frame_1, text= 'Alterar', bd=2, bg= '#107bd2', fg= '#FFFFFF', font= ('verdana', 8, 'bold'))
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        
        self.bt_apagar = Button(self.frame_1, text= 'Apagar', bd=2, bg= '#FF0000', fg= '#FFFFFF', font= ('verdana', 8, 'bold'))
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        # Label e Input
        self.lb_codigo = Label(self.frame_1, text= 'Código', bg= '#DCDCDC', fg= '#107bd2')
        self.lb_codigo.place(relx=0.05, rely=0.05)

        self.codigo_entry = Entry(self.frame_1, bg= '#B0C4DE', fg= '#107bd2')
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        self.lb_nome = Label(self.frame_1, text= 'Nome', bg= '#DCDCDC', fg= '#107bd2')
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = Entry(self.frame_1, bg= '#B0C4DE', fg= '#107bd2')
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.8)

        self.lb_telefone = Label(self.frame_1, text= 'Telefone', bg= '#DCDCDC', fg= '#107bd2')
        self.lb_telefone.place(relx=0.05, rely=0.6)

        self.telefone_entry = Entry(self.frame_1, bg= '#B0C4DE', fg= '#107bd2')
        self.telefone_entry.place(relx=0.05, rely=0.7, relwidth=0.4)
        
        self.lb_cidade = Label(self.frame_1, text= 'Cidade', bg= '#DCDCDC', fg= '#107bd2')
        self.lb_cidade.place(relx=0.5, rely=0.6)

        self.cidade_entry = Entry(self.frame_1, bg= '#B0C4DE', fg= '#107bd2')
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4)

    def lista_frame_2(self):
        self.listaCLI = ttk.Treeview(self.frame_2, height=3, column=('col1', 'col2', 'col3', 'col4'))
        self.listaCLI.heading('#0', text='')
        self.listaCLI.heading('#1', text='Código')
        self.listaCLI.heading('#2', text='Nome')
        self.listaCLI.heading('#3', text='Telefone')
        self.listaCLI.heading('#4', text='Cidade')

        self.listaCLI.column('#0', width=1)
        self.listaCLI.column('#1', width=50)
        self.listaCLI.column('#2', width=200)
        self.listaCLI.column('#3', width=125)
        self.listaCLI.column('#4', width=125)

        self.listaCLI.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCLI.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.03, relheight=0.85)

        
Aplication()
