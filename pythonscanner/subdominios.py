SUBDOMINIOS = [
    "www",
    "mail",
    "ftp",
    "dev",
    "api",
    "admin",
    "test",
    "blog",
    "shop",
    "cdn"
]


import socket

def descubrir_subdominios(dominio):

    encontrados = []

    for sub in SUBDOMINIOS:

        host = f"{sub}.{dominio}"

        try:

            ip = socket.gethostbyname(
                host
            )

            encontrados.append(
                (
                    host,
                    ip
                )
            )

        except:
            pass

    return encontrados


import socket

def descubrir_subdominios(dominio):

    encontrados = []

    for sub in SUBDOMINIOS:

        host = f"{sub}.{dominio}"

        try:

            ip = socket.gethostbyname(
                host
            )

            encontrados.append(
                (
                    host,
                    ip
                )
            )

        except:
            pass

    return encontrados