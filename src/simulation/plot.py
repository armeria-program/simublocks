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

import matplotlib.pyplot as plt

class Plot:

    def run(s):
        Plot.plotInput(s['inputs'], s['t'])
        Plot.plotSystem(s['blocks'], s['t'])
        plt.show()

    def plotInput(inputs,t):

        plt.figure("Input")
        plt.title("Input Signals")
        cont = 0
        
        for i in inputs:
            cont += 1
            b = inputs[i]
            if len(inputs) > 1: plt.subplot(100*len(inputs) + 10 + cont)
            plt.plot(t[:-1], b.input[:-1])
            plt.legend([b.name])
            print(b.name)

    def plotSystem(blocks, t):

        for i in blocks:
            b = blocks[i]
            plt.figure('figure'+str(i))
            plt.subplot(211)
            plt.title("Bloco: " + b.name)
            plt.plot(t[:-1], ((b.ss[2]@b.x).T + (b.ss[3]@b.u).T)[:-1]  )
            plt.legend(["Block Output"])
            plt.subplot(212)
            plt.plot(t[:-1], (b.u).reshape(len(b.x))[:-1])
            plt.legend(["Block Input"])