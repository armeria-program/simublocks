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
from src.dialog.dialogTools import dialogTools

class newCornerDialog(object):

    def __init__(self):

        root = self.root = Tk()
        root.resizable(0,0)
        root.title(str("Criar uma Quina"))
        Label(root, text="Digite top, bottom, left ou right").grid(row=0, column=0, columnspan=2)
        Label(root, text="Entrada").grid(row=1, column=0)
        self.input1 = Entry(root)
        self.input1.grid(row=1, column=1)
        Label(root, text="Saída").grid(row=2, column=0)
        self.input2 = Entry(root)
        self.input2.grid(row=2, column=1)

        Button(root, width=11, text="Criar", command=self.save_button).grid(row=3, column=0)
        Button(root, width=11, text="Cancelar", command=self.cancel_button).grid(row=3, column=1)
        
        dialogTools.center(root)

    def save_button(self):

        code = [
            self.input1.get(),
            self.input2.get()
        ]
        self.returning = {
            'code': code,
            'status': 'save'
        }
        self.root.quit()

    def cancel_button(self):
        self.returning = {
            'status': 'cancel'
        }
        self.root.quit()