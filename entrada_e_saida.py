from microbit import *
import radio

radio.config(group=53)
radio.on()

cpfs_validos = []
cpfs_invalidos = []
cpf = 0

def enviar_cpf():
    cpf = input("Digite seu CPF: ")
    return cpf

def exibir_contagem():
    display.scroll("Validos: " + str(len(cpfs_validos)))
    display.scroll("Invalidos: " + str(len(cpfs_invalidos)))

def receber_cpf(cpf, valido):
    if len(cpf)==0:
        pass
    if len(cpf)!=0 and valido=='valido':
        display.scroll("Valido")
        cpfs_validos.append((cpf, "Valido"))
    else:
        display.scroll("Invalido")
        cpfs_invalidos.append((cpf, "Invalido"))

while True:
    if button_a.was_pressed():
        cpf_enviar = enviar_cpf()
        if cpf_enviar.lower() == "parar":
            exibir_contagem()
        radio.send(cpf_enviar)
        cpf = cpf_enviar
    if button_b.was_pressed():
        valido = radio.receive()
        receber_cpf(cpf,valido)
    if accelerometer.was_gesture('shake'):
        break