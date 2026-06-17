# TERPY

```text
████████╗███████╗██████╗ ██████╗ ██╗   ██╗
╚══██╔══╝██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝
   ██║   █████╗  ██████╔╝██████╔╝ ╚████╔╝
   ██║   ██╔══╝  ██╔══██╗██╔═══╝   ╚██╔╝
   ██║   ███████╗██║  ██║██║        ██║
   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝        ╚═╝

            ByZexter27
```

TERPY es una herramienta de reconocimiento de red desarrollada en Python para aprender conceptos de networking, sockets, DNS y concurrencia.

## Características

* Escaneo de puertos TCP multihilo
* Barra de progreso en tiempo real
* Detección de servicios
* Banner Grabbing
* Descubrimiento de subdominios
* Escaneo de red local (LAN)
* Guardado de resultados
* Historial de escaneos
* Interfaz CLI con colores

## Requisitos

* Python 3.10 o superior

## Dependencias

Instalar las librerías necesarias:

```bash
pip install colorama
pip install tabulate
```

o

```bash
pip install colorama tabulate
```

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/Zexter27/Terpy-networking.git
```

Entrar al proyecto:

```bash
cd Terpy-networking
```

Instalar dependencias:

```bash
pip install colorama tabulate
```

Ejecutar:

```bash
python main.py
```

## Estructura del proyecto

```text
TERPY/
│
├── main.py
├── scanner.py
├── network_scanner.py
├── subdominios.py
├── storage.py
├── ui.py
│
└── resultados/
```

## Funciones

### Escaneo de puertos

Permite escanear un rango de puertos de un host objetivo.

Ejemplo:

```text
IP o dominio: scanme.nmap.org
Puerto inicial: 1
Puerto final: 1000
```

### Banner Grabbing

Obtiene información de los servicios encontrados en puertos abiertos.

Ejemplo:

```text
22/tcp  ssh   OpenSSH_9.6
80/tcp  http  HTTP/1.1 200 OK
```

### Escaneo LAN

Detecta hosts activos dentro de la red local.

Ejemplo:

```text
IP local detectada: 192.168.1.25
Red sugerida: 192.168.1.0/24
```

Resultado:

```text
192.168.1.1
192.168.1.10
192.168.1.15
```

### Descubrimiento de subdominios

Busca subdominios comunes asociados a un dominio.

Ejemplo:

```text
www.dominio.com
mail.dominio.com
api.dominio.com
```

## Resultados

Los reportes se almacenan automáticamente en:

```text
resultados/
```

Formato:

```text
22/tcp | ssh | OpenSSH_9.6
80/tcp | http | HTTP/1.1 200 OK
```

## Tecnologías utilizadas

* Python
* Socket
* ThreadPoolExecutor
* Colorama
* Tabulate

## Autor

**Zexter27**

Proyecto desarrollado con fines educativos y de aprendizaje en networking y programación.
