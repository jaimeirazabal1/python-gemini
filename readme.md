# Interfaz de Usuario para la API de Gemini

Esta aplicación web, desarrollada con Flask, permite a los usuarios interactuar con la API de Gemini para generar contenido basado en entradas proporcionadas.

## Requisitos Previos

- Python 3.x instalado en su sistema.
- Clave de API válida para la API de Gemini.

## Instalación

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/jaimeirazabal1/python-gemini
   cd tu_repositorio
   ```

2. **Crear y activar un entorno virtual:**

   ```bash
   python -m venv venv
   source venv/bin/activate   # En Windows: venv\Scripts\activate
   ```

3. **Instalar las dependencias necesarias:**

   ```bash
   pip install -r requirements.txt
   ```

## Configuración

1. **Configurar la clave de API:**

   - Cree un archivo llamado `.env` en el directorio raíz del proyecto.
   - Añada la siguiente línea, reemplazando `tu_clave_de_api` con su clave de API de Gemini:

     ```env
     API_KEY=tu_clave_de_api
     ```

## Ejecución de la Aplicación

Inicie la aplicación ejecutando:

```bash
python app.py
```

La aplicación estará disponible en `http://127.0.0.1:5000/`.

## Uso

1. Acceda a la URL mencionada anteriormente en su navegador web.
2. Ingrese su consulta en el campo de texto proporcionado.
3. Presione el botón "Enviar" para recibir una respuesta generada por la API de Gemini.

## Estructura del Proyecto

- `app.py`: Archivo principal que contiene la lógica de la aplicación Flask.
- `templates/index.html`: Plantilla HTML que define la interfaz de usuario.
- `.env`: Archivo que almacena la clave de API de forma segura.
- `requirements.txt`: Lista de dependencias necesarias para la aplicación.

## Dependencias

Las dependencias necesarias para esta aplicación se encuentran en el archivo `requirements.txt`. Asegúrese de instalarlas antes de ejecutar la aplicación.

## Notas Adicionales

- Asegúrese de que su clave de API sea válida y tenga los permisos necesarios para interactuar con la API de Gemini.
- Mantenga su clave de API segura y no la comparta públicamente.
- Para personalizar la interfaz de usuario, modifique el archivo `index.html` ubicado en el directorio `templates`.

## Recursos

- [Documentación de Flask](https://flask.palletsprojects.com/)
- [Documentación de la API de Gemini](https://ai.google.dev/)

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulte el archivo `LICENSE` para obtener más detalles. 