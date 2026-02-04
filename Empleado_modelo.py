class empleado_modelo:
    def __init__(self,nombre,apellido,cedula,celular):
        self.nombre_empleado = nombre
        self.apellido_empleado = apellido
        self.cedula_empleado = cedula
        self.celular_empleado = celular
        print( "empleado creado como objeto")

    def set_nombre_empleado(self,nuevo_nombre):
        self.nombre_empleado = nuevo_nombre

    def get_nombre_empleado(self):
        return self.set_nombre_empleado
    
    def set_apellido_empleado(self,nuevo_apellido):
        self.apellido_empleado = nuevo_apellido

    def get_apellido_empleado(self):
        return self.set_apellido_empleado
    
    def set_cedula_empleado(self,nueva_cedula):
        self.cedula_empleado = nueva_cedula

    def get_cedula_empleado(self):
        return self.set_cedula_empleado
    
    def set_celular_empleado(self,nuevo_celular):
        self.set_celular_empleado = nuevo_celular

    def get_celular_empleado(self):
        return self.set_celular_empleado
    
    def ver_info_empleado(self):
        info_empleado = " nombre_empleado " + self.nombre_empleado + " apellido_empleado " + self.apellido_empleado
        info_empleado = info_empleado + "cedula_empleado " + self.cedula_empleado + " celular_empleado " + self.celular_empleado
        return info_empleado 
