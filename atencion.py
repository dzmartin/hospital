from abc import ABC, abstractmethod


class Atencion(ABC):
    TIPOS_COBRO_VALIDOS = {1, 2}

    def __init__(self, codigo, tipoDeCobro):
        if tipoDeCobro not in self.TIPOS_COBRO_VALIDOS:
            raise ValueError("El tipo de cobro debe ser 1 o 2")
        self.codigo = codigo
        self.tipoDeCobro = tipoDeCobro

    @abstractmethod
    def importeACobrar(self):
        raise NotImplementedError

    def getId(self):
        return self.codigo

    def getTipoCobro(self):
        return self.tipoDeCobro

    def setId(self, codigo):
        self.codigo = codigo

    def setTipocobro(self, tipoDeCobro):
        if tipoDeCobro not in self.TIPOS_COBRO_VALIDOS:
            raise ValueError("El tipo de cobro debe ser 1 o 2")
        self.tipoDeCobro = tipoDeCobro

    def tipocobro_descripcion(self):
        return {1: "efectivo", 2: "tarjeta de credito"}[self.tipoDeCobro]

    def __str__(self):
        return f"ID: {self.codigo}, Tipo de cobro: {self.tipocobro_descripcion()}"


class AtencionMedica(Atencion):
    def __init__(self, codigo, tipoDeCobro, paciente, importe):
        super().__init__(codigo, tipoDeCobro)
        self.paciente = paciente
        self.importe = importe

    def importeACobrar(self):
        importe = self.importe * (0.75 if self.esPacienteHabitual() else 1)
        return importe * (1.20 if self.tipoDeCobro == 2 else 0.90)

    def esPacienteHabitual(self):
        return self.paciente.habitual

    def getPaciente(self):
        return self.paciente

    def getImporteConsulta(self):
        return self.importe

    def setPaciente(self, paciente):
        self.paciente = paciente

    def setImporteConsulta(self, importe):
        self.importe = importe

    def __str__(self):
        return f"Atencion Medica {self.codigo}: {self.importeACobrar():.2f}, Paciente: {self.paciente.nombre}"


class AtencionFarmacia(Atencion):
    def __init__(self, codigo, tipoDeCobro, importeTotal, descuento):
        super().__init__(codigo, tipoDeCobro)
        if descuento < 0:
            raise ValueError("El descuento debe ser 0 o positivo")
        self.importeTotal = importeTotal
        self.descuento = descuento

    def importeACobrar(self):
        importe = self.importeTotal - self.descuento
        return importe * (1.30 if self.tipoDeCobro == 2 else 0.95)

    def importe_final(self):
        return self.importeTotal - self.descuento

    def getImporte(self):
        return self.importeTotal

    def getCupon(self):
        return self.descuento

    def setImporte(self, importe):
        self.importeTotal = importe

    def setCupon(self, descuento):
        if descuento < 0:
            raise ValueError("El descuento debe ser 0 o positivo")
        self.descuento = descuento

    def __str__(self):
        return f"Atencion Farmacia {self.codigo}: {self.importeACobrar():.2f}"