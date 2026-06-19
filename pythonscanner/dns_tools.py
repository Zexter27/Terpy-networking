import dns.resolver


def consultar_dns(dominio):

    tipos = [
        "A",
        "AAAA",
        "MX",
        "NS",
        "TXT"
    ]

    for tipo in tipos:

        print(f"\n[{tipo}]")

        try:

            respuestas = dns.resolver.resolve(
                dominio,
                tipo
            )

            for r in respuestas:

                print(r)

        except Exception:

            print("No disponible")