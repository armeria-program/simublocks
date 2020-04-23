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

from src.element import Workspace
from src.dialog import Dialog
from src.simulation import Simulation

class SimulationFunc:

    def execute():
        try:
            # show dialog window to enter data ( T and tf )
            res = Dialog.execute()

            if res['status'] == 'ok':
                # receive data
                data = res['data']
                T = float(data["T"])
                tf = float(data["tf"])
                # run simulation
                Simulation(T,tf)

        except Exception as e:
            Dialog.alert("Erro", str(e))

    def importCode():
        code = Workspace.importCode
        res = Dialog.importCode(code)
        if res['status'] == 'ok':
            Workspace.importCode = res['code']