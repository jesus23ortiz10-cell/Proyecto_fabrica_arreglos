class Api_BD_maquinas:
    def __init__(self):
        self.api_maquina [
        [  "codigo maquina", "nombre maquina", "modelo maquina", "estado maquina", ],
        ["cod 1234", "brazo mecanico", "x200", "apagar"],
        [ "cod 2352", "cinta transportadora", "zx400", "requiere mantenimiento"]
        [ "cod 5648", "monobrazo", "jk100", "encendida"],
        ]

    def imprimir_info(self):
        for i in range(len(self.Api_maquinas)):
            print(self.Api_maquinas(i))

    def buscar_info(self):
        return self.Api_maquina[2][2]