from tkinter import Tk, Label, Button, LEFT, RIGHT, W, IntVar
from sensor_cliente import *
from threading import Thread

class MyFirstGUI:
    def __init__(self, master):
        self.master = master

        master.title("GUI do Sensor")

        # Variaveis do Sensor
        #threadSensor = Thread(target = novoSensor(),)
        #threadSensor.start()
        self.sensor = novoSensor()

        # Label principal
        self.label = Label(master, text="Configurações do Sensor:")
        self.label.grid(row=0, column=1, columnspan=1)

        # Label BPM:
        self.bpm_label = Label(master, text="BPM:")
        self.bpm_label.grid(row=1, column=0, sticky=W)

        # Valor BPM e Label_Valor_BPM
        self.valor_bpm_label_num = IntVar()
        self.valor_bpm_label_num.set(self.sensor.bpm)
        self.valor_bpm_label = Label(master, textvariable=self.valor_bpm_label_num)
        self.valor_bpm_label.grid(row=1, column=1)

        # Botão Incrementar BPM
        self.incrementar_bpm_button = Button(master, text="/\\", command=self.incrementarBPM)
        self.incrementar_bpm_button.grid(row=1, column=2)

        self.decrementar_bpm_button = Button(master, text="\\/", command=self.decrementarBPM)
        self.decrementar_bpm_button.grid(row=1, column=3)

        # # # # MOVIMENTO # # # #

        # Label movimento
        self.movimento_label = Label(master, text="Movimentando:")
        self.movimento_label.grid(row=2, column=0, sticky=W)

        # Valor Movimento e Label_Valor_Movimento
        if (True == self.sensor.movimento):
            self.valor_movimento_label = Label(master, text="SIM!")
        else:
            self.valor_movimento_label = Label(master, text="NÃO!")
        self.valor_movimento_label.grid(row=2, column=1)

        # Botão Movimentar
        self.movimentar_button = Button(master, text="ANDA!", command=self.movimentar)
        self.movimentar_button.grid(row=2, column=2)

        self.parar_button = Button(master, text="PARA!", command=self.parar)
        self.parar_button.grid(row=2, column=3)
        
        # Label Pressao
        self.pressao_label = Label(master, text="Pressão:")
        self.pressao_label.grid(row=3, column=0, sticky=W)

        # Valor Pressao e Label_Valor_Pressao
        self.valor_pressao_label = Label(master, text=str(self.sensor.pressao))
        self.valor_pressao_label.grid(row=3, column=1)

        # Botão Incrementar Pressao
        self.pressao_baixa_button = Button(master, text="BAIXA", command=self.pressao_baixa)
        self.pressao_baixa_button.grid(row=3, column=2)

        # Botão Decrementar Pressao
        self.pressao_normal_button = Button(master, text="NORMAL", command=self.pressao_normal)
        self.pressao_normal_button.grid(row=3, column=3)

        # Botão Pressao Alta
        self.pressao_alta_button = Button(master, text="ALTA", command=self.pressao_alta)
        self.pressao_alta_button.grid(row=3, column=4)

        # Botão fechar
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=4, column=1, columnspan=1)

        # Atualiza dados da interface
            # FALTA FAZER            

    # # # Funções da classe # # #

#    def atualizarValores(self):
        # FALTA FAZER
            

    def incrementarBPM(self):
        self.sensor.bpm += 1
        self.valor_bpm_label_num.set(self.sensor.bpm)
        self.valor_bpm_label = Label(self.master, textvariable=self.valor_bpm_label_num)

    def decrementarBPM(self):
        self.sensor.bpm -= 1
        self.valor_bpm_label_num.set(self.sensor.bpm)
        self.valor_bpm_label = Label(self.master, textvariable=self.valor_bpm_label_num)

    def pressao_baixa(self):
        self.sensor.pressao = 1
        self.valor_pressao_label = Label(self.master, text=str(self.sensor.pressao))
        self.valor_pressao_label.grid(row=3, column=1)

    def pressao_normal(self):
        self.sensor.pressao = 0
        self.valor_pressao_label = Label(self.master, text=str(self.sensor.pressao))
        self.valor_pressao_label.grid(row=3, column=1)

    def pressao_alta(self):
        self.sensor.pressao = 2
        self.valor_pressao_label = Label(self.master, text=str(self.sensor.pressao))
        self.valor_pressao_label.grid(row=3, column=1)

    def movimentar(self):
        self.sensor.movimento = True
        self.valor_movimento_label = Label(self.master, text="SIM!")
        self.valor_movimento_label.grid(row=2, column=1)

    def parar(self):
        self.sensor.movimento = False
        self.valor_movimento_label = Label(self.master, text="NÃO!")
        self.valor_movimento_label.grid(row=2, column=1)


root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
