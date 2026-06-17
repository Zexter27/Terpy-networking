import socket
import ipaddress
from concurrent.futures import ThreadPoolExecutor
from threading import Lock
from tabulate import tabulate

hosts_activos = []

lock = Lock()

PUERTOS_COMUNES = [
    22,
    80,
    443,
    445,
    3389
]


def obtener_ip_local():

    try:

        s = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM
        )

        s.connect(
            ("8.8.8.8", 80)
        )

        ip = s.getsockname()[0]

        s.close()

        return ip

    except:

        return None


def sugerir_red():

    ip = obtener_ip_local()

    if not ip:

        return None

    partes = ip.split(".")

    return (
        f"{partes[0]}."
        f"{partes[1]}."
        f"{partes[2]}."
        "0/24"
    )


def host_activo(ip):

    for puerto in PUERTOS_COMUNES:

        try:

            with socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM
            ) as sock:

                sock.settimeout(0.3)

                if sock.connect_ex(
                    (str(ip), puerto)
                ) == 0:

                    return True

        except:
            pass

    return False


def verificar_host(ip):

    if host_activo(ip):

        with lock:

            hosts_activos.append(
                str(ip)
            )

            print(
                f"[+] Host activo: {ip}"
            )


def escanear_red(red):

    global hosts_activos

    hosts_activos = []

    try:

        network = ipaddress.ip_network(
            red,
            strict=False
        )

    except ValueError:

        print(
            "\n[!] Red inválida"
        )

        return []

    total = len(
        list(network.hosts())
    )

    print(
        f"\n[*] Escaneando {total} hosts..."
    )

    with ThreadPoolExecutor(
        max_workers=100
    ) as executor:

        for ip in network.hosts():

            executor.submit(
                verificar_host,
                ip
            )

    return hosts_activos


def mostrar_hosts(hosts):

    if not hosts:

        print(
            "\n[!] No se encontraron hosts activos."
        )

        return

    tabla = []

    for host in sorted(hosts):

        tabla.append(
            [host]
        )

    print()

    print(
        tabulate(
            tabla,
            headers=[
                "Hosts Activos"
            ],
            tablefmt="fancy_grid"
        )
    )