from tkinter import *

root = Tk()

class Aplication():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_de_tela()
        root.mainloop()
    
    def tela(self):
        self.root.title('Cadastro de Clientes')
        self.root.configure(background='#1E3643')
        self.root.geometry('700x500')
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=400, height=300)

    def frames_de_tela(self):
        self.frame_1 = Frame(self.root, bd=4, bg= '#DCDCDC', highlightbackground= '#5F9EA0', highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        self.frame_1 = Frame(self.root, bd=4, bg= '#DCDCDC', highlightbackground= '#5F9EA0', highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
         

Aplication()
