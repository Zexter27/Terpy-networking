from datetime import datetime
import os

def guardar(resultados):

    os.makedirs(
        "resultados",
        exist_ok=True
    )

    nombre = datetime.now().strftime(
        "scan_%Y%m%d_%H%M%S.txt"
    )

    ruta = f"resultados/{nombre}"

    with open(
        ruta,
        "w",
        encoding="utf-8"
    ) as archivo:

        archivo.write(
            "=" * 60 + "\n"
        )

        archivo.write(
            "TERPY - REPORTE DE ESCANEO\n"
        )

        archivo.write(
            "=" * 60 + "\n\n"
        )

        for puerto, servicio, banner in resultados:

            archivo.write(
                f"{puerto}/tcp | "
                f"{servicio} | "
                f"{banner}\n"
            )

    return ruta