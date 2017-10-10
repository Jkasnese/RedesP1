from tkinter import Tk, Label, Button, LEFT, RIGHT, W, IntVar, E
from medico_controller import *
from threading import Thread

class MyFirstGUI:
    def __init__(self, master):
        self.master = master

        master.title("Programa do Medico")

        # Atributos:
            # Medico
        self.medico, self.bocal = novo_medico(nome, crm, senha, ip_servidor, tcp_porta)
            # Pacientes:
        self.labels_pacientes = [] # [0]CPF, [1]BPM, [2]pressao, [3]movimento, [4]botão monitorar

        # Label principal
        self.label = Label(master, text="Lista de pacientes em risco:")
        self.label.grid(row=0, column=1, columnspan=1)

        # Label paciente:
        self.paciente_label = Label(master, text="Paciente:")
        self.paciente_label.grid(row=1, column=0, sticky=W)

        # Label BPM:
        self.bpm_label = Label(master, text="BPM:")
        self.bpm_label.grid(row=1, column=1, columnspan=1)

        # Label Pressao
        self.pressao_label = Label(master, text="Pressão:")
        self.pressao_label.grid(row=1, column=2, columnspan=1)

        # Label movimento
        self.movimento_label = Label(master, text="Movimentando:")
        self.movimento_label.grid(row=1, column=3, sticky=E)

        thread_atualizar_lista = Thread(target=self.atualizar_lista, args=(master,), daemon=True)
        thread_atualizar_lista.start()        

        # Botão fechar
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=1, column=4, columnspan=1, sticky=E)

        # Atualiza dados da interface
            # FALTA FAZER            

    # # # Funções da classe # # #

#    def atualizarValores(self):
        # FALTA FAZER

    def atualizar_lista(self, master):
        while True:
            # Exibir pacientes: [0]CPF, [1]BPM, [2]pressao, [3]movimento, [4]botão monitorar
            #Talvez precise iterar na lista de labels e ir botand o grid
            if (not lista_risco):
                # Label lista vazia
                self.vazia_label = Label(master, text="Nao ha pacientes cadastrados!")
                self.vazia_label.grid(row=2, column=0, sticky=W)
            else:
                linha = 2
                for paciente in lista_risco:
                    self.exibir_paciente(paciente, master, linha) # CPF de cada paciente
                    linha += 1
                #self.atualizar_grid()

    def atualizar_grid(self):
        linha = 2
        for i in self.labels_pacientes:
            for j in range (4):
                i.grid(row=linha, column=j)
            linha += 1

    # Recebe lista de dados de um paciente. [0] = CPF, [1] = BPM, [2] = Pressao, [3] = Movimento
    def exibir_paciente(self, paciente, master, linha):
        paciente = paciente.spit(caracter_separador)
        for i in range(4):
            label_paciente = Label(self.master, text=str(paciente[i]))
            label_paciente.grid(row=linha, column=i, columnspan=1)
            self.labels_pacientes.append(label_paciente)
        monitorar_button = Button(self.master, text="MONITORAR", command= lambda: self.monitorar_paciente(paciente[0]))
        monitorar_button.grid(row=linha, column=4, sticky=E)

    def monitorar_paciente(self, cpf):
        selecionar_paciente_monitorado(self.medico.crm, cpf, self.bocal, 5005)


# Rodando
nome = str(input("Digite o nome do medico: "))
crm = str(input("Digite o CRM do medico: "))
senha = str(input("Digite a senha do medico: "))
ip_servidor = str(input("Digite o IP do servidor: "))
tcp_porta = int(input("Digite a porta TCP do servidor: "))
root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
