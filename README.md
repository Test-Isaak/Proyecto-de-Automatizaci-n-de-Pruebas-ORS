# Laboratorio 1: Introducción a Playwright - Interacciones Básicas con Elementos Web

## Descripción

Automatizacion de pruebas basicas para el entorno de https://www.automationexercise.com/.

## Funcionalidades automatizadas

- Escritura en campos de texto.
- Clic en botones.
- Selección de menús desplegables.
- Uso de checkbox y radio buttons.

## Instalación

- .venv\Scripts\activate.bat
- .venv\Scripts\python -m pip install --upgrade pip
- .venv\Scripts\pip install -e .
- .venv\Scripts\python -m playwright install chromium


## Ejecución

### Para ejecucion total de todas las pruebas

- pytest 

### Para ejecucion de pruebas individual

- pytest tests/test_contacto.py
- pytest tests/test_registro.py
- pytest tests/test_suscripcion.py
