# Full Stack RPA Ashtronic

## Descripción
Este proyecto es una solución de Automatización Robótica de Procesos (RPA) diseñada para extraer información de facturación médica y pacientes desde un portal web externo, como parte de la prueba técnica para la empresa Ashtronic.

El sistema consta de una API REST desarrollada en **FastAPI** que gestiona la ejecución del bot, y un script de **Selenium** que navega, se autentica y extrae los datos requeridos, almacenándolos de forma estructurada en una base de datos **MySQL**.

## Arquitectura
El proyecto sigue una arquitectura de microservicios contenerizados:

1.  **API Service (App):**
    *   Construido con Python y FastAPI.
    *   Expone endpoints para iniciar trabajos de scraping y consultar estados.
    *   Ejecuta la lógica de negocio y orquesta el bot de Selenium.

2.  **Worker / Scraper (Selenium):**
    * Ejecutado bajo demanda por la API.
    * Navega el portal objetivo, maneja la autenticación y extrae datos de tablas dinámicas.

3.  **Database Service (DB):**
    *   Base de datos MySQL.
    *   Almacena dos entidades principales: `jobs` (historial de ejecuciones) y `patients` (datos extraídos).
    *   Persistencia de datos mediante volúmenes de Docker.

Los servicios se comunican dentro de una red privada gestionada por Docker Compose.

## Prerrequisitos
Para ejecutar este proyecto localmente, necesitas tener instalado:

*   Docker Desktop (incluye Docker Compose).
*   Git.

## Variables de Entorno
El proyecto utiliza variables de entorno para manejar credenciales sensibles.

1.  Busca el archivo `.env.example` en la raíz del proyecto.
2.  Haz una copia de este archivo y renómbralo a `.env`.
3.  Rellena los valores correspondientes.

> **Nota:** La variable `DB_HOST` debe ser `db` cuando se ejecuta con Docker, ya que es el nombre del servicio en la red interna.

## Cómo ejecutar
El despliegue está automatizado con Docker Compose. Sigue estos pasos:

1.  Abre una terminal en la carpeta raíz del proyecto.
2.  Ejecuta el siguiente comando para construir las imágenes e iniciar los contenedores:

    ```bash
    docker-compose up --build
    ```

3.  Espera a que finalice la construcción. Verás logs indicando que la base de datos está lista y la aplicación ha iniciado.

Para detener la aplicación, presiona `Ctrl + C` o ejecuta:
```bash
docker-compose down
```

## Cómo probar endpoints
La API cuenta con documentación interactiva automática (Swagger UI).

1.  Con el proyecto corriendo, abre tu navegador en:
    http://localhost:8000/docs

2.  Desde allí podrás ver todos los endpoints disponibles y probarlos directamente con el botón "Try it out".

## Decisiones Técnicas

*   **Docker:** Se eligió para garantizar que el entorno de ejecución sea idéntico en desarrollo y producción, eliminando problemas de dependencias.
*   **FastAPI:** Seleccionado por su rendimiento, facilidad de uso y generación automática de documentación, lo cual agiliza la integración y pruebas.
*   **Selenium:** Utilizado para el scraping debido a que el portal objetivo requiere interacción compleja con JavaScript (login, navegación por menús, modales).
*   **MySQL:** Se optó por una base de datos relacional para garantizar la integridad de los datos transaccionales (pacientes y trabajos) y facilitar consultas estructuradas.
*   **Separación de Responsabilidades:** La lógica de conexión a base de datos, el bot de RPA y la capa de API están modularizados para facilitar el mantenimiento y la escalabilidad.
*   **Estrategia de Extracción:**
    * El sitio objetivo utiliza tablas dinámicas que ocultan columnas (`display: none`) en resoluciones bajas.
    * **Decisión:** Se utilizó `.get_attribute('textContent')` en lugar de `.text` para extraer datos ocultos en el DOM sin necesidad de interacciones de UI innecesarias (clicks), mejorando la velocidad y estabilidad del bot.
*  **Persistencia y Trazabilidad:**
    * Se implementó un campo `raw_row_json` en la base de datos que almacena la fila tal cual se extrajo. Esto cumple con el requisito de auditoría, permitiendo depurar errores de parseo sin perder la data original.
    * Sistema de **Logging centralizado** en `app/core/logs` para monitorear la ejecución dentro del contenedor.
*   **Inicialización de Base de Datos (Bootstrapping)**:
    * Se utilizó un script de inicialización (`init.sql`) ya que se priorizó el despliegue automático. Al montar el script en el entrypoint de Docker, la base de datos se autoconfigura al levantar el contenedor, eliminando pasos manuales y garantizando un entorno reproducible sin dependencias externas.

## Próximos Pasos y Mejoras

Aunque la solución cumple con lo pedido en la prueba, he identificado varias formas de mejorar el proyecto para que sea más completo y robusto en el futuro:

1.  **Ejecución en Segundo Plano (Asincronía):**
    * **Situación actual:** Cuando pides una extracción, tienes que esperar a que el bot termine para recibir respuesta.
    * **Mejora:** Hacer que la API responda inmediatamente "Recibido" y que el bot trabaje por su cuenta, avisando al usuario (por ejemplo, por correo) cuando haya terminado. Así no se bloquea la aplicación si son muchos datos.

2.  **Interfaz Visual (Frontend):**
    * **Situación actual:** Se usa la interfaz de documentación (Swagger).
    * **Mejora:** Crear una página web sencilla con botones y tablas. Así, desde la cual se podría usar el bot, establecer parámetros, ver el progreso de las descargas y listar los resultados.

3.  **Mayor Tolerancia a Fallos (Robustez):**
    * **Situación actual:** El bot funciona bien con la estructura actual de la página.
    * **Mejora:** Hacer el bot más inteligente para que, si la página web cambia un poco (por ejemplo, si mueven un botón de lugar o cambia el ID de un elemento).

4.  **Despliegue en la Nube:**
    * **Situación actual:** El proyecto corre en máquina local.
    * **Mejora:** Subir los contenedores a un servidor en la nube como AWS para que el sistema esté disponible 24/7 y se pueda acceder desde cualquier lugar.

5.  **Reintentos Automáticos:**
    * **Situación actual:** Si la página se cae o el internet falla, el proceso se detiene y marca error.
    * **Mejora:** Programar el bot para que, si encuentra un error de conexión, espere unos segundos e intente de nuevo automáticamente un par de veces antes de rendirse.
