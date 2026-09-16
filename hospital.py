from atencion import AtencionMedica


class Hospital:
    def __init__(self, razonSocial):
        self.razonSocial = razonSocial
        self.atencionesRealizadas = []

    def addAtencion(self, atencion):
        self.atencionesRealizadas.append(atencion)

    def atencionesMedicas(self):
        return [atencion for atencion in self.atencionesRealizadas
                if isinstance(atencion, AtencionMedica)]

    def getRazonSocial(self):
        return self.razonSocial

    def setRazonSocial(self, razonSocial):
        self.razonSocial = razonSocial

    def importe_total_atencion_consulta(self):
        return sum(atencion.getImporteConsulta() for atencion in self.atencionesMedicas())

    def importe_promedio_atenciones(self, valor_min, valor_max):
        importes = [atencion.importeACobrar() for atencion in self.atencionesMedicas()
                    if valor_min <= atencion.importeACobrar() <= valor_max]
        return sum(importes) / len(importes) if importes else 0.0

    def codigo_primera_atencion_habitual(self):
        for atencion in self.atencionesMedicas():
            if atencion.esPacienteHabitual():
                return atencion.codigo
        return 0

    def __str__(self):
        detalles = ", ".join(str(atencion) for atencion in self.atencionesRealizadas)
        return f"Hospital: {self.razonSocial}, Cantidad de atenciones: {len(self.atencionesRealizadas)}, {detalles}"