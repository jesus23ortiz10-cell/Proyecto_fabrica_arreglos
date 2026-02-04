from Empleado_modelo import empleado_modelo
from bd_modelo import Api_BD
from Api_maquinas import Api_BD_maquinas

#codigo principal

obj_Api = Api_BD()
obj_Api_maquinas = Api_BD_maquinas()
obj_Api_maquinas.imprimir_info()
print(obj_Api_maquinas).buscar_info

obj_empleado1  =empleado_modelo ("Andres", "Fernandez", "1065873149", "3216579481")
obj_empleado2  =empleado_modelo ("Felipe", "Ortiz", "98765090", "3198732189")
obj_empleado3  =empleado_modelo ("Carlos", "Gomez", "997806547", "3179536810")

obj_Api.guardar_empleados(obj_empleado1)
obj_Api.guardar_empleados(obj_empleado2)
obj_Api.guardar_empleados(obj_empleado3)
obj_Api.imprimir_Api()
