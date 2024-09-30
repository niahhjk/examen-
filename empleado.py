class Empleado:
    def __init__(self, rfc, apellidos, nombres):
        self.rfc = rfc
        self.apellidos = apellidos
        self.nombres = nombres
    def mostrar_info(self):
        return f"RFC: {self.rfc}, Apellidos: {self.apellidos}, Nombres: {self.nombres}"
    
class EmpleadoVendedor(Empleado):
    def __init__(self, rfc, apellidos, nombres, monto_vendido, tasa_comision):
        super().__init__(rfc, apellidos, nombres)
        self.monto_vendido = monto_vendido
        self.tasa_comision = tasa_comsion
    def calcular_ingresos(self):
        return self.monto_vendido * self.tasa_comision
    def calcular_bonificacion(self):
        if self.monto_vendido < 1000:
            return 0
        elif 1000 <= self.monto_vendido <= 5000:
            return self.calcular_ingresos() * 0.05
        else:
            return self.calcular_ingresos() * 0.10
    def calcular_descuento(self):
        if self.calcular_ingresos() < 1000:
            return self.calcular_ingresos() * 0.11
        else:
            return self.calcular_ingresos() * 0.15
    def calcular_sueldo_neto(self):
        return self.calcular_ingresos() + self.calcular_bonificacion() - self.calcular_descuento()

class EmpleadoPermanente(Empleado):
    def __init__(self, rfc, apellidos, nombres, sueldo_base, num_seguro_social):
        super().__init__(rfc, apellidos, nombres)
        self.sueldo_base = sueldo_base
        self.num_seguro_social = num_seguro_social  
    def calcular_ingresos(self):
        return self.sueldo_base
    def calcular_descuento(self):
        return self.sueldo_base * 0.11
    def calcular_sueldo_neto(self):
        return self.calcular_ingresos() - self.calcular_descuento()
    
def main():
    tipo_empleado = input("SELECCIONA EL TIPO DE EMPLEADO: VENDEDOR O PERMANENTE ").lower()
    rfc = input("INGRESA EL RFC: ")
    apellidos = input("INGRESA LOS APELLIDOS: ")
    nombres = input("INGRESA EL NOMBRE: ")
    
    if tipo_empleado == "vendedor":
        monto_vendido = float(input("INGRESA EL MONTO VENDIDO: "))
        tasa_comision = float(input("INGRESA LA TASA DE COMISION: "))
        vendedor = EmpleadoVenddor(rfc, apellidos, nombres, monto_vendido, tasa_comision)
        print(vendedor.mostrar_info())
        print("INGRESOS:", vendedor.calcular_ingresos())
        print("BONIFICACION:", vendedor.calcular_bonificacion())
        print("DESCUENTO:", vendedor.calcular_descuento())
        print("SUELDO NETO:", vendedor.calcular_sueldo_neto())
    elif tipo_empleado == "permanente":
        sueldo_base = float(input("INGRESA EL SUELDO BASE: "))
        num_seguro_social = input("INGRESA EL NUMERO DE SEGURO SOCIAL: ")
        permanente = EmpleadoPermanente(rfc, apellidos, nombres, sueldo_base, num_seguro_social)
        print(permanente.mostrar_info())
        print("INGRESOS:", permanente.calcular_ingresos())
        print("DESCEUNTO:", permanente.calcular_descuento())
        print("SUELDO NETO:", permanente.calcular_sueldo_neto())
    else:
        print("SELECCIONA UNA DE LAS DOS OPCIONES ")

if __name__ == "__main__":
    main()

