import socket


def mostrar_info_red():

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

        print(
            f"\nIP Local: {ip}"
        )

    except:

        print(
            "\nNo se pudo obtener la IP."
        )