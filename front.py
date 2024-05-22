import streamlit as st
from chatbot import predict_class, get_response, intents

st.set_option('deprecation.showfileUploaderEncoding', False)


st.set_page_config(page_title="Chaty",
                   page_icon="img/cropped-Beyond-Education_Horizonatal-color.png")

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

        st.markdown("Hola, ¿Como puedo ayudarte?")

    st.session_state.messages.append({"role": "assistant", "content": "Hola, como puedo ayudarte?"})
    st.session_state.first_message = False


if prompt := st.chat_input("cómo puedo ayudarte?"):

    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    #implementacion del algoritmo
    insts = predict_class(prompt)
    res = get_response(insts, intents)


    with st.chat_message("assistant"):
        st.markdown(res)

    st.session_state.messages.append({"role": "assistant", "content": res})


