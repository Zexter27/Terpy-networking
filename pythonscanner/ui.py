from colorama import (
    Fore,
    Style,
    init
)

init(
    autoreset=True
)

def banner():

    print(
        Fore.CYAN +
        """
████████╗███████╗██████╗ ██████╗ ██╗   ██╗
╚══██╔══╝██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝
   ██║   █████╗  ██████╔╝██████╔╝ ╚████╔╝
   ██║   ██╔══╝  ██╔══██╗██╔═══╝   ╚██╔╝
   ██║   ███████╗██║  ██║██║        ██║
   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝        ╚═╝
"""
    )

    print(
        Fore.YELLOW +
        "             ByZexter27\n"
    )

def menu():

    print(
        Fore.GREEN +
        "[1] Escanear puertos"
    )

    print(
        Fore.GREEN +
        "[2] Descubrir subdominios"
    )

    print(
        Fore.GREEN +
        "[3] Escaneo LAN"
    )

    print(
        Fore.GREEN +
        "[4] DNS Avanzado"
    )

    print(
        Fore.GREEN +
        "[5] Historial"
    )

    print(
        Fore.GREEN +
        "[6] Información de red"
    )

    print(
        Fore.RED +
        "[0] Salir"
    )

    return input(
        Fore.WHITE +
        "\nSeleccione una opción: "
    )