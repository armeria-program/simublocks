# MIT License
#
# Copyright (c) 2020 Anderson Vitor Bento
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk
from src.dialog.dialogTools import dialogTools

class editBlockDialog(object):

    def __init__(self, data):

        root = self.root = Tk()
        root.resizable(0,0)
        root.title(str("Editar Bloco ") + str(data['name']))
        self.data = data 

        if data['type'] != 'corner':
            Label(root, text="Nome:").grid(row=0, column=0)
            self.inputName = Entry(root)
            self.inputName.insert(END, self.data['name'])
            self.inputName.grid(row=0,column=1,columnspan=2,sticky="EW")

        if data['type'] == 'input':
            self.editInput(root)
        elif data['type'] == 'sum':
            self.editSum(root)
        elif data['type'] == "system":
            if data['code']['type'] == "TF":
                self.editSystemTF(root)
            else:
                self.editSystemSS(root)
                        
        Button(root, width=11, text="Editar", command=self.save_button).grid(row=4, column=0)
        Button(root, width=11, text="Cancelar", command=self.cancel_button).grid(row=4, column=1)
        Button(root, width=11, text="Remover Bloco", command=self.remove_button).grid(row=4, column=2)
        
        dialogTools.center(root)

    def save_button(self):
        self.data['name'] = self.inputName.get()

        if self.data['type'] == 'input':
            self.data['code'] = self.inputCode.get(1.0, END)
        elif self.data['type'] == 'sum':
            self.data['code'] = [
                self.input1.get(),
                self.input2.get()
            ]
        else:
            if self.data['code']['type'] == "TF":
                self.data['code']['self'] = [
                    self.input1.get(),
                    self.input2.get()
                ]
            else:
                self.data['code']['self'] = [
                    self.input1.get(),
                    self.input2.get(),
                    self.input3.get(),
                    self.input4.get()
                ]
            self.data['code']['sub_type'] = self.dropdown.get()

        self.returning = {
            'data': self.data,
            'status': 'save'
        }
        self.root.quit()

    def cancel_button(self):
        self.returning = {
            'status': 'cancel'
        }
        self.root.quit()

    def remove_button(self):
        self.returning = {
            'status': 'delete'
        }
        self.root.quit()

    def twoEntries(self, root, code):
        self.input1 = Entry(root)
        self.input1.insert(END, code[0])
        self.input1.grid(row=2, column=1)
        self.input2 = Entry(root)
        self.input2.insert(END, code[1])
        self.input2.grid(row=2, column=2)
    
    def moreTwoEntries(self, root, code):
        self.input3 = Entry(root)
        self.input3.insert(END, code[0])
        self.input3.grid(row=3, column=1)
        self.input4 = Entry(root)
        self.input4.insert(END, code[1])
        self.input4.grid(row=3, column=2)

    def editSum(self, root):
        Label(root, text="Entradas:").grid(row=2, column=0)
        code = self.data['code']
        self.twoEntries(root, code)

    def dropdownButton(self,root):
        Label(root, text="Tipo:").grid(row=1, column=0)
        self.dropdown = ttk.Combobox(root,state="readonly", values=[ "continuous",  "discrete"])
        self.dropdown.grid(row=1, column=1, columnspan=2)
        if self.data['code']['sub_type'] == "continuous":
            self.dropdown.current(0)
        else:
            self.dropdown.current(1)

    def editSystemTF(self, root):
        self.dropdownButton(root)
        Label(root, text="Num and Den:").grid(row=2, column=0)
        code = self.data['code']['self']
        self.twoEntries(root, code)

    def editSystemSS(self, root):
        self.dropdownButton(root)
        code = self.data['code']['self']
        Label(root, text="A and B:").grid(row=2, column=0)
        self.twoEntries(root, code)
        Label(root, text="C and D:").grid(row=3, column=0)
        self.moreTwoEntries(root, code[2:])

    def editInput(self, root):
        Label(root, text="Código:").grid(row=1, column=0)
        self.inputCode = ScrolledText(root, height=7,width=50)
        self.inputCode.insert(END, self.data['code'])
        self.inputCode.grid(row=1, column=1,columnspan=2)