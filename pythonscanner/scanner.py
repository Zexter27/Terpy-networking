import socket
import time
from concurrent.futures import ThreadPoolExecutor
from threading import Lock
from tabulate import tabulate

# ==========================
# VARIABLES GLOBALES
# ==========================

resultados = []

lock = Lock()

puertos_completados = 0
host_actual = ""
ip_actual = ""

total_escaneados = 0

tiempo_total = 0

# ==========================
# BARRA DE PROGRESO
# ==========================

def barra_progreso(completados, total):

    porcentaje = completados / total

    ancho = 30

    llenos = int(ancho * porcentaje)

    barra = (
        "█" * llenos +
        "░" * (ancho - llenos)
    )

    print(
        f"\r[{barra}] {porcentaje * 100:.1f}%",
        end="",
        flush=True
    )

# ==========================
# SERVICIOS
# ==========================

def ver_servicio(puerto):

    try:
        return socket.getservbyport(puerto)

    except OSError:
        return "desconocido"

# ==========================
# BANNER HTTP
# ==========================

def obtener_banner_http(host, puerto):

    try:

        with socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        ) as sock:

            sock.settimeout(2)

            sock.connect(
                (host, puerto)
            )

            peticion = (
                f"HEAD / HTTP/1.1\r\n"
                f"Host: {host}\r\n"
                f"Connection: close\r\n\r\n"
            )

            sock.send(
                peticion.encode()
            )

            respuesta = sock.recv(
                2048
            ).decode(
                errors="ignore"
            )

            return respuesta

    except:

        return "No disponible"

# ==========================
# BANNER GENERAL
# ==========================

def obtener_banner(host, puerto):

    try:

        if puerto in [80, 8080]:

            respuesta = obtener_banner_http(
                host,
                puerto
            )

            primera_linea = (
                respuesta
                .split("\n")[0]
                .strip()
            )

            return primera_linea

        with socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        ) as sock:

            sock.settimeout(2)

            sock.connect(
                (host, puerto)
            )

            banner = (
                sock.recv(1024)
                .decode(
                    errors="ignore"
                )
                .strip()
            )

            if banner:
                return banner[:60]

            return "Sin banner"

    except:

        return "No disponible"

# ==========================
# ESCANEO DE PUERTO
# ==========================

def escaneo(host, puerto, total):

    global puertos_completados

    try:

        with socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        ) as sock:

            sock.settimeout(0.5)

            if sock.connect_ex(
                (host, puerto)
            ) == 0:

                servicio = ver_servicio(
                    puerto
                )

                banner = obtener_banner(
                    host,
                    puerto
                )

                with lock:

                    resultados.append(
                        (
                            puerto,
                            servicio,
                            banner
                        )
                    )

    except:
        pass

    finally:

        with lock:

            puertos_completados += 1

            barra_progreso(
                puertos_completados,
                total
            )

# ==========================
# ESCANEO PRINCIPAL
# ==========================

def escanear(host, inicio, fin):

    global puertos_completados
    global host_actual
    global ip_actual
    global total_escaneados
    global tiempo_total

    resultados.clear()

    puertos_completados = 0

    host_actual = host

    try:

        ip_actual = socket.gethostbyname(
            host
        )

    except:

        ip_actual = "No resuelta"

    total = (
        fin -
        inicio +
        1
    )

    total_escaneados = total

    inicio_tiempo = (
        time.perf_counter()
    )

    with ThreadPoolExecutor(
        max_workers=100
    ) as executor:

        for puerto in range(
            inicio,
            fin + 1
        ):

            executor.submit(
                escaneo,
                host,
                puerto,
                total
            )

    tiempo_total = (
        time.perf_counter()
        - inicio_tiempo
    )

    print()

# ==========================
# TABLA DE RESULTADOS
# ==========================

def mostrar_resultados():

    if not resultados:

        print(
            "\nNo se encontraron "
            "puertos abiertos."
        )

        return

    resultados.sort()

    tabla = []

    for (
        puerto,
        servicio,
        banner
    ) in resultados:

        tabla.append(
            [
                puerto,
                servicio,
                banner[:50]
            ]
        )

    print()

    print(
        tabulate(
            tabla,
            headers=[
                "Puerto",
                "Servicio",
                "Banner"
            ],
            tablefmt="fancy_grid"
        )
    )


def mostrar_estadisticas():

    abiertos = len(
        resultados
    )

    cerrados = (
        total_escaneados
        - abiertos
    )

    print()

    print("=" * 60)

    print(
        "INFORMACIÓN DEL OBJETIVO"
    )

    print("=" * 60)

    print()

    print(
        f"Host................: "
        f"{host_actual}"
    )

    print(
        f"IP..................: "
        f"{ip_actual}"
    )

    print()

    print("=" * 60)

    print(
        "ESTADÍSTICAS"
    )

    print("=" * 60)

    print()

    print(
        f"Puertos escaneados..: "
        f"{total_escaneados}"
    )

    print(
        f"Abiertos............: "
        f"{abiertos}"
    )

    print(
        f"Cerrados............: "
        f"{cerrados}"
    )

    print(
        f"Tiempo..............: "
        f"{tiempo_total:.2f} segundos"
    )