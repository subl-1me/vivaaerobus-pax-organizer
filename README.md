# vivaaerobus-pax-organizer

**vivaaerobus-pax-organizer** es una aplicación de consola escrita en Python que monitorea constantemente una carpeta para detectar archivos PDF, extraer su contenido de texto, clasificar la información de los pasajeros y asignar habitaciones automáticamente. Su propósito es mantener un control organizado de los pasajeros y registrar la información localmente.

---

## Características

- Monitoreo continuo de una carpeta para detectar nuevos archivos `.pdf`
- Extracción automática de texto desde archivos PDF
- Identificación y clasificación de datos de pasajeros
- Asignación automática de habitaciones
- Registro y almacenamiento local de los datos procesados
- Informe de duplicados y errores

---

## Requisitos

- Python 3.8 o superior
- Dependencias (instalables vía `pip`):

```bash
pip install watchdog PyPDF2
```
