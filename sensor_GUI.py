from tkinter import Tk, Label, Button, LEFT, RIGHT, W, IntVar
from sensor_controller import *
from threading import Thread

class MyFirstGUI:
    def __init__(self, master):
        self.master = master

        master.title("GUI do Sensor")

        # Variaveis do Sensor
        #threadSensor = Thread(target = novoSensor(),)
        #threadSensor.start()
        # REMOVER SENSOR E ADICIONAR CONTROLLER P/ MVC PENDENTE FALTA FAZER
        self.sensor = novoSensor(cpf_sensor, ip_servidor, tcp_porta)

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

        # # # # PRESSAO # # # #
        
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

        # # # # COORDENADAS # # # #
       
        # Label POSX
        self.posicaox_label = Label(master, text="X:")
        self.posicaox_label.grid(row=4, column=0, sticky=W)

        # Valor posicaoX
        self.valor_posicaox_label_num = IntVar()
        self.valor_posicaox_label_num.set(self.sensor.x)
        self.valor_posicaox_label = Label(master, textvariable=self.valor_posicaox_label_num)
        self.valor_posicaox_label.grid(row=4, column=1)

        # Botão Incrementar X
        self.incrementar_posicaox_button = Button(master, text="/\\", command=self.incrementar_posicaox)
        self.incrementar_posicaox_button.grid(row=4, column=2)

        # Botão Decrementar X
        self.decrementar_posicaox_button = Button(master, text="\\/", command=self.decrementar_posicaox)
        self.decrementar_posicaox_button.grid(row=4, column=3)

        # Label POSY
        self.posicaoy_label = Label(master, text="Y:")
        self.posicaoy_label.grid(row=5, column=0, sticky=W)

        # Valor posicaoY
        self.valor_posicaoy_label_num = IntVar()
        self.valor_posicaoy_label_num.set(self.sensor.y)
        self.valor_posicaoy_label = Label(master, textvariable=self.valor_posicaoy_label_num)
        self.valor_posicaoy_label.grid(row=5, column=1)

        # Botão Incrementar X
        self.incrementar_posicaoy_button = Button(master, text="/\\", command=self.incrementar_posicaoy)
        self.incrementar_posicaoy_button.grid(row=5, column=2)

        # Botão Decrementar X
        self.decrementar_posicaoy_button = Button(master, text="\\/", command=self.decrementar_posicaoy)
        self.decrementar_posicaoy_button.grid(row=5, column=3)

        # # # # FECHAR # # # #

        # Botão fechar
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=6, column=1, columnspan=1)
        
        

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

    def incrementar_posicaox(self):
        self.sensor.x += 1
        self.valor_posicaox_label_num.set(self.sensor.x)
        self.valor_posicaox_label = Label(self.master, textvariable=self.valor_posicaox_label_num)

    def decrementar_posicaox(self):
        self.sensor.x -= 1
        self.valor_posicaox_label_num.set(self.sensor.x)
        self.valor_posicaox_label = Label(self.master, textvariable=self.valor_posicaox_label_num)

    def incrementar_posicaoy(self):
        self.sensor.y += 1
        self.valor_posicaoy_label_num.set(self.sensor.y)
        self.valor_posicaoy_label = Label(self.master, textvariable=self.valor_posicaoy_label_num)

    def decrementar_posicaoy(self):
        self.sensor.y -= 1
        self.valor_posicaoy_label_num.set(self.sensor.y)
        self.valor_posicaoy_label = Label(self.master, textvariable=self.valor_posicaoy_label_num)

# Rodando
cpf_sensor = str(input("Digite um CPF para o sensor: "))
ip_servidor = str(input("Digite o IP do servidor: "))
tcp_porta = int(input("Digite a porta TCP do servidor: "))
root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
