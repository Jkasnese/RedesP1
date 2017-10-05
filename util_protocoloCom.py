
# COMANDO PROTOCOLO
    # 0 = CadastrarSensor
    # 1 = Mensagem de dados do Sensor
    # 2 = Cadastrar médico
    # 3 = Dados do médico

# CADASTRAR SENSOR

    # PRIMEIRA MENSAGEM DO SENSOR É "CADASTRO(0)|CPF"
    ## resposta do servidor é (0) cadastrou, (1) não cadastrou

# MENSAGEM SENSOR   
    # DEMAIS MENSAGENS DO SENSOR SÃO "DADOS(1)|ID|BPM|PRESSAO|MOVIMENTO"

caracter_separador = ";"
