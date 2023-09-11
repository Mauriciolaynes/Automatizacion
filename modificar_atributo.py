class Email:
    def __init__(self):
        self.eviado = False
    def enviar_correo(self):
        self.enviado = True
mi_correo = Email()

print(mi_correo.eviado)
mi_correo.enviar_correo()
print(mi_correo.enviado)