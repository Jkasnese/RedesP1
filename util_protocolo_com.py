# TODAS AS MENSAGENS DEVERÃO SER TROCADAS EM FORMATO STRING

# COMANDO PROTOCOLO
    # 0 = CadastrarSensor
    # 1 = Mensagem de dados do Sensor
    # 2 = Cadastrar médico
    # 3 = Autenticar médico
    # 4 = Pedir lista de pacientes em risco
    # 5 = Buscar paciente
    # 6 = Selecionar paciente para ser monitorado
    # 7 = Parar monitoramento

    # 9 = Repita mensagem

# RESPOSTA DO SERVIDOR = X
    # 0 = Sucesso
    # !0 = Fracasso
    # Depois ver documentação C sobre erros, return 0 etc.
    # CÓDIGO DE ERRO DE AUTENTICAÇÃO
    #  00 sucesso
    #  0!0 Fracasso

# CADASTRAR SENSOR

    # PRIMEIRA MENSAGEM DO SENSOR É "CADASTRO(0)CPF|ID"
    ## resposta do servidor é (0) cadastrou, (1) não cadastrou

# MENSAGEM SENSOR   
    # DEMAIS MENSAGENS DO SENSOR SÃO "DADOS(1)|ID|BPM|PRESSAO|MOVIMENTO|X|Y"

# CADASTRAR MEDICO
    # Cadastrar médico: 2CRM|NOME|SENHA

# AUTENTICAR MEDICO
    # 

# LISTA PACIENTES RISCO
    # 0CPF|BPM|PRESSAO|MOVIMENTO
    # UTILIZADO SEPARADOR PACIENTES

    # Resposta do servidor: 0lista ou 1, indicando falha.

# BUSCAR PACIENTE:
    # Médico: 5CRM|CPF
    # Servidor retorna: #CPF|BPM|PRESSAO|MOVIMENTO

# PACIENTE MONITORADO:
    # Médico envia: 6CRM|BOCAL

# PARAR MONITORAMENTO
    # Medico envia: 7CRM



caracter_separador = ";"
separador_pacientes = "|"
tamanho_mundo = 200
