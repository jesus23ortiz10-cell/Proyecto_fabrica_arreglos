class base_datos_empleado:
    def __init__(self):
        #este es el array
        self.bd_empleado_lista = []

    def guardar_empleados(self,obj_empleado):
        self.bd_empleado_lista.append(obj_empleado)
        return True
       
    def extender_varios_empleados(self,varios_obj):
        self.extender_varios_empleados(varios_obj)
        
    def imprimir_info(self):
        for i in range (len(self.bd_empleado_lista)):
            print(self.bd_empleado_lista[1].ver_info_empleado())