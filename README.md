# Chatbot de Asistente Virtual en Streamlit

Este es un proyecto de un chatbot desarrollado con Streamlit y PostgreSQL para proporcionar asistencia virtual. El chatbot puede responder a preguntas y almacenar las conversaciones en una base de datos PostgreSQL.

## Descripción del Proyecto

El proyecto incluye:

- Un chatbot desarrollado con Streamlit.
- Conexión a una base de datos PostgreSQL para almacenar preguntas y respuestas.
- Implementación de procesamiento de lenguaje natural con `nltk`.
- Despliegue en Streamlit Cloud.
- Entrenamiento del modelo de chatbot con un archivo JSON de intenciones.

## Estructura del Proyecto

El proyecto tiene la siguiente estructura de archivos:

```bash
chatbot-streamlit/
│
├── app.py                  # Archivo principal de la aplicación
├── chatbot.py              # Archivo con las funciones de predicción y respuesta
├── intents.json            # Archivo JSON con las intenciones y patrones
├── requirements.txt        # Archivo con las dependencias del proyecto
├── .env                    # Archivo con las variables de entorno (no se sube a GitHub)
├── README.md               # Este archivo
└── modelos entrenados/
    ├── chatbot_model.h5    # Modelo de chatbot entrenado
    ├── words.pkl           # Palabras tokenizadas
    └── classes.pkl         # Clases de intenciones
```


## Requisitos

Para ejecutar este proyecto, necesitas tener instaladas las siguientes herramientas:

- Python 3.7+
- Streamlit
- psycopg2
- nltk
- keras
- numpy

## Configuración del Entorno

### 1. Clonar el Repositorio

Clona el repositorio en tu máquina local:

```bash
git clone https://github.com/NicoDataDesafio/DATA.git
cd DATA
```

### 2. Crear un Entorno Virtual

Crea y activa un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
```

### 3. Instalar Dependencias

Instala las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

### 4. Ejecución del Proyecto

Para ejecutar el chatbot localmente, usa el siguiente comando:

```bash
streamlit run app.py
```

Si prefieres ejecutar la aplicación desplegada en streamlit cloud entra a:

https://chatybe.streamlit.app/