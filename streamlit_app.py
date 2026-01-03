import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Załadowanie zmiennych środowiskowych
load_dotenv()

# Konfiguracja strony Streamlit
st.set_page_config(page_title="Chatbot", page_icon="🤖")
st.title("Mój Chatbot")

# Inicjalizacja klienta OpenAI
client = OpenAI()

# Inicjalizacja historii wiadomości i ID poprzedniej odpowiedzi
if "messages" not in st.session_state:
    st.session_state.messages = []
if "previous_response_id" not in st.session_state:
    st.session_state.previous_response_id = None

# Wyświetlanie historii wiadomości
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Pole wprowadzania wiadomości
if prompt := st.chat_input("W czym mogę Ci pomóc?"):
    # Dodanie wiadomości użytkownika do historii
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Wywołanie API OpenAI (zgodnie z logiką z app.py)
    with st.chat_message("assistant"):
        try:
            # Używamy tej samej logiki co w app.py
            response = client.responses.create(
                model='gpt-4.1-mini',
                input=prompt,
                previous_response_id=st.session_state.previous_response_id
            )
            
            output_text = response.output_text
            response_id = response.id
            
            st.markdown(output_text)
            
            # Zapisanie odpowiedzi asystenta i aktualizacja ID
            st.session_state.messages.append({"role": "assistant", "content": output_text})
            st.session_state.previous_response_id = response_id
            
        except Exception as e:
            st.error(f"Wystąpił błąd: {e}")
