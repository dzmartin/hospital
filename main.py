import csv
from pathlib import Path

from atencion import AtencionFarmacia, AtencionMedica
from hospital import Hospital
from paciente import Paciente


DATA = Path(__file__).parent / "data"


def aBooleano(valor):
    return str(valor).strip().lower() == "true"


def _filas(nombre):
    with (DATA / nombre).open(newline="", encoding="utf-8") as archivo:
        return list(csv.DictReader(archivo))


def cargarPacientes():
    return {
        int(fila["codigo_atencion"]): Paciente(
            fila["nombre"], int(fila["sintoma"]), aBooleano(fila["habitual"])
        )
        for fila in _filas("pacientes.csv")
    }


def cargarAtencionesMedicas(pacientes):
    return [
        AtencionMedica(
            int(fila["codigo"]), int(fila["tipo_cobro"]),
            pacientes[int(fila["codigo"])], float(fila["importe_consulta"])
        )
        for fila in _filas("atenciones_medicas.csv")
    ]


def cargarAtencionesFarmacia():
    return [
        AtencionFarmacia(
            int(fila["codigo"]), int(fila["tipo_cobro"]),
            float(fila["importe_total"]), float(fila["cupon_descuento"])
        )
        for fila in _filas("atenciones_farmacia.csv")
    ]


def cargarHospital():
    pacientes = cargarPacientes()
    hospital = Hospital("Hospital San Roque")
    for atencion in cargarAtencionesMedicas(pacientes) + cargarAtencionesFarmacia():
        hospital.addAtencion(atencion)
    return hospital