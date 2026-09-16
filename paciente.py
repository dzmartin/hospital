class Paciente:
    SINTOMAS_VALIDOS = {1, 2, 3}

    def __init__(self, nombre, sintoma, habitual=False):
        if sintoma not in self.SINTOMAS_VALIDOS:
            raise ValueError("El sintoma debe ser 1, 2 o 3")
        self.nombre = nombre
        self.sintoma = sintoma
        self.habitual = habitual

    @property
    def esHabitual(self):
        return self.habitual

    @esHabitual.setter
    def esHabitual(self, valor):
        self.habitual = valor

    def getNombre(self):
        return self.nombre

    def getSintoma(self):
        return self.sintoma

    def getEsHabitual(self):
        return self.habitual

    def setNombre(self, nombre):
        self.nombre = nombre

    def setSintoma(self, sintoma):
        if sintoma not in self.SINTOMAS_VALIDOS:
            raise ValueError("El sintoma debe ser 1, 2 o 3")
        self.sintoma = sintoma

    def setEsHabitual(self, habitual):
        self.habitual = habitual

    def tiposintoma(self):
        return {1: "corazon", 2: "pulmon", 3: "otras"}[self.sintoma]

    def __str__(self):
        return f"Paciente: {self.nombre}, Sintoma: {self.tiposintoma()}, Habitual: {self.habitual}"