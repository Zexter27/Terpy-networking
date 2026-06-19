from ui import *
from scanner import *
from storage import *
from network_scanner import *
from dns_tools import *
from network_info import *
from network_scanner import *

while True:

    banner()

    opcion = menu()

    if opcion == "1":

        host = input(
            "\nIP o dominio: "
        )

        inicio = int(
            input("Puerto inicial: ")
        )

        fin = int(
            input("Puerto final: ")
        )

        resultados.clear()

        escanear(
            host,
            inicio,
            fin
        )

        mostrar_resultados()

        mostrar_estadisticas()

        ruta = guardar(
            resultados
        )

        print(
            f"\nResultados guardados en:"
        )

        print(ruta)

    elif opcion == "2":

        red_sugerida = sugerir_red()

        if red_sugerida:

            print(
                f"\nIP local detectada: "
                f"{obtener_ip_local()}"
            )

            print(
                f"Red sugerida: "
                f"{red_sugerida}"
            )

            usar = input(
                "\n¿Usar esta red? (S/N): "
            ).lower()

            if usar == "s":

                red = red_sugerida

            else:

                red = input(
                    "\nIngrese la red: "
                )

        else:

            red = input(
                "\nIngrese la red: "
            )

        hosts = escanear_red(
            red
        )

        mostrar_hosts(
            hosts
        )

        input(
            "\nENTER para continuar..."
        )

    elif opcion == "3":

        print(
            "\nFunción en desarrollo..."
        )

        input(
            "\nENTER para continuar..."
        )
    elif opcion == "4":

        dominio = input(
            "\nDominio: "
        )

        consultar_dns(
            dominio
        )

        input(
            "\nENTER para continuar..."
        )


    elif opcion == "5":

        archivos = listar_reportes()

        if archivos:

            try:

                seleccion = int(
                    input(
                        "\nSeleccione reporte: "
                    )
                )

                if (
                    1 <= seleccion <=
                    len(archivos)
                ):

                    abrir_reporte(
                        archivos[
                            seleccion - 1
                        ]
                    )

            except:

                print(
                    "\nSelección inválida."
                )

        input(
            "\nENTER para continuar..."
        )

    elif opcion == "6":

        mostrar_info_red()

        input(
            "\nENTER para continuar..."
        )


    elif opcion == "0":

        print(
            "\nHasta luego."
        )

        break

    else:

        print(
            "\nOpción inválida."
        )

        input(
            "\nENTER para continuar..."
        )