from datetime import datetime
import json
import os
def guardar(resultados):

    os.makedirs(
        "resultados",
        exist_ok=True
    )

    fecha = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    txt_path = (
        f"resultados/scan_{fecha}.txt"
    )

    json_path = (
        f"resultados/scan_{fecha}.json"
    )

    # =========================
    # TXT
    # =========================

    with open(
        txt_path,
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

    # =========================
    # JSON
    # =========================

    datos = []

    for puerto, servicio, banner in resultados:

        datos.append(
            {
                "puerto": puerto,
                "servicio": servicio,
                "banner": banner
            }
        )

    with open(
        json_path,
        "w",
        encoding="utf-8"
    ) as archivo:

        json.dump(
            datos,
            archivo,
            indent=4,
            ensure_ascii=False
        )

    return txt_path



import os

def listar_reportes():

    carpeta = "resultados"

    if not os.path.exists(carpeta):

        print(
            "\nNo hay reportes."
        )

        return None

    archivos = sorted(
        [
            f
            for f in os.listdir(carpeta)
            if f.endswith(".txt")
        ],
        reverse=True
    )   

    if not archivos:

        print(
            "\nNo hay reportes."
        )

        return None

    print()

    for i, archivo in enumerate(
        archivos,
        start=1
    ):

        print(
            f"[{i}] {archivo}"
        )

    return archivos

def abrir_reporte(archivo):

    ruta = os.path.join(
        "resultados",
        archivo
    )

    try:

        with open(
            ruta,
            "r",
            encoding="utf-8"
        ) as f:

            contenido = f.read()

        print()

        print("=" * 60)

        print(contenido)

        print("=" * 60)

    except Exception as e:

        print(
            f"\nError: {e}"
        )