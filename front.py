import streamlit as st
import psycopg2
from chatbot import predict_class, get_response, intents
import nltk
nltk.download('punkt')
nltk.download('wordnet')

import os

my_database = os.environ.get('my_database')
my_host = os.environ.get('my_host')
my_password = os.environ.get('my_password')
my_port = os.environ.get('my_port')
my_user = os.environ.get('my_user')

my_database = "chatbot_8n2w"
my_host = "dpg-cp6qaka0si5c73aigcc0-a.frankfurt-postgres.render.com"
my_password = "UmxrGACXMb3Y1jaYLwnuS5zQDUBtXWg6"
my_port = 5432 
my_user = "chatbot_8n2w_user"

# Configura las variables de conexión
HOST = my_host
DATABASE = my_database
USER = my_user
PASSWORD = my_password
PORT = my_port  # Asegúrate de que este valor sea un entero

# Configura la conexión a la base de datos
def get_db_connection():
    return psycopg2.connect(
        host=HOST,
        database=DATABASE,
        user=USER,
        password=PASSWORD,
        port=PORT
    )

# Función para crear la tabla si no existe
def create_table_if_not_exists():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id SERIAL PRIMARY KEY,
            pregunta TEXT,
            respuesta TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

# Función para guardar una pregunta y su respuesta en la base de datos
def save_message_to_db(pregunta, respuesta):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (pregunta, respuesta) VALUES (%s, %s)", (pregunta, respuesta))
    conn.commit()
    cursor.close()
    conn.close()


# Crear la tabla si no existe
create_table_if_not_exists()

st.set_option('deprecation.showfileUploaderEncoding', False)
st.set_page_config(page_title="Chaty", page_icon="img/cropped-Beyond-Education_Horizonatal-color.png")

# Título

st.title(":male_mage: Asistente virtual:robot_face:")


if "messages" not in st.session_state:
    st.session_state.messages = []

if "first_message" not in st.session_state:
    st.session_state.first_message = True

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if st.session_state.first_message:
    with st.chat_message("assistant"):
        st.markdown("¡Hola! Soy Chaty, tu asistente virtual en Beyond Education. ¿Cómo puedo ayudarte hoy?")

    st.session_state.messages.append({"role": "assistant", "content": "¡Hola! Soy Chaty, tu asistente virtual en Beyond Education. ¿Cómo puedo ayudarte hoy?"})

    st.session_state.first_message = False

if prompt := st.chat_input("¿Cómo puedo ayudarte?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Implementación del algoritmo con manejo de errores
    try:
        insts = predict_class(prompt)
        res = get_response(insts, intents)
    except IndexError:
        res = "Perdona, no tengo clara la pregunta, ¿puedes reformularla?, aún soy 1.0 [:ghost:](https://pedrope.streamlit.app/)"

    with st.chat_message("assistant"):
        st.markdown(res)
    st.session_state.messages.append({"role": "assistant", "content": res})

    # Guardar pregunta y respuesta en la base de datos
    save_message_to_db(prompt.replace("DELETE", ""), res)
