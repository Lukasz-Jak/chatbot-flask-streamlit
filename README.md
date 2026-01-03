# Chatbot – Flask + Streamlit

Simple AI chatbot with Flask backend and Streamlit frontend.

---

## Stack
- Python 3.14
- Flask (backend API)
- Streamlit (frontend)
- OpenAI API

---

## Features
- Chat z zachowaniem kontekstu
- Frontend w Streamlit
- Backend REST API

---

## Uruchomienie projektu

### 1. Utworzenie środowiska wirtualnego

    python -m venv .venv

### 2. Instalacja zależności

    pip install -r requirements.txt

---

## Uruchamianie aplikacji

### Backend (Flask API)

    python app.py

### Frontend (Streamlit)

    streamlit run streamlit_app.py

Po uruchomieniu frontend będzie dostępny domyślnie pod adresem:

    http://localhost:8501

---

## Konfiguracja zmiennych środowiskowych

Utwórz plik `.env` w katalogu głównym projektu i dodaj:

    OPENAI_API_KEY=your_api_key_here

**Uwaga:**  
Plik `.env` nie jest wersjonowany i nie powinien być commitowany do repozytorium.
