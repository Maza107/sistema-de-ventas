class Cliente:
    """ Clase que impleta cliente"""
    def __init__(self,numero_documento,razon_social,direccion,telefono) -> None:
        self.numero_documento = numero_documento
        self.razon_social = razon_social
        self.direccion = direccion
        self.telefono = telefono
        pass
    def convertir_a_texto(self):
        return "|{}|{}|{}|{}|".format(self.numero_documento,
                                      self.razon_social,
                                      self.direccion,
                                      self.telefono)